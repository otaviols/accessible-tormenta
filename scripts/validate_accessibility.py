"""
Script de Validação de Acessibilidade para Markdown
Detecta problemas de acessibilidade em arquivos markdown do projeto Tormenta20.

Uso:
    python validate_accessibility.py [--verbose] [--summary] [--book BOOK_NAME]
    
Exemplos:
    python validate_accessibility.py --book dragao-brasil
    python validate_accessibility.py --summary
    python validate_accessibility.py --verbose --book herois-arton
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import argparse


@dataclass
class Issue:
    """Representa um problema de acessibilidade encontrado."""
    file_path: Path
    line_number: int
    issue_type: str
    description: str
    line_content: str
    
    def __str__(self):
        return f"{self.file_path}:{self.line_number} [{self.issue_type}] {self.description}"


@dataclass
class ValidationReport:
    """Relatório de validação de acessibilidade."""
    issues: List[Issue] = field(default_factory=list)
    files_checked: int = 0
    
    def add_issue(self, issue: Issue):
        self.issues.append(issue)
    
    def get_by_type(self, issue_type: str) -> List[Issue]:
        return [i for i in self.issues if i.issue_type == issue_type]
    
    def get_by_file(self, file_path: Path) -> List[Issue]:
        return [i for i in self.issues if i.file_path == file_path]
    
    def has_issues(self) -> bool:
        return len(self.issues) > 0
    
    def count_by_type(self) -> Dict[str, int]:
        counts = defaultdict(int)
        for issue in self.issues:
            counts[issue.issue_type] += 1
        return dict(counts)


class AccessibilityValidator:
    """Validador de acessibilidade para arquivos Markdown."""
    
    # Padrões de problemas
    PATTERNS = {
        'table_header_row': re.compile(r'^\|\s*\*\*[^*]+\*\*\s*\|'),
        'bold_item_description': re.compile(r'^\*\*([^*]+)\.\*\*\s+(.+)'),
        'invalid_placeholder': re.compile(r'\|\s*\*\*\s*\|'),
        'table_row': re.compile(r'^\|.+\|$'),
        'heading': re.compile(r'^(#{1,6})\s+(.+)$'),
        'table_separator': re.compile(r'^\|[\s\-:]+\|$'),
    }
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.report = ValidationReport()
    
    def validate_file(self, file_path: Path) -> List[Issue]:
        """Valida um único arquivo markdown."""
        issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            self.report.files_checked += 1
            
            # Validar problemas linha por linha
            in_table = False
            table_start_line = 0
            previous_heading_level = 0
            
            for i, line in enumerate(lines, 1):
                line_stripped = line.strip()
                
                # Detectar início/fim de tabela
                if self.PATTERNS['table_separator'].match(line_stripped):
                    if not in_table:
                        in_table = True
                        table_start_line = i
                elif in_table and not self.PATTERNS['table_row'].match(line_stripped):
                    in_table = False
                
                # 1. Cabeçalhos em linhas de tabela
                if in_table and self.PATTERNS['table_header_row'].match(line_stripped):
                    issue = Issue(
                        file_path=file_path,
                        line_number=i,
                        issue_type='table_header_in_row',
                        description='Cabeçalho de categoria dentro de linha de tabela (deve ser H4 antes da tabela)',
                        line_content=line_stripped
                    )
                    issues.append(issue)
                    self.report.add_issue(issue)
                
                # 2. Placeholders inválidos
                if in_table and self.PATTERNS['invalid_placeholder'].match(line_stripped):
                    # Verificar se é realmente um placeholder (não é cabeçalho de tabela)
                    if not line_stripped.startswith('|---'):
                        issue = Issue(
                            file_path=file_path,
                            line_number=i,
                            issue_type='invalid_placeholder',
                            description='Placeholder inválido "**" em célula (use "—" para N/A)',
                            line_content=line_stripped
                        )
                        issues.append(issue)
                        self.report.add_issue(issue)
                
                # 3. Itens com formato **Nome.** em vez de cabeçalho
                if not in_table:
                    match = self.PATTERNS['bold_item_description'].match(line_stripped)
                    if match:
                        # Verificar se não é início de frase normal
                        item_name = match.group(1)
                        # Se o nome tem mais de 3 palavras, provavelmente é texto normal
                        if len(item_name.split()) <= 4:
                            issue = Issue(
                                file_path=file_path,
                                line_number=i,
                                issue_type='item_without_heading',
                                description=f'Item "{item_name}" usa **Nome.** em vez de cabeçalho ### Nome',
                                line_content=line_stripped
                            )
                            issues.append(issue)
                            self.report.add_issue(issue)
                
                # 4. Hierarquia de cabeçalhos (pulos de nível)
                heading_match = self.PATTERNS['heading'].match(line_stripped)
                if heading_match:
                    level = len(heading_match.group(1))
                    
                    # Ignorar H1 (sempre válido)
                    if level > 1 and previous_heading_level > 0:
                        # Pulo de mais de 1 nível
                        if level > previous_heading_level + 1:
                            issue = Issue(
                                file_path=file_path,
                                line_number=i,
                                issue_type='heading_skip',
                                description=f'Pulo de hierarquia: H{previous_heading_level} → H{level} (deve ser H{previous_heading_level + 1})',
                                line_content=line_stripped
                            )
                            issues.append(issue)
                            self.report.add_issue(issue)
                    
                    previous_heading_level = level
            
            # 5. Verificar tabelas incompletas (última linha é separador)
            if in_table and len(lines) > 0:
                last_line = lines[-1].strip()
                if self.PATTERNS['table_separator'].match(last_line):
                    issue = Issue(
                        file_path=file_path,
                        line_number=len(lines),
                        issue_type='incomplete_table',
                        description='Tabela parece incompleta (termina com separador)',
                        line_content=last_line
                    )
                    issues.append(issue)
                    self.report.add_issue(issue)
        
        except Exception as e:
            print(f"Erro ao processar {file_path}: {e}", file=sys.stderr)
        
        return issues
    
    def validate_directory(self, directory: Path, exclude_dirs: List[str] = None) -> ValidationReport:
        """Valida todos os arquivos markdown em um diretório."""
        if exclude_dirs is None:
            exclude_dirs = ['_imagens', '__pycache__', '.git', 'node_modules']
        
        md_files = []
        for md_file in directory.rglob('*.md'):
            # Excluir diretórios específicos
            if any(excl in md_file.parts for excl in exclude_dirs):
                continue
            md_files.append(md_file)
        
        if self.verbose:
            print(f"\nValidando {len(md_files)} arquivos markdown em {directory}...")
        
        for md_file in md_files:
            self.validate_file(md_file)
        
        return self.report
    
    def print_report(self, summary_only: bool = False):
        """Imprime o relatório de validação."""
        print("\n" + "="*80)
        print("RELATÓRIO DE VALIDAÇÃO DE ACESSIBILIDADE")
        print("="*80)
        
        print(f"\nArquivos verificados: {self.report.files_checked}")
        print(f"Total de problemas encontrados: {len(self.report.issues)}")
        
        if len(self.report.issues) == 0:
            print("\n✅ Nenhum problema de acessibilidade encontrado!")
            return
        
        # Resumo por tipo
        print("\n" + "-"*80)
        print("RESUMO POR TIPO DE PROBLEMA")
        print("-"*80)
        
        type_counts = self.report.count_by_type()
        type_names = {
            'table_header_in_row': 'Cabeçalhos em linhas de tabela',
            'invalid_placeholder': 'Placeholders inválidos',
            'item_without_heading': 'Itens sem cabeçalho',
            'heading_skip': 'Pulos na hierarquia de cabeçalhos',
            'incomplete_table': 'Tabelas incompletas'
        }
        
        for issue_type, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
            type_name = type_names.get(issue_type, issue_type)
            print(f"  {type_name}: {count}")
        
        if summary_only:
            # Resumo por arquivo
            print("\n" + "-"*80)
            print("ARQUIVOS COM PROBLEMAS")
            print("-"*80)
            
            files_with_issues = defaultdict(int)
            for issue in self.report.issues:
                files_with_issues[issue.file_path] += 1
            
            for file_path, count in sorted(files_with_issues.items(), key=lambda x: x[1], reverse=True):
                # Mostrar caminho relativo a partir de 'livros/'
                try:
                    rel_path = file_path.relative_to(file_path.parts[0])
                    for i, part in enumerate(file_path.parts):
                        if part == 'livros':
                            rel_path = Path(*file_path.parts[i:])
                            break
                except:
                    rel_path = file_path
                
                print(f"  {rel_path}: {count} problema(s)")
        else:
            # Detalhes completos
            print("\n" + "-"*80)
            print("DETALHES DOS PROBLEMAS")
            print("-"*80)
            
            # Agrupar por arquivo
            by_file = defaultdict(list)
            for issue in self.report.issues:
                by_file[issue.file_path].append(issue)
            
            for file_path, file_issues in sorted(by_file.items()):
                # Mostrar caminho relativo
                try:
                    rel_path = file_path.relative_to(file_path.parts[0])
                    for i, part in enumerate(file_path.parts):
                        if part == 'livros':
                            rel_path = Path(*file_path.parts[i:])
                            break
                except:
                    rel_path = file_path
                
                print(f"\n📄 {rel_path} ({len(file_issues)} problema(s))")
                
                for issue in sorted(file_issues, key=lambda x: x.line_number):
                    print(f"  Linha {issue.line_number}: [{issue.issue_type}]")
                    print(f"    {issue.description}")
                    if self.verbose and issue.line_content:
                        print(f"    Conteúdo: {issue.line_content[:100]}...")
        
        print("\n" + "="*80)


def main():
    parser = argparse.ArgumentParser(
        description='Valida acessibilidade de arquivos Markdown do projeto Tormenta20'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Mostra informações detalhadas durante a validação'
    )
    parser.add_argument(
        '--summary', '-s',
        action='store_true',
        help='Mostra apenas resumo (sem detalhes de cada problema)'
    )
    parser.add_argument(
        '--book', '-b',
        type=str,
        help='Valida apenas um livro específico (tormenta20-core, dragao-brasil, herois-arton, ameacas-arton)'
    )
    
    args = parser.parse_args()
    
    # Determinar diretório base
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    livros_dir = project_root / 'livros'
    
    if not livros_dir.exists():
        print(f"Erro: Diretório 'livros' não encontrado em {project_root}", file=sys.stderr)
        sys.exit(1)
    
    validator = AccessibilityValidator(verbose=args.verbose)
    
    # Determinar quais livros validar
    if args.book:
        book_dir = livros_dir / args.book
        if not book_dir.exists():
            print(f"Erro: Livro '{args.book}' não encontrado em {livros_dir}", file=sys.stderr)
            sys.exit(1)
        validator.validate_directory(book_dir)
    else:
        # Validar todos os livros
        for book_dir in livros_dir.iterdir():
            if book_dir.is_dir() and not book_dir.name.startswith('_'):
                if args.verbose:
                    print(f"\n{'='*80}")
                    print(f"Validando livro: {book_dir.name}")
                    print(f"{'='*80}")
                validator.validate_directory(book_dir)
    
    # Imprimir relatório
    validator.print_report(summary_only=args.summary)
    
    # Retornar código de erro se houver problemas
    sys.exit(1 if validator.report.has_issues() else 0)


if __name__ == '__main__':
    main()

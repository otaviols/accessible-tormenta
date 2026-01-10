#!/usr/bin/env python3
"""
Script para normalizar frontmatter YAML em arquivos markdown.

Converte navegação inline para frontmatter YAML e padroniza campos.

Uso:
    python scripts/normalize_frontmatter.py livros/tormenta20-core/ --fix
    python scripts/normalize_frontmatter.py livros/herois-arton/ --validate
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, Optional, Tuple


class FrontmatterNormalizer:
    """Normaliza frontmatter YAML em arquivos markdown."""
    
    def __init__(self, book_path: str):
        """
        Inicializa normalizador para um livro específico.
        
        Args:
            book_path: Caminho para o diretório do livro
        """
        self.book_path = Path(book_path)
        self.book_name = self.book_path.name
        self.stats = {
            'files_processed': 0,
            'files_with_frontmatter': 0,
            'files_without_frontmatter': 0,
            'files_modified': 0,
            'errors': []
        }
    
    def process_all(self, fix: bool = False) -> Dict:
        """
        Processa todos os arquivos .md do livro.
        
        Args:
            fix: Se True, modifica arquivos. Se False, apenas valida.
        
        Returns:
            Dicionário com estatísticas
        """
        mode = "CORRIGINDO" if fix else "VALIDANDO"
        print(f"\n{mode} frontmatter em: {self.book_path}")
        print("=" * 70)
        
        md_files = list(self.book_path.rglob("*.md"))
        print(f"Arquivos .md encontrados: {len(md_files)}\n")
        
        for md_file in md_files:
            try:
                self.process_file(md_file, fix)
            except Exception as e:
                error_msg = f"Erro em {md_file}: {str(e)}"
                self.stats['errors'].append(error_msg)
                print(f"ERRO: {error_msg}")
        
        self.print_summary()
        return self.stats
    
    def process_file(self, file_path: Path, fix: bool = False):
        """
        Processa um arquivo específico.
        
        Args:
            file_path: Caminho do arquivo .md
            fix: Se True, modifica o arquivo
        """
        self.stats['files_processed'] += 1
        
        content = file_path.read_text(encoding='utf-8')
        
        # Verificar se já tem frontmatter
        has_frontmatter = content.startswith('---\n')
        
        if has_frontmatter:
            self.stats['files_with_frontmatter'] += 1
            # Validar frontmatter existente
            if not self.validate_frontmatter(content, file_path):
                if fix:
                    # Tentar corrigir
                    new_content = self.fix_frontmatter(content, file_path)
                    if new_content != content:
                        file_path.write_text(new_content, encoding='utf-8')
                        self.stats['files_modified'] += 1
                        print(f"OK Corrigido: {file_path.relative_to(self.book_path)}")
        else:
            self.stats['files_without_frontmatter'] += 1
            # Converter navegação inline para frontmatter
            if fix:
                new_content = self.add_frontmatter(content, file_path)
                if new_content != content:
                    file_path.write_text(new_content, encoding='utf-8')
                    self.stats['files_modified'] += 1
                    print(f"OK Adicionado frontmatter: {file_path.relative_to(self.book_path)}")
            else:
                print(f"AVISO Sem frontmatter: {file_path.relative_to(self.book_path)}")
    
    def validate_frontmatter(self, content: str, file_path: Path) -> bool:
        """
        Valida se frontmatter está completo e correto.
        
        Args:
            content: Conteúdo do arquivo
            file_path: Caminho do arquivo
        
        Returns:
            True se válido, False caso contrário
        """
        # Extrair frontmatter
        match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not match:
            return False
        
        frontmatter = match.group(1)
        
        # Verificar campos obrigatórios
        required_fields = ['title', 'navigation']
        for field in required_fields:
            if field not in frontmatter:
                return False
        
        return True
    
    def fix_frontmatter(self, content: str, file_path: Path) -> str:
        """
        Corrige frontmatter existente.
        
        Args:
            content: Conteúdo do arquivo
            file_path: Caminho do arquivo
        
        Returns:
            Conteúdo com frontmatter corrigido
        """
        # Extrair frontmatter e conteúdo
        match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if not match:
            return content
        
        frontmatter = match.group(1)
        body = match.group(2)
        
        # Extrair campos existentes
        title = self.extract_field(frontmatter, 'title')
        if not title:
            # Tentar extrair do primeiro heading
            heading_match = re.search(r'^# (.+)$', body, re.MULTILINE)
            if heading_match:
                title = heading_match.group(1)
        
        # Construir novo frontmatter
        new_frontmatter = self.build_frontmatter(file_path, title, frontmatter)
        
        return f"---\n{new_frontmatter}\n---\n{body}"
    
    def add_frontmatter(self, content: str, file_path: Path) -> str:
        """
        Adiciona frontmatter a arquivo que não tem.
        
        Args:
            content: Conteúdo do arquivo
            file_path: Caminho do arquivo
        
        Returns:
            Conteúdo com frontmatter adicionado
        """
        # Extrair título do primeiro heading
        heading_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = heading_match.group(1) if heading_match else file_path.stem
        
        # Extrair navegação inline se existir
        nav_pattern = r'\[← Anterior: ([^\]]+)\]\(([^)]+)\)\s*\|\s*\[Próximo: ([^\]]+) →\]\(([^)]+)\)'
        nav_match = re.search(nav_pattern, content)
        
        prev_file = nav_match.group(2) if nav_match else None
        next_file = nav_match.group(4) if nav_match else None
        
        # Remover navegação inline do conteúdo
        if nav_match:
            content = content.replace(nav_match.group(0), '').strip()
            # Remover linha em branco extra
            content = re.sub(r'\n{3,}', '\n\n', content)
        
        # Construir frontmatter
        frontmatter = self.build_frontmatter(file_path, title, None, prev_file, next_file)
        
        return f"---\n{frontmatter}\n---\n\n{content}"
    
    def build_frontmatter(self, file_path: Path, title: Optional[str], 
                         existing_fm: Optional[str] = None,
                         prev_file: Optional[str] = None,
                         next_file: Optional[str] = None) -> str:
        """
        Constrói frontmatter YAML padronizado.
        
        Args:
            file_path: Caminho do arquivo
            title: Título do arquivo
            existing_fm: Frontmatter existente (para preservar campos)
            prev_file: Arquivo anterior (navegação)
            next_file: Próximo arquivo (navegação)
        
        Returns:
            String com frontmatter YAML
        """
        # Determinar capítulo baseado no caminho
        parts = file_path.relative_to(self.book_path).parts
        chapter = parts[0] if len(parts) > 1 else ""
        
        # Extrair navegação de frontmatter existente se disponível
        if existing_fm:
            prev_file = prev_file or self.extract_nav_field(existing_fm, 'previous')
            next_file = next_file or self.extract_nav_field(existing_fm, 'next')
        
        # Construir YAML
        yaml_lines = []
        yaml_lines.append(f'title: "{title}"')
        yaml_lines.append(f'book: "{self.book_name}"')
        
        if chapter:
            yaml_lines.append(f'chapter: "{chapter}"')
        
        yaml_lines.append('navigation:')
        yaml_lines.append(f'  previous: {self.format_nav_value(prev_file)}')
        yaml_lines.append(f'  next: {self.format_nav_value(next_file)}')
        yaml_lines.append('  up: "README.md"')
        
        return '\n'.join(yaml_lines)
    
    def extract_field(self, frontmatter: str, field: str) -> Optional[str]:
        """Extrai valor de campo do frontmatter."""
        pattern = f'^{field}:\\s*"?([^"\\n]+)"?$'
        match = re.search(pattern, frontmatter, re.MULTILINE)
        return match.group(1) if match else None
    
    def extract_nav_field(self, frontmatter: str, nav_field: str) -> Optional[str]:
        """Extrai campo de navegação do frontmatter."""
        pattern = f'^\\s*{nav_field}:\\s*"?([^"\\n]+)"?$'
        match = re.search(pattern, frontmatter, re.MULTILINE)
        value = match.group(1) if match else None
        return value if value and value != 'null' else None
    
    def format_nav_value(self, value: Optional[str]) -> str:
        """Formata valor de navegação para YAML."""
        if not value or value == 'null':
            return 'null'
        # Se já tiver aspas, manter
        if value.startswith('"') and value.endswith('"'):
            return value
        return f'"{value}"'
    
    def print_summary(self):
        """Imprime resumo do processamento."""
        print("\n" + "=" * 70)
        print("RESUMO DO PROCESSAMENTO")
        print("=" * 70)
        print(f"Arquivos processados: {self.stats['files_processed']}")
        print(f"Arquivos com frontmatter: {self.stats['files_with_frontmatter']}")
        print(f"Arquivos sem frontmatter: {self.stats['files_without_frontmatter']}")
        print(f"Arquivos modificados: {self.stats['files_modified']}")
        
        if self.stats['errors']:
            print(f"\nAVISO: Erros encontrados: {len(self.stats['errors'])}")
            for error in self.stats['errors']:
                print(f"   - {error}")
        else:
            print("\nOK: Nenhum erro encontrado!")
        
        print("=" * 70 + "\n")


def main():
    """Função principal do script."""
    
    if len(sys.argv) < 2:
        print("❌ ERRO: Caminho do livro não especificado")
        print("\nUso:")
        print("    python scripts/normalize_frontmatter.py livros/tormenta20-core/ --fix")
        print("    python scripts/normalize_frontmatter.py livros/herois-arton/ --validate")
        print("\nOpções:")
        print("    --fix        Modifica arquivos para corrigir/adicionar frontmatter")
        print("    --validate   Apenas valida sem modificar (padrão)")
        sys.exit(1)
    
    book_path = sys.argv[1]
    fix = '--fix' in sys.argv
    
    # Verificar se caminho existe
    if not os.path.exists(book_path):
        print(f"❌ ERRO: Caminho não encontrado: {book_path}")
        sys.exit(1)
    
    # Executar normalização
    normalizer = FrontmatterNormalizer(book_path)
    stats = normalizer.process_all(fix=fix)
    
    # Código de saída baseado em erros
    if stats['errors']:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()

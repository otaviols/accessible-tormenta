#!/usr/bin/env python3
"""
Script para migrar links internos após reorganização multi-livros.

Atualiza:
- Caminhos de imagens (../imagens/ → ../../_imagens/livro/)
- Referências a arquivos renumerados (18-duende.md → 01-duende.md)
- Links relativos entre capítulos

Uso:
    python scripts/migrate_links.py livros/tormenta20-core/
    python scripts/migrate_links.py livros/herois-arton/
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


class LinkMigrator:
    """Migra links internos para nova estrutura multi-livros."""
    
    # Mapeamento de arquivos renumerados (Heróis de Arton - raças)
    RENAMED_FILES = {
        '18-duende.md': '01-duende.md',
        '19-eiradaan.md': '02-eiradaan.md',
        '20-galokk.md': '03-galokk.md',
        '21-meio-elfo.md': '04-meio-elfo.md',
        '22-satiro.md': '05-satiro.md',
    }
    
    def __init__(self, book_path: str):
        """
        Inicializa migrador para um livro específico.
        
        Args:
            book_path: Caminho para o diretório do livro (ex: livros/tormenta20-core/)
        """
        self.book_path = Path(book_path)
        self.book_name = self.book_path.name
        self.stats = {
            'files_processed': 0,
            'files_modified': 0,
            'image_links_updated': 0,
            'file_links_updated': 0,
            'errors': []
        }
    
    def migrate_all(self, dry_run: bool = False) -> Dict:
        """
        Migra todos os arquivos .md do livro.
        
        Args:
            dry_run: Se True, apenas mostra o que seria feito sem modificar
        
        Returns:
            Dicionário com estatísticas da migração
        """
        print(f"\n{'[DRY RUN] ' if dry_run else ''}Migrando links em: {self.book_path}")
        print("=" * 70)
        
        # Encontrar todos arquivos .md
        md_files = list(self.book_path.rglob("*.md"))
        print(f"Arquivos .md encontrados: {len(md_files)}\n")
        
        for md_file in md_files:
            try:
                self.migrate_file(md_file, dry_run)
            except Exception as e:
                error_msg = f"Erro em {md_file}: {str(e)}"
                self.stats['errors'].append(error_msg)
                print(f"❌ {error_msg}")
        
        self.print_summary()
        return self.stats
    
    def migrate_file(self, file_path: Path, dry_run: bool = False):
        """
        Migra links em um arquivo específico.
        
        Args:
            file_path: Caminho do arquivo .md
            dry_run: Se True, apenas analisa sem modificar
        """
        self.stats['files_processed'] += 1
        
        # Ler conteúdo
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        
        # Aplicar migrações
        content = self.migrate_image_links(content, file_path)
        content = self.migrate_renamed_files(content, file_path)
        
        # Verificar se houve mudanças
        if content != original_content:
            self.stats['files_modified'] += 1
            
            if not dry_run:
                # Salvar arquivo modificado
                file_path.write_text(content, encoding='utf-8')
                print(f"✓ {file_path.relative_to(self.book_path)}")
            else:
                print(f"[DRY RUN] Modificaria: {file_path.relative_to(self.book_path)}")
    
    def migrate_image_links(self, content: str, file_path: Path) -> str:
        """
        Atualiza links de imagens para nova estrutura.
        
        Converte:
            ../imagens/arquivo.png → ../../_imagens/livro-name/arquivo.png
            ../../imagens/arquivo.png → ../../../_imagens/livro-name/arquivo.png
        
        Args:
            content: Conteúdo do arquivo
            file_path: Caminho do arquivo (para calcular profundidade)
        
        Returns:
            Conteúdo com links atualizados
        """
        # Padrão para links de imagens markdown: ![alt](caminho)
        image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        
        def replace_image(match):
            alt_text = match.group(1)
            old_path = match.group(2)
            
            # Ignorar URLs absolutos
            if old_path.startswith('http://') or old_path.startswith('https://'):
                return match.group(0)
            
            # Ignorar se já está no formato novo
            if '/_imagens/' in old_path:
                return match.group(0)
            
            # Verificar se é link de imagem (termina com extensão de imagem)
            if not re.search(r'\.(png|jpg|jpeg|gif|svg|webp)$', old_path, re.IGNORECASE):
                return match.group(0)
            
            # Converter caminho
            if '/imagens/' in old_path or old_path.startswith('imagens/'):
                # Contar níveis de ../ no caminho original
                levels = old_path.count('../')
                
                # Extrair nome do arquivo de imagem
                image_name = old_path.split('/')[-1]
                
                # Construir novo caminho
                # Se estava em ../imagens/, agora será ../../_imagens/livro/
                # Se estava em ../../imagens/, agora será ../../../_imagens/livro/
                new_levels = levels + 1  # Adiciona um nível por causa de livros/
                prefix = '../' * new_levels
                new_path = f"{prefix}_imagens/{self.book_name}/{image_name}"
                
                self.stats['image_links_updated'] += 1
                return f'![{alt_text}]({new_path})'
            
            return match.group(0)
        
        return re.sub(image_pattern, replace_image, content)
    
    def migrate_renamed_files(self, content: str, file_path: Path) -> str:
        """
        Atualiza referências a arquivos renumerados.
        
        Converte:
            18-duende.md → 01-duende.md
            [Duende](18-duende.md) → [Duende](01-duende.md)
        
        Args:
            content: Conteúdo do arquivo
            file_path: Caminho do arquivo
        
        Returns:
            Conteúdo com referências atualizadas
        """
        # Apenas aplicar para Heróis de Arton
        if self.book_name != 'herois-arton':
            return content
        
        modified = False
        for old_name, new_name in self.RENAMED_FILES.items():
            if old_name in content:
                content = content.replace(old_name, new_name)
                self.stats['file_links_updated'] += 1
                modified = True
        
        return content
    
    def print_summary(self):
        """Imprime resumo das migrações."""
        print("\n" + "=" * 70)
        print("RESUMO DA MIGRAÇÃO")
        print("=" * 70)
        print(f"Arquivos processados: {self.stats['files_processed']}")
        print(f"Arquivos modificados: {self.stats['files_modified']}")
        print(f"Links de imagens atualizados: {self.stats['image_links_updated']}")
        print(f"Links de arquivos atualizados: {self.stats['file_links_updated']}")
        
        if self.stats['errors']:
            print(f"\n⚠️  Erros encontrados: {len(self.stats['errors'])}")
            for error in self.stats['errors']:
                print(f"   - {error}")
        else:
            print("\n✅ Nenhum erro encontrado!")
        
        print("=" * 70 + "\n")


def main():
    """Função principal do script."""
    
    if len(sys.argv) < 2:
        print("❌ ERRO: Caminho do livro não especificado")
        print("\nUso:")
        print("    python scripts/migrate_links.py livros/tormenta20-core/")
        print("    python scripts/migrate_links.py livros/herois-arton/")
        print("\nOpções:")
        print("    --dry-run    Mostra o que seria feito sem modificar arquivos")
        sys.exit(1)
    
    book_path = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    
    # Verificar se caminho existe
    if not os.path.exists(book_path):
        print(f"❌ ERRO: Caminho não encontrado: {book_path}")
        sys.exit(1)
    
    # Executar migração
    migrator = LinkMigrator(book_path)
    stats = migrator.migrate_all(dry_run=dry_run)
    
    # Código de saída baseado em erros
    if stats['errors']:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()

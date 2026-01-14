#!/usr/bin/env python3
"""
Script para corrigir frontmatter do livro deuses-arton.

Padroniza:
- book: "deuses-arton" (slug correto)
- chapter: "NN-directory-name" (nome do diretório)
- Navegação aninhada em navigation:
- Extensões .md consistentes
"""

import os
import re
from pathlib import Path


def fix_frontmatter(file_path: Path) -> bool:
    """Corrige frontmatter de um arquivo."""
    content = file_path.read_text(encoding='utf-8')
    
    # Verificar se tem frontmatter
    if not content.startswith('---\n'):
        return False
    
    # Extrair frontmatter
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        return False
    
    fm_text = match.group(1)
    body = match.group(2)
    
    # Determinar capítulo a partir do caminho
    parts = file_path.parts
    chapter_dir = None
    for i, part in enumerate(parts):
        if part == 'deuses-arton' and i + 1 < len(parts):
            next_part = parts[i + 1]
            if next_part.startswith(('01-', '02-', '03-', '04-', '05-')):
                chapter_dir = next_part
                break
    
    # Parsear campos do frontmatter
    lines = fm_text.split('\n')
    new_fm = []
    nav_lines = []
    in_navigation = False
    in_accessibility = False
    
    for line in lines:
        stripped = line.strip()
        
        # Pular linhas vazias
        if not stripped:
            continue
        
        # Detectar blocos que devemos pular
        if stripped.startswith('accessibility:'):
            in_accessibility = True
            continue
        
        if in_accessibility:
            if line.startswith('  ') or line.startswith('\t'):
                continue
            else:
                in_accessibility = False
        
        # Processar campos principais
        if stripped.startswith('title:'):
            new_fm.append(line)
        
        elif stripped.startswith('book:'):
            # Corrigir book para slug correto
            new_fm.append('book: "deuses-arton"')
        
        elif stripped.startswith('chapter:'):
            # Corrigir chapter para formato de diretório
            if chapter_dir:
                new_fm.append(f'chapter: "{chapter_dir}"')
            else:
                new_fm.append(line)
        
        elif stripped.startswith('navigation:'):
            in_navigation = True
            # Não adiciona ainda, vamos reconstruir
        
        elif in_navigation:
            # Coletar campos de navegação
            if line.startswith('  ') or line.startswith('\t'):
                nav_lines.append(stripped)
            else:
                in_navigation = False
                # Processar campos não-navegação
                if not stripped.startswith(('type:', 'subtype:', 'order:', 'section:', 'page:')):
                    # Pode ser navegação inline antiga (previous:, next:, up:)
                    if stripped.startswith(('previous:', 'next:', 'up:')):
                        nav_lines.append(stripped)
                    else:
                        # Outros campos válidos
                        if stripped.startswith(('section:', 'page:')):
                            new_fm.append(line)
        
        # Campos que devem ser mantidos fora de navigation
        elif stripped.startswith(('section:', 'page:')):
            new_fm.append(line)
        
        # Campos inline de navegação (formato antigo)
        elif stripped.startswith(('previous:', 'next:', 'up:')):
            nav_lines.append(stripped)
        
        # Pular campos extras que não são padrão
        elif stripped.startswith(('type:', 'subtype:', 'order:')):
            continue
    
    # Construir bloco de navegação padronizado
    if nav_lines:
        new_fm.append('navigation:')
        
        prev_val = None
        next_val = None
        up_val = None
        
        for nav_line in nav_lines:
            if nav_line.startswith('previous:'):
                prev_val = nav_line.split(':', 1)[1].strip()
            elif nav_line.startswith('next:'):
                next_val = nav_line.split(':', 1)[1].strip()
            elif nav_line.startswith('up:'):
                up_val = nav_line.split(':', 1)[1].strip()
        
        # Normalizar valores
        def normalize_nav_value(val):
            if not val or val in ('null', 'None'):
                return 'null'
            # Remover aspas se existirem
            val = val.strip('"\'')
            # Adicionar .md se não tiver extensão
            if val != 'null' and not val.endswith('.md') and not val.endswith('/'):
                val = val + '.md'
            # Retornar com aspas
            if val == 'null':
                return 'null'
            return f'"{val}"'
        
        new_fm.append(f'  previous: {normalize_nav_value(prev_val)}')
        new_fm.append(f'  next: {normalize_nav_value(next_val)}')
        new_fm.append(f'  up: {normalize_nav_value(up_val) if up_val else "README.md"}')
    
    # Reconstruir conteúdo
    new_content = '---\n' + '\n'.join(new_fm) + '\n---\n' + body
    
    # Verificar se houve mudança
    if new_content != content:
        file_path.write_text(new_content, encoding='utf-8')
        return True
    
    return False


def main():
    """Executa correção em todos os arquivos de deuses-arton."""
    base_path = Path('livros/deuses-arton')
    
    if not base_path.exists():
        print(f"Erro: Diretório {base_path} não encontrado")
        return
    
    md_files = list(base_path.rglob('*.md'))
    
    print(f"\nCorrigindo frontmatter em: {base_path}")
    print("=" * 70)
    print(f"Arquivos .md encontrados: {len(md_files)}\n")
    
    modified = 0
    skipped = 0
    
    for md_file in md_files:
        try:
            if fix_frontmatter(md_file):
                modified += 1
                rel_path = md_file.relative_to(base_path)
                print(f"✓ Corrigido: {rel_path}")
            else:
                skipped += 1
        except Exception as e:
            print(f"✗ Erro em {md_file}: {e}")
    
    print("\n" + "=" * 70)
    print(f"RESUMO:")
    print(f"  Arquivos modificados: {modified}")
    print(f"  Arquivos sem alteração: {skipped}")
    print(f"  Total processado: {len(md_files)}")
    print("=" * 70)


if __name__ == '__main__':
    main()

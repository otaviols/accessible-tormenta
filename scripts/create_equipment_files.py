#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para criar arquivos de equipamentos do Dragão Brasil (Capítulo 07)
"""

import os

SOURCE_FILE = r"c:\jogos\backup\backup\ddddd\accessible-tormenta\extracted\dragao-brasil\full_text.txt"
OUTPUT_DIR = r"c:\jogos\backup\backup\ddddd\accessible-tormenta\livros\dragao-brasil\06-equipamentos"

# Capítulo 07 - Equipamentos: linhas 8422-10294
EQUIPMENT_SECTIONS = [
    ("01-novas-armas.md", "Novas Armas", "README.md", "02-armaduras-escudos.md", 8422, 8700),
    ("02-armaduras-escudos.md", "Novas Armaduras e Escudos", "01-novas-armas.md", "03-itens-gerais.md", 8700, 8850),
    ("03-itens-gerais.md", "Itens Gerais", "02-armaduras-escudos.md", "04-itens-superiores.md", 8850, 9200),
    ("04-itens-superiores.md", "Itens Superiores", "03-itens-gerais.md", "05-materiais-especiais.md", 9200, 9400),
    ("05-materiais-especiais.md", "Materiais Especiais", "04-itens-superiores.md", "06-itens-magicos.md", 9400, 9700),
    ("06-itens-magicos.md", "Itens Mágicos Específicos", "05-materiais-especiais.md", "07-runas-magicas.md", 9700, 9950),
    ("07-runas-magicas.md", "Runas Mágicas", "06-itens-magicos.md", "08-artefatos.md", 9950, 10150),
    ("08-artefatos.md", "Artefatos", "07-runas-magicas.md", "README.md", 10150, 10294),
]

def create_equipment_file(filename, title, previous, next_file, start_line, end_line):
    """Cria um arquivo de equipamento"""
    
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    content_lines = lines[start_line:end_line]
    content = ''.join(content_lines)
    
    # Limpar marcadores
    content = content.replace('=' * 60, '').replace('PÁGINA ', '\n## Página ')
    
    header = f"""---
title: "{title}"
book: "dragao-brasil"
chapter: "06-equipamentos"
---

# {title}

{title} do livro Dragão Brasil.

---

"""
    
    footer = f"""

---

[← Anterior: {previous.replace('.md', '')}]({previous}) | [Próximo: {next_file.replace('.md', '')} →]({next_file})
"""
    
    full_content = header + content + footer
    
    output_path = os.path.join(OUTPUT_DIR, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"✓ Criado: {filename}")

def main():
    print("\n=== Criando arquivos de equipamentos ===\n")
    
    for section_data in EQUIPMENT_SECTIONS:
        filename, title, previous, next_file, start_line, end_line = section_data
        create_equipment_file(filename, title, previous, next_file, start_line, end_line)
    
    # Atualizar README
    readme_content = """---
title: "Equipamentos"
book: "dragao-brasil"
chapter: "06-equipamentos"
---

# Equipamentos

Novos equipamentos, armas, armaduras, itens mágicos e artefatos.

---

## 📑 Conteúdo do Capítulo

1. **[Novas Armas](01-novas-armas.md)** - Armas exóticas e marciais
2. **[Armaduras e Escudos](02-armaduras-escudos.md)** - Novas proteções
3. **[Itens Gerais](03-itens-gerais.md)** - Equipamentos diversos
4. **[Itens Superiores](04-itens-superiores.md)** - Equipamentos de qualidade excepcional
5. **[Materiais Especiais](05-materiais-especiais.md)** - Materiais raros e exóticos
6. **[Itens Mágicos](06-itens-magicos.md)** - Itens mágicos específicos
7. **[Runas Mágicas](07-runas-magicas.md)** - Sistema de runas
8. **[Artefatos](08-artefatos.md)** - Artefatos únicos e lendários

---

## 🔗 Navegação

- **Anterior:** [05 - Distinções](../05-distincoes/README.md)
- **Próximo:** [07 - Magias](../07-magias/README.md)
- **Índice:** [← Voltar ao Índice do Livro](../README.md)
"""
    
    readme_path = os.path.join(OUTPUT_DIR, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✓ Atualizado: README.md")
    print(f"\n=== Concluído! ===")
    print(f"{len(EQUIPMENT_SECTIONS) + 1} arquivos criados em: {OUTPUT_DIR}\n")

if __name__ == "__main__":
    main()

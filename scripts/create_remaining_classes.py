#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para extrair e criar arquivos de classes do Dragão Brasil
"""

import os
import sys

# Configurações
SOURCE_FILE = r"c:\jogos\backup\backup\ddddd\accessible-tormenta\extracted\dragao-brasil\full_text.txt"
OUTPUT_DIR = r"c:\jogos\backup\backup\ddddd\accessible-tormenta\livros\dragao-brasil\02-classes"

# Definição das classes e suas faixas de linhas (0-indexed)
CLASSES = [
    ("05-cacador.md", "Caçador", "04-bucaneiro.md", "06-cavaleiro.md", 1725, 1863),
    ("06-cavaleiro.md", "Cavaleiro", "05-cacador.md", "07-druida.md", 1792, 1863),
    ("07-druida.md", "Druida", "06-cavaleiro.md", "08-guerreiro.md", 1862, 2194),
    ("08-guerreiro.md", "Guerreiro", "07-druida.md", "09-inventor.md", 2193, 2275),
    ("09-inventor.md", "Inventor", "08-guerreiro.md", "10-ladino.md", 2193, 2350),
    ("10-ladino.md", "Ladino", "09-inventor.md", "11-lutador.md", 2274, 2423),
    ("11-lutador.md", "Lutador", "10-ladino.md", "12-miragem.md", 2349, 2502),
    ("12-miragem.md", "Miragem", "11-lutador.md", "13-mistico.md", 2422, 2580),
    ("13-mistico.md", "Místico", "12-miragem.md", "14-nobre.md", 2579, 3063),
    ("14-nobre.md", "Nobre", "13-mistico.md", "15-samurai.md", 2998, 3063),
    ("15-samurai.md", "Samurai", "14-nobre.md", "README.md", 3062, 3514),
]

def create_class_file(filename, title, previous, next_file, start_line, end_line):
    """Cria um arquivo de classe com conteúdo extraído"""
    
    # Ler o arquivo fonte
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Extrair conteúdo (linhas são 0-indexed)
    content_lines = lines[start_line:end_line]
    content = ''.join(content_lines)
    
    # Remover marcadores de página se necessário
    content = content.replace('=' * 60, '').replace('PÁGINA ', '\n## Página ')
    
    # Criar o arquivo
    header = f"""---
title: "{title} - Poderes de Classe"
book: "dragao-brasil"
chapter: "02-classes"
---

# {title}

Novos poderes e conteúdo para a classe {title}.

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
    """Função principal"""
    print("\n=== Criando arquivos de classes ===\n")
    
    for class_data in CLASSES:
        filename, title, previous, next_file, start_line, end_line = class_data
        create_class_file(filename, title, previous, next_file, start_line, end_line)
    
    print(f"\n=== Concluído! ===")
    print(f"{len(CLASSES)} arquivos criados em: {OUTPUT_DIR}\n")

if __name__ == "__main__":
    main()

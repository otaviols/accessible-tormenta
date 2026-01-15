#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criar arquivos para os capítulos restantes do Dragão Brasil
"""

import os

SOURCE_FILE = r"c:\jogos\backup\backup\ddddd\accessible-tormenta\extracted\dragao-brasil\full_text.txt"
BASE_DIR = r"c:\jogos\backup\backup\ddddd\accessible-tormenta\livros\dragao-brasil"

def create_file(filepath, content):
    """Cria um arquivo com o conteúdo especificado"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Criado: {os.path.basename(filepath)}")

def extract_content(start_line, end_line):
    """Extrai conteúdo do arquivo fonte"""
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    content = ''.join(lines[start_line:end_line])
    return content.replace('=' * 60, '').replace('PÁGINA ', '\n## Página ')

# ============================================================
# CAPÍTULO 04 - DEUSES E REMANESCÊNCIA (Linhas 4255-4462)
# ============================================================
print("\n=== Capítulo 04 - Deuses e Remanescência ===\n")

content_04 = extract_content(4255, 4462)

create_file(os.path.join(BASE_DIR, "04-pericias-poderes", "00-deuses-remanescencia.md"), f"""---
title: "Deuses e Remanescência"
book: "dragao-brasil"
chapter: "04-pericias-poderes"
---

# Deuses e Remanescência

Novos poderes concedidos por deuses e o sistema de Remanescência para personagens sem devoção.

---

{content_04}

---

[← Anterior: Origens](../03-origens/README.md) | [Próximo: Perícias e Poderes →](README.md)
""")

#  ============================================================
# CAPÍTULO 03 - COMPLETAR ORIGENS REGIONAIS (Linhas 3514-4242)
# ============================================================
print("\n=== Capítulo 03 - Completar Origens Regionais ===\n")

# Ler o arquivo atual
origens_path = os.path.join(BASE_DIR, "03-origens", "02-origens-regionais.md")
with open(origens_path, 'r', encoding='utf-8') as f:
    current_content = f.read()

# Extrair conteúdo faltante
remaining_content = extract_content(3900, 4242)

# Localizar onde inserir (antes do rodapé de navegação)
nav_marker = "\n---\n\n[← Anterior:"
if nav_marker in current_content:
    parts = current_content.split(nav_marker)
    updated_content = parts[0] + "\n\n" + remaining_content + nav_marker + parts[1]
else:
    updated_content = current_content + "\n\n" + remaining_content

with open(origens_path, 'w', encoding='utf-8') as f:
    f.write(updated_content)
print(f"✓ Atualizado: 02-origens-regionais.md (adicionadas ~20-30 origens)")

# ============================================================
# CAPÍTULO 06 - COMPLETAR PERÍCIAS E PODERES (Linhas 7483-8337)
# ============================================================
print("\n=== Capítulo 06 - Perícias e Poderes ===\n")

poderes_sections = [
    ("03-poderes-combate.md", "Poderes de Combate", "02-poderes-gerais.md", "04-poderes-destino.md", 7621, 7836),
    ("04-poderes-destino.md", "Poderes de Destino", "03-poderes-combate.md", "05-poderes-magia.md", 7836, 8045),
    ("05-poderes-magia.md", "Poderes de Magia", "04-poderes-destino.md", "06-poderes-concedidos.md", 8045, 8191),
    ("06-poderes-concedidos.md", "Poderes Concedidos", "05-poderes-magia.md", "07-escola-combate.md", 8191, 8260),
    ("07-escola-combate.md", "Escola de Combate", "06-poderes-concedidos.md", "README.md", 8260, 8337),
]

for filename, title, prev, next_file, start, end in poderes_sections:
    content = extract_content(start, end)
    filepath = os.path.join(BASE_DIR, "04-pericias-poderes", filename)
    create_file(filepath, f"""---
title: "{title}"
book: "dragao-brasil"
chapter: "04-pericias-poderes"
---

# {title}

{title} do livro Dragão Brasil.

---

{content}

---

[← Anterior: {prev.replace('.md', '')}]({prev}) | [Próximo: {next_file.replace('.md', '')} →]({next_file})
""")

# ============================================================
# CAPÍTULO 09 - COMPLETAR REGRAS (Linhas 10916-13158)
# ============================================================
print("\n=== Capítulo 09 - Regras ===\n")

regras_sections = [
    ("05-toques-finais.md", "Toques Finais e Perfis", "04-desvantagens.md", "06-overdose-mana.md", 10916, 11100),
    ("06-overdose-mana.md", "Overdose de Mana", "05-toques-finais.md", "07-persona-non-grata.md", 11100, 11250),
    ("07-persona-non-grata.md", "Persona Non Grata", "06-overdose-mana.md", "08-questao-carater.md", 11250, 11400),
    ("08-questao-carater.md", "Questão de Caráter", "07-persona-non-grata.md", "09-alimentacao.md", 11400, 11650),
    ("09-alimentacao.md", "Regra de Alimentação", "08-questao-carater.md", "10-invocacoes.md", 11650, 11770),
    ("10-invocacoes.md", "Invocações (Final Fantasy)", "09-alimentacao.md", "11-chocobos.md", 11770, 12100),
    ("11-chocobos.md", "Chocobos", "10-invocacoes.md", "12-sumo-sacerdotes.md", 12100, 12700),
    ("12-sumo-sacerdotes.md", "Sumo-Sacerdotes", "11-chocobos.md", "13-descanso.md", 12700, 12900),
    ("13-descanso.md", "Tipos de Descanso", "12-sumo-sacerdotes.md", "14-regra-grupos.md", 12900, 13050),
    ("14-regra-grupos.md", "Regra de Grupos", "13-descanso.md", "README.md", 13050, 13158),
]

for filename, title, prev, next_file, start, end in regras_sections:
    content = extract_content(start, end)
    filepath = os.path.join(BASE_DIR, "08-regras", filename)
    create_file(filepath, f"""---
title: "{title}"
book: "dragao-brasil"
chapter: "08-regras"
---

# {title}

{title} do livro Dragão Brasil.

---

{content}

---

[← Anterior: {prev.replace('.md', '')}]({prev}) | [Próximo: {next_file.replace('.md', '')} →]({next_file})
""")

print("\n=== TODOS OS CAPÍTULOS CRIADOS! ===\n")

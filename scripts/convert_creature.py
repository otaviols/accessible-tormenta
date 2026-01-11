#!/usr/bin/env python3
"""
Script para converter criaturas de Ameaças de Arton do formato extraído para markdown.
"""

import re
import sys
from pathlib import Path

def extract_creature_block(full_text, start_pattern, end_pattern=None):
    """Extrai bloco de criatura do texto completo."""
    lines = full_text.split('\n')
    start_idx = None
    
    for i, line in enumerate(lines):
        if start_pattern in line:
            start_idx = i
            break
    
    if start_idx is None:
        return None
    
    # Se não especificado, pega até próxima criatura ou fim de seção
    end_idx = len(lines)
    if end_pattern:
        for i in range(start_idx + 1, len(lines)):
            if end_pattern in lines[i]:
                end_idx = i
                break
    else:
        # Procura por próximo cabeçalho de criatura ou separador
        for i in range(start_idx + 50, min(start_idx + 300, len(lines))):
            if lines[i].strip().startswith('ND ') or '======' in lines[i]:
                end_idx = i
                break
    
    return '\n'.join(lines[start_idx:end_idx])

def parse_stat_block(text):
    """Converte bloco de estatísticas em dicionário estruturado."""
    stats = {
        'name': '',
        'nd': '',
        'type': '',
        'size': '',
        'init': '',
        'perception': '',
        'senses': [],
        'defense': '',
        'fort': '',
        'ref': '',
        'will': '',
        'special_defenses': [],
        'hp': '',
        'movement': {},
        'attacks_melee': [],
        'attacks_ranged': [],
        'abilities': [],
        'attributes': {},
        'skills': '',
        'equipment': '',
        'treasure': '',
        'partner': ''
    }
    
    lines = text.split('\n')
    
    # Extrai nome e ND
    for i, line in enumerate(lines):
        if line.strip() and not line.startswith('"'):
            stats['name'] = line.strip()
        if 'ND ' in line:
            match = re.search(r'ND (\d+/?[\d]*)', line)
            if match:
                stats['nd'] = match.group(1)
        if re.match(r'^(Animal|Humanoide|Monstro|Construto|Espírito|Morto-vivo)', line):
            parts = line.split()
            if len(parts) >= 2:
                stats['type'] = parts[0]
                stats['size'] = parts[1] if len(parts) > 1 else ''
            break
    
    # Extrai estatísticas linha por linha
    for line in lines:
        line = line.strip()
        
        # Iniciativa e Percepção
        if line.startswith('Iniciativa'):
            match = re.search(r'Iniciativa ([+\-\d]+)', line)
            if match:
                stats['init'] = match.group(1)
            match = re.search(r'Percepção ([+\-\d]+)', line)
            if match:
                stats['perception'] = match.group(1)
            # Sentidos especiais
            if ',' in line:
                parts = line.split(',')[1:]
                stats['senses'] = [p.strip() for p in parts if p.strip()]
        
        # Defesas
        if line.startswith('Defesa '):
            match = re.search(r'Defesa (\d+)', line)
            if match:
                stats['defense'] = match.group(1)
            match = re.search(r'Fort ([+\-\d]+)', line)
            if match:
                stats['fort'] = match.group(1)
            match = re.search(r'Ref ([+\-\d]+)', line)
            if match:
                stats['ref'] = match.group(1)
            match = re.search(r'Von ([+\-\d]+)', line)
            if match:
                stats['will'] = match.group(1)
        
        # PV
        if line.startswith('Pontos de Vida'):
            match = re.search(r'(\d+)', line)
            if match:
                stats['hp'] = match.group(1)
        
        # Deslocamento
        if line.startswith('Deslocamento'):
            if 'natação' in line:
                match = re.search(r'natação (\d+m)', line)
                if match:
                    stats['movement']['natação'] = match.group(1)
            if 'voo' in line:
                match = re.search(r'voo (\d+m)', line)
                if match:
                    stats['movement']['voo'] = match.group(1)
            match = re.search(r'(\d+m)', line)
            if match:
                stats['movement']['caminhando'] = match.group(1)
        
        # Ataques
        if line.startswith('Corpo a Corpo'):
            stats['attacks_melee'].append(line.replace('Corpo a Corpo ', ''))
        if line.startswith('À Distância'):
            stats['attacks_ranged'].append(line.replace('À Distância ', ''))
        
        # Atributos
        if line.startswith('For '):
            attrs = line.split(',')
            for attr in attrs:
                attr = attr.strip()
                if attr.startswith('For '):
                    stats['attributes']['For'] = attr.replace('For ', '')
                elif attr.startswith('Des '):
                    stats['attributes']['Des'] = attr.replace('Des ', '')
                elif attr.startswith('Con '):
                    stats['attributes']['Con'] = attr.replace('Con ', '')
                elif attr.startswith('Int '):
                    stats['attributes']['Int'] = attr.replace('Int ', '')
                elif attr.startswith('Sab '):
                    stats['attributes']['Sab'] = attr.replace('Sab ', '')
                elif attr.startswith('Car '):
                    stats['attributes']['Car'] = attr.replace('Car ', '')
    
    return stats

def generate_markdown(stats, creature_num, total_creatures, section="Montarias"):
    """Gera arquivo markdown a partir das estatísticas."""
    
    # Determina navegação
    prev_file = f"{creature_num-1:02d}-*.md" if creature_num > 1 else "README.md"
    next_file = f"{creature_num+1:02d}-*.md" if creature_num < total_creatures else "README.md"
    
    md = f"""---
title: "{stats['name']}"
book: "Ameaças de Arton"
chapter: "Capítulo 1: Ameaças"
section: "{section}"
navigation:
  previous: "{prev_file}"
  next: "{next_file}"
  up: "README.md"
---

# {stats['name']}

![Ilustração de {stats['name']}](../../_imagens/ameacas-arton/{stats['name'].lower().replace(' ', '-')}.jpg)
*Descrição: [DESCRIÇÃO DA IMAGEM PENDENTE]*

> "[CITAÇÃO PENDENTE]"
>
> — [AUTOR PENDENTE]

[DESCRIÇÃO NARRATIVA PENDENTE]

## Estatísticas

**{stats['name']}**  
**ND {stats['nd']}**

**{stats['type']} {stats['size']}**

| Atributo | Valor |
|----------|-------|
| **Iniciativa** | {stats['init']} |
| **Percepção** | {stats['perception']} |
"""
    
    if stats['senses']:
        md += f"| **Especiais** | {', '.join(stats['senses'])} |\n"
    
    md += f"""
| Defesa | Valor |
|--------|-------|
| **Defesa** | {stats['defense']} |
| **Fortitude** | {stats['fort']} |
| **Reflexos** | {stats['ref']} |
| **Vontade** | {stats['will']} |
"""
    
    md += f"""
| Pontos de Vida | Valor |
|----------------|-------|
| **PV** | {stats['hp']} |

| Deslocamento | Valor |
|--------------|-------|
"""
    
    for move_type, value in stats['movement'].items():
        md += f"| **{move_type.capitalize()}** | {value} |\n"
    
    if stats['attacks_melee'] or stats['attacks_ranged']:
        md += "\n### Ataques\n\n"
        if stats['attacks_melee']:
            md += "**Corpo a Corpo**\n"
            for attack in stats['attacks_melee']:
                md += f"- {attack}\n"
            md += "\n"
        if stats['attacks_ranged']:
            md += "**À Distância**\n"
            for attack in stats['attacks_ranged']:
                md += f"- {attack}\n"
            md += "\n"
    
    md += """
### Atributos

| For | Des | Con | Int | Sab | Car |
|-----|-----|-----|-----|-----|-----|
"""
    md += f"| {stats['attributes'].get('For', '0')} | {stats['attributes'].get('Des', '0')} | "
    md += f"{stats['attributes'].get('Con', '0')} | {stats['attributes'].get('Int', '0')} | "
    md += f"{stats['attributes'].get('Sab', '0')} | {stats['attributes'].get('Car', '0')} |\n\n"
    
    md += """**Tesouro:** [PENDENTE].

---

**Navegação:**
- [← Anterior](README.md)
- [→ Próximo](README.md)
- [↑ {section}](README.md)
"""
    
    return md

if __name__ == "__main__":
    print("Script de conversão de criaturas - Ameaças de Arton")
    print("=" * 60)
    print("\nEste script é um template. Use as funções para converter criaturas.")
    print("\nExemplo de uso:")
    print("  python convert_creature.py <arquivo_full_text> <nome_criatura>")

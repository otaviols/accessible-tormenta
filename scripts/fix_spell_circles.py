"""
Script para corrigir círculos das magias no Tormenta20-Core.
Remove duplicatas e move magias para os círculos corretos.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict

# Mapeamento de arquivos para círculos
CIRCLE_FILES = {
    1: "livros/tormenta20-core/09-magia/03-descricao-magias-1-circulo.md",
    2: "livros/tormenta20-core/09-magia/04-descricao-magias-2-circulo.md",
    3: "livros/tormenta20-core/09-magia/06-descricao-magias-3-circulo.md",
    4: "livros/tormenta20-core/09-magia/08-descricao-magias-4-circulo.md",
    5: "livros/tormenta20-core/09-magia/10-descricao-magias-5-circulo.md",
}

def extract_spell_content(content: str, spell_name: str) -> str:
    """Extrai o conteúdo completo de uma magia do arquivo."""
    # Padrão para encontrar a magia e todo seu conteúdo até a próxima magia
    pattern = rf'^## {re.escape(spell_name)}$\n\n(.*?)(?=^## |\Z)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    
    if match:
        # Retornar o header e todo o conteúdo
        return f"## {spell_name}\n\n{match.group(1).rstrip()}"
    return None

def get_frontmatter(content: str) -> str:
    """Extrai o frontmatter YAML do arquivo."""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        return f"---\n{match.group(1)}\n---\n"
    return ""

def get_header_before_spells(content: str) -> str:
    """Extrai todo o conteúdo antes da primeira magia."""
    # Encontrar a primeira magia (## seguido de maiúscula)
    match = re.search(r'^## [A-ZÀ-Ú]', content, re.MULTILINE)
    if match:
        return content[:match.start()].rstrip() + "\n\n"
    return content

def parse_spell_from_content(spell_content: str) -> Dict:
    """Parse uma magia do seu conteúdo completo."""
    lines = spell_content.split('\n', 3)
    if len(lines) < 3:
        return None
    
    spell_name = lines[0].replace('## ', '').strip()
    type_line = lines[2].strip()
    
    # Extrair círculo da linha de tipo
    circle_match = re.search(r'\b(\d)\b', type_line)
    declared_circle = int(circle_match.group(1)) if circle_match else None
    
    return {
        'name': spell_name,
        'type_line': type_line,
        'declared_circle': declared_circle,
        'content': spell_content
    }

def main():
    base_path = Path(__file__).parent.parent
    
    # Carregar relatório de auditoria
    report_path = base_path / "spell_audit_report.json"
    if not report_path.exists():
        print("❌ Relatório de auditoria não encontrado. Execute audit_spell_circles.py primeiro.")
        return
    
    report = json.loads(report_path.read_text(encoding='utf-8'))
    
    print("=" * 80)
    print("CORREÇÃO DE CÍRCULOS DAS MAGIAS - TORMENTA20-CORE")
    print("=" * 80)
    print()
    
    # Organizar magias por círculo correto
    spells_by_correct_circle = defaultdict(list)
    
    # Processar cada arquivo
    for circle in range(1, 6):
        file_path = base_path / CIRCLE_FILES[circle]
        content = file_path.read_text(encoding='utf-8')
        
        print(f"📖 Processando Círculo {circle}...")
        
        # Extrair todas as magias do arquivo
        spell_pattern = r'^## (.+?)$\n\n^(.+?)$\n\n(.*?)(?=^## |\Z)'
        matches = list(re.finditer(spell_pattern, content, re.MULTILINE | re.DOTALL))
        
        for match in matches:
            spell_name = match.group(1).strip()
            type_line = match.group(2).strip()
            spell_body = match.group(3).rstrip()
            
            # Extrair círculo declarado
            circle_match = re.search(r'\b(\d)\b', type_line)
            declared_circle = int(circle_match.group(1)) if circle_match else circle
            
            # Construir conteúdo completo da magia
            spell_content = f"## {spell_name}\n\n{type_line}\n\n{spell_body}"
            
            # Adicionar à lista do círculo correto
            spells_by_correct_circle[declared_circle].append({
                'name': spell_name,
                'type_line': type_line,
                'declared_circle': declared_circle,
                'content': spell_content,
                'current_circle': circle
            })
        
        print(f"   ✓ {len(matches)} magias extraídas")
    
    print()
    print("=" * 80)
    print("REORGANIZANDO MAGIAS")
    print("=" * 80)
    print()
    
    # Remover duplicatas - manter apenas uma versão de cada magia
    for circle, spells in spells_by_correct_circle.items():
        unique_spells = {}
        for spell in spells:
            if spell['name'] not in unique_spells:
                unique_spells[spell['name']] = spell
            else:
                print(f"⚠️  Duplicata removida: {spell['name']} (estava no círculo {spell['current_circle']})")
        
        spells_by_correct_circle[circle] = list(unique_spells.values())
    
    print()
    print("=" * 80)
    print("RECONSTRUINDO ARQUIVOS")
    print("=" * 80)
    print()
    
    # Reescrever cada arquivo com as magias corretas em ordem alfabética
    for circle in range(1, 6):
        file_path = base_path / CIRCLE_FILES[circle]
        original_content = file_path.read_text(encoding='utf-8')
        
        # Preservar frontmatter e header
        frontmatter = get_frontmatter(original_content)
        header = get_header_before_spells(original_content)
        
        # Remover frontmatter do header se já foi extraído
        if frontmatter:
            header = header.replace(frontmatter, '').lstrip()
        
        # Ordenar magias alfabeticamente
        spells = sorted(spells_by_correct_circle[circle], key=lambda x: x['name'])
        
        # Construir novo conteúdo
        new_content = frontmatter
        if header and header.strip():
            new_content += header
        
        # Adicionar magias
        for i, spell in enumerate(spells):
            new_content += spell['content']
            if i < len(spells) - 1:
                new_content += "\n\n"
        
        # Adicionar quebra de linha final
        new_content += "\n"
        
        # Escrever arquivo
        file_path.write_text(new_content, encoding='utf-8')
        
        print(f"✓ Círculo {circle}: {len(spells)} magias organizadas")
    
    print()
    print("=" * 80)
    print("ESTATÍSTICAS FINAIS")
    print("=" * 80)
    print()
    
    for circle in range(1, 6):
        count = len(spells_by_correct_circle[circle])
        print(f"Círculo {circle}: {count} magias")
    
    total = sum(len(spells) for spells in spells_by_correct_circle.values())
    print(f"\nTotal: {total} magias únicas")
    print()
    print("✅ Correção concluída com sucesso!")

if __name__ == "__main__":
    main()

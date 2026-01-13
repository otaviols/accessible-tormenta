"""
Script para auditar e corrigir círculos das magias no Tormenta20-Core.
Identifica magias colocadas em círculos incorretos e gera relatório detalhado.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

# Mapeamento de arquivos para círculos
CIRCLE_FILES = {
    1: "livros/tormenta20-core/09-magia/03-descricao-magias-1-circulo.md",
    2: "livros/tormenta20-core/09-magia/04-descricao-magias-2-circulo.md",
    3: "livros/tormenta20-core/09-magia/06-descricao-magias-3-circulo.md",
    4: "livros/tormenta20-core/09-magia/08-descricao-magias-4-circulo.md",
    5: "livros/tormenta20-core/09-magia/10-descricao-magias-5-circulo.md",
}

def extract_spells_from_file(file_path: Path, expected_circle: int) -> List[Dict]:
    """Extrai todas as magias de um arquivo, identificando seu círculo declarado."""
    if not file_path.exists():
        print(f"❌ Arquivo não encontrado: {file_path}")
        return []
    
    content = file_path.read_text(encoding='utf-8')
    spells = []
    
    # Padrão para encontrar magias: ## Nome seguido da linha de tipo
    pattern = r'^## (.+?)$\n\n^(.+?)$'
    matches = re.finditer(pattern, content, re.MULTILINE)
    
    for match in matches:
        spell_name = match.group(1).strip()
        type_line = match.group(2).strip()
        
        # Extrair círculo da linha de tipo (ex: "Divina 2", "Arcana 3")
        circle_match = re.search(r'\b(\d)\b', type_line)
        declared_circle = int(circle_match.group(1)) if circle_match else None
        
        # Extrair tradição e escola
        tradition_school_match = re.match(r'^(\w+)\s+(\d+)\s*(?:\((.+?)\))?', type_line)
        tradition = tradition_school_match.group(1) if tradition_school_match else "Unknown"
        school = tradition_school_match.group(3) if tradition_school_match and tradition_school_match.group(3) else ""
        
        spells.append({
            'name': spell_name,
            'type_line': type_line,
            'declared_circle': declared_circle,
            'file_circle': expected_circle,
            'tradition': tradition,
            'school': school,
            'is_misplaced': declared_circle != expected_circle if declared_circle else False
        })
    
    return spells

def find_duplicates(all_spells: List[Dict]) -> Dict[str, List[Dict]]:
    """Encontra magias que aparecem em múltiplos arquivos."""
    spell_dict = {}
    
    for spell in all_spells:
        name = spell['name']
        if name not in spell_dict:
            spell_dict[name] = []
        spell_dict[name].append(spell)
    
    # Retornar apenas duplicatas
    return {name: occurrences for name, occurrences in spell_dict.items() if len(occurrences) > 1}

def main():
    base_path = Path(__file__).parent.parent
    
    print("=" * 80)
    print("AUDITORIA DE CÍRCULOS DAS MAGIAS - TORMENTA20-CORE")
    print("=" * 80)
    print()
    
    all_spells = []
    
    # Extrair magias de cada arquivo
    for circle, file_rel_path in CIRCLE_FILES.items():
        file_path = base_path / file_rel_path
        print(f"📖 Analisando Círculo {circle}: {file_rel_path}")
        spells = extract_spells_from_file(file_path, circle)
        all_spells.extend(spells)
        print(f"   ✓ {len(spells)} magias encontradas")
        print()
    
    # Encontrar duplicatas
    print("=" * 80)
    print("DUPLICATAS ENCONTRADAS")
    print("=" * 80)
    print()
    
    duplicates = find_duplicates(all_spells)
    
    if duplicates:
        for spell_name, occurrences in sorted(duplicates.items()):
            print(f"🔄 {spell_name}")
            for occ in occurrences:
                marker = "✓ CORRETO" if occ['declared_circle'] == occ['file_circle'] else "❌ INCORRETO"
                print(f"   - Círculo {occ['file_circle']} (declarado como {occ['type_line']}) {marker}")
            print()
    else:
        print("✓ Nenhuma duplicata encontrada")
        print()
    
    # Magias mal colocadas (mas não duplicadas)
    print("=" * 80)
    print("MAGIAS EM CÍRCULO ERRADO (NÃO DUPLICADAS)")
    print("=" * 80)
    print()
    
    misplaced_unique = []
    for spell in all_spells:
        if spell['is_misplaced'] and spell['name'] not in duplicates:
            misplaced_unique.append(spell)
    
    if misplaced_unique:
        for spell in sorted(misplaced_unique, key=lambda x: x['name']):
            print(f"❌ {spell['name']}")
            print(f"   Está em: Círculo {spell['file_circle']}")
            print(f"   Deveria estar em: Círculo {spell['declared_circle']} ({spell['type_line']})")
            print()
    else:
        print("✓ Todas as magias não-duplicadas estão no círculo correto")
        print()
    
    # Estatísticas finais
    print("=" * 80)
    print("ESTATÍSTICAS")
    print("=" * 80)
    print()
    print(f"Total de entradas de magias: {len(all_spells)}")
    print(f"Magias únicas: {len(set(s['name'] for s in all_spells))}")
    print(f"Duplicatas: {len(duplicates)}")
    print(f"Magias mal colocadas (total): {sum(1 for s in all_spells if s['is_misplaced'])}")
    print()
    
    # Gerar relatório JSON para processamento posterior
    report_path = base_path / "spell_audit_report.json"
    report = {
        'all_spells': all_spells,
        'duplicates': {name: [{'name': s['name'], 'type_line': s['type_line'], 
                               'declared_circle': s['declared_circle'], 
                               'file_circle': s['file_circle']} 
                              for s in occurrences] 
                       for name, occurrences in duplicates.items()},
        'misplaced_unique': [{'name': s['name'], 'type_line': s['type_line'],
                             'declared_circle': s['declared_circle'],
                             'file_circle': s['file_circle']}
                            for s in misplaced_unique]
    }
    
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"📄 Relatório JSON salvo em: {report_path}")
    print()

if __name__ == "__main__":
    main()

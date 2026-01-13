"""
Script para verificar ordem alfabética das magias.
"""

import re
from pathlib import Path

# Mapeamento de arquivos para círculos
CIRCLE_FILES = {
    1: "livros/tormenta20-core/09-magia/03-descricao-magias-1-circulo.md",
    2: "livros/tormenta20-core/09-magia/04-descricao-magias-2-circulo.md",
    3: "livros/tormenta20-core/09-magia/06-descricao-magias-3-circulo.md",
    4: "livros/tormenta20-core/09-magia/08-descricao-magias-4-circulo.md",
    5: "livros/tormenta20-core/09-magia/10-descricao-magias-5-circulo.md",
}

def extract_spell_names(content: str):
    """Extrai nomes de todas as magias."""
    pattern = r'^## (.+?)$'
    matches = re.findall(pattern, content, re.MULTILINE)
    return matches

def main():
    base_path = Path(__file__).parent.parent
    
    print("=" * 80)
    print("VERIFICAÇÃO DE ORDEM ALFABÉTICA")
    print("=" * 80)
    print()
    
    all_ok = True
    
    for circle in range(1, 6):
        file_path = base_path / CIRCLE_FILES[circle]
        content = file_path.read_text(encoding='utf-8')
        
        spell_names = extract_spell_names(content)
        sorted_names = sorted(spell_names)
        
        print(f"📖 Círculo {circle}: {len(spell_names)} magias")
        
        # Verificar se está ordenado
        if spell_names == sorted_names:
            print(f"   ✓ Ordem alfabética correta")
        else:
            print(f"   ❌ Ordem incorreta!")
            all_ok = False
            
            # Mostrar diferenças
            for i, (current, expected) in enumerate(zip(spell_names, sorted_names)):
                if current != expected:
                    print(f"      Posição {i+1}: '{current}' deveria ser '{expected}'")
        
        print()
    
    if all_ok:
        print("✅ Todos os arquivos estão em ordem alfabética correta!")
    else:
        print("⚠️ Alguns arquivos precisam de reordenação.")

if __name__ == "__main__":
    main()

import json
import sys

# Fix encoding for Windows console
sys.stdout.reconfigure(encoding='utf-8')

# Carregar o conteúdo extraído
with open('extracted/herois-arton-cap4/extracted_content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Páginas chave baseadas no sumário
pages_to_check = [278, 279, 280, 281, 282, 283, 288, 292, 294, 296, 305, 310, 314, 328]

print("=" * 80)
print("ANÁLISE DETALHADA DAS PÁGINAS DO CAPÍTULO 4")
print("=" * 80)

for page_num in pages_to_check:
    page_data = data['pages'][page_num - 1]
    text = page_data['text']
    
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    print(f"\n{'='*80}")
    print(f"PÁGINA {page_num}")
    print('='*80)
    
    # Mostrar as primeiras 25 linhas não-vazias
    for i, line in enumerate(lines[:25]):
        print(f"{i+1:2d}. {line[:75]}")

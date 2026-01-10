import json
import re

# Carregar o conteúdo extraído
with open('extracted/herois-arton-cap4/extracted_content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Páginas do Capítulo 4 (278-332)
cap4_pages = data['pages'][277:332]

print("=" * 80)
print("CAPÍTULO 4: REGRAS OPCIONAIS - Páginas 278-332")
print("=" * 80)
print()

# Vamos extrair as primeiras linhas de cada página para identificar títulos
for i, page in enumerate(cap4_pages):
    page_num = page['number']
    text = page['text']
    
    # Mostrar apenas páginas chave (baseado no sumário fornecido)
    key_pages = [278, 280, 281, 282, 288, 292, 294, 296, 305, 310, 314, 328]
    
    if page_num in key_pages:
        print(f"\n{'='*80}")
        print(f"PÁGINA {page_num}")
        print('='*80)
        
        # Pegar as primeiras linhas (até 500 caracteres)
        lines = text.split('\n')
        preview = []
        char_count = 0
        
        for line in lines:
            line = line.strip()
            if line and not line.isdigit():  # Ignorar números de página
                preview.append(line)
                char_count += len(line)
                if char_count > 800 or len(preview) > 20:
                    break
        
        print('\n'.join(preview[:15]))

print("\n" + "=" * 80)
print("Análise completa das páginas-chave do Capítulo 4")
print("=" * 80)

import json
import re

# Carregar o conteúdo extraído
with open('extracted/herois-arton-cap4/extracted_content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Páginas do Capítulo 4 (278-332)
# Lembrando que o índice é 0-based, então página 278 = índice 277
cap4_pages = data['pages'][277:332]

print("=" * 70)
print("CAPÍTULO 4: REGRAS OPCIONAIS")
print("Páginas 278-332")
print("=" * 70)
print()

# Padrões para identificar títulos de seção
# Títulos geralmente estão em letras maiúsculas ou têm formatação especial
section_titles = []

for page in cap4_pages:
    page_num = page['number']
    text = page['text']
    
    # Procurar por títulos (geralmente linhas curtas em maiúsculas ou com formatação específica)
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Verificar se é um título de seção
        # Critérios: linha curta, muitas maiúsculas, não começa com número
        if line and len(line) < 100:
            # Títulos típicos
            if (line.isupper() and len(line) > 5) or \
               (re.match(r'^[A-ZÁÉÍÓÚÂÊÔÃÕÇ\s]+$', line) and len(line) > 10) or \
               (line.startswith('Capítulo')) or \
               (re.match(r'^[A-Z][a-záéíóúâêôãõç\s]+$', line) and len(line) > 15 and len(line) < 60):
                
                # Evitar linhas genéricas
                if line not in ['TORMENTA', 'ARTON', 'CAPÍTULO', 'PÁGINA'] and \
                   not line.startswith('Página') and \
                   not line.startswith('278') and \
                   not re.match(r'^\d+$', line):
                    section_titles.append((page_num, line))

# Imprimir seções encontradas
print("Seções identificadas:")
print()

last_page = 0
for page_num, title in section_titles:
    if page_num != last_page:  # Evitar duplicatas da mesma página
        print(f"Página {page_num}: {title}")
        last_page = page_num

print()
print("=" * 70)
print(f"Total de seções identificadas: {len(set([t[1] for t in section_titles]))}")

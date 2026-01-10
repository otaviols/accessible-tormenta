import json
import re

# Carregar o conteúdo extraído
with open('extracted/herois-arton-cap4/extracted_content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=" * 80)
print("CAPÍTULO 4: REGRAS OPCIONAIS")
print("Seções Identificadas do PDF (Páginas 278-332)")
print("=" * 80)
print()

# Mapear páginas específicas com base no sumário fornecido
sections_map = {
    280: "Atributos Variados",
    281: "Raças Abertas / Devoções Abertas",
    282: "Complicações",
    288: "Idades Variadas",
    292: "Objetivos Heroicos",
    294: "Papéis no Grupo",
    296: "Combate Avançado",
    305: "Culinária Avançada",
    310: "Exploração de Masmorras",
    314: "Domínios",
    328: "Lista de Regras Opcionais"
}

# Extrair texto das páginas específicas
results = []

for page_num in sorted(sections_map.keys()):
    page_data = data['pages'][page_num - 1]  # índice 0-based
    text = page_data['text']
    
    # Pegar as primeiras linhas significativas
    lines = [l.strip() for l in text.split('\n') if l.strip() and not l.strip().isdigit()]
    
    # Procurar por títulos em maiúsculas ou formatação especial
    title_found = None
    
    for i, line in enumerate(lines[:30]):  # Primeiras 30 linhas
        # Procurar por padrões de título
        if len(line) > 5 and len(line) < 80:
            # Título em maiúsculas
            if line.isupper() and 'CAPÍTULO' not in line and 'PÁGINA' not in line:
                title_found = line
                break
            # Título com primeira letra maiúscula (padrão comum)
            elif re.match(r'^[A-ZÁÉÍÓÚ][a-záéíóúâêôãõç\s]+$', line) and len(line) > 10:
                if not line.startswith('Você') and not line.startswith('O ') and \
                   not line.startswith('A ') and not line.startswith('E ') and \
                   not line.startswith('Um '):
                    title_found = line
                    break
    
    # Se não encontrou título óbvio, usar a descrição do sumário
    if not title_found:
        title_found = sections_map[page_num]
    
    results.append((page_num, title_found))
    print(f"Página {page_num}: {title_found}")

# Agora vamos buscar subseções do Combate Avançado
print("\n" + "=" * 80)
print("SUBSEÇÕES DE COMBATE AVANÇADO (p. 296-304)")
print("=" * 80)

combat_pages = range(296, 305)
for page_num in combat_pages:
    page_data = data['pages'][page_num - 1]
    text = page_data['text']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    # Procurar por "Tabela" nas linhas
    for line in lines[:40]:
        if 'Tabela' in line or 'TABELA' in line:
            if 'Acertos Críticos' in line or 'Teste de Morte' in line or 'Falhas Críticas' in line:
                print(f"Página {page_num}: {line}")
                break

print("\n" + "=" * 80)
print("Análise Completa - Seções do Capítulo 4 Identificadas")
print("=" * 80)

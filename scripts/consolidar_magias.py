"""
Script para consolidar magias por círculo, removendo duplicatas.
Lê todos os arquivos de subdivisão alfabética e cria um arquivo único por círculo.
"""

import re
from pathlib import Path
from collections import OrderedDict

# Diretório das magias
MAGIA_DIR = Path(__file__).parent.parent / "livros" / "tormenta20-core" / "09-magia"

# Padrão para identificar magias
SPELL_HEADER_PATTERN = re.compile(r'^## ([A-ZÀ-Ú].*?)$', re.MULTILINE)

def extrair_magias_de_arquivo(filepath):
    """Extrai magias de um arquivo, retornando dict {nome: conteúdo completo}"""
    content = filepath.read_text(encoding='utf-8')
    
    # Encontrar todas as posições de cabeçalhos de magias
    matches = list(SPELL_HEADER_PATTERN.finditer(content))
    
    magias = OrderedDict()
    
    for i, match in enumerate(matches):
        spell_name = match.group(1).strip()
        start_pos = match.start()
        
        # Fim é o início da próxima magia, ou fim do arquivo
        if i < len(matches) - 1:
            end_pos = matches[i + 1].start()
        else:
            # Procurar pelo próximo divisor de navegação ou fim do arquivo
            nav_pattern = r'\n---\n\s*\['
            nav_match = re.search(nav_pattern, content[start_pos:])
            if nav_match:
                end_pos = start_pos + nav_match.start()
            else:
                end_pos = len(content)
        
        spell_content = content[start_pos:end_pos].rstrip()
        
        # Adicionar apenas se não existir (primeira ocorrência prevalece)
        if spell_name not in magias:
            magias[spell_name] = spell_content
    
    return magias

def consolidar_circulo(circulo_num):
    """Consolida todas as magias de um círculo em um único arquivo"""
    print(f"\n=== Processando Círculo {circulo_num} ===")
    
    # Padrões de arquivo para este círculo
    if circulo_num == 1:
        prefix = "03-descricao-magias-1-circulo"
    elif circulo_num == 2:
        prefix = "04-descricao-magias-2-circulo"
    elif circulo_num == 3:
        prefix = "06-descricao-magias-3-circulo"
    elif circulo_num == 4:
        prefix = "08-descricao-magias-4-circulo"
    elif circulo_num == 5:
        prefix = "10-descricao-magias-5-circulo"
    
    # Encontrar todos os arquivos deste círculo
    arquivos = sorted(MAGIA_DIR.glob(f"{prefix}-*.md"))
    
    print(f"Arquivos encontrados: {len(arquivos)}")
    for arq in arquivos:
        print(f"  - {arq.name}")
    
    # Coletar todas as magias (sem duplicatas)
    todas_magias = OrderedDict()
    
    for arquivo in arquivos:
        magias = extrair_magias_de_arquivo(arquivo)
        print(f"\n{arquivo.name}: {len(magias)} magias")
        
        for nome, conteudo in magias.items():
            if nome in todas_magias:
                print(f"  ⚠️  DUPLICATA IGNORADA: {nome}")
            else:
                todas_magias[nome] = conteudo
                print(f"  ✓ {nome}")
    
    print(f"\nTotal de magias únicas no círculo {circulo_num}: {len(todas_magias)}")
    
    # Criar arquivo consolidado
    output_file = MAGIA_DIR / f"{prefix}.md"
    
    # Ler o frontmatter do primeiro arquivo
    primeiro_arquivo = arquivos[0]
    content = primeiro_arquivo.read_text(encoding='utf-8')
    
    # Extrair frontmatter YAML
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(0)
        # Ajustar título
        frontmatter = re.sub(
            r'title: ".*?"',
            f'title: "Magias de {circulo_num}º Círculo"',
            frontmatter
        )
    else:
        frontmatter = f"""---
title: "Magias de {circulo_num}º Círculo"
book: "tormenta20-core"
chapter: "09-magia"
---

"""
    
    # Construir conteúdo consolidado
    output_content = frontmatter
    output_content += f"# Magias de {circulo_num}º Círculo\n\n"
    output_content += f"> Todas as magias de {circulo_num}º círculo em ordem alfabética\n\n"
    output_content += "---\n\n"
    
    # Adicionar todas as magias
    for spell_content in todas_magias.values():
        output_content += spell_content + "\n\n"
    
    # Adicionar navegação
    nav_lines = []
    if circulo_num > 1:
        prev_num = circulo_num - 1
        if prev_num == 1:
            prev_file = "03-descricao-magias-1-circulo.md"
        elif prev_num == 2:
            prev_file = "04-descricao-magias-2-circulo.md"
        elif prev_num == 3:
            prev_file = "06-descricao-magias-3-circulo.md"
        elif prev_num == 4:
            prev_file = "08-descricao-magias-4-circulo.md"
        nav_lines.append(f"[◄ Anterior: {prev_num}º Círculo]({prev_file})")
    
    nav_lines.append("[Voltar para Magia](README.md)")
    
    if circulo_num < 5:
        next_num = circulo_num + 1
        if next_num == 2:
            next_file = "04-descricao-magias-2-circulo.md"
        elif next_num == 3:
            next_file = "06-descricao-magias-3-circulo.md"
        elif next_num == 4:
            next_file = "08-descricao-magias-4-circulo.md"
        elif next_num == 5:
            next_file = "10-descricao-magias-5-circulo.md"
        nav_lines.append(f"[Próximo: {next_num}º Círculo ►]({next_file})")
    
    output_content += "---\n\n"
    output_content += " | ".join(nav_lines) + "\n"
    
    # Salvar arquivo consolidado
    output_file.write_text(output_content, encoding='utf-8')
    print(f"\n✓ Arquivo consolidado criado: {output_file.name}")
    print(f"  Tamanho: {len(output_content)} caracteres")
    
    return len(todas_magias), arquivos

def main():
    print("=" * 70)
    print("CONSOLIDAÇÃO DE MAGIAS POR CÍRCULO")
    print("=" * 70)
    
    total_magias = 0
    arquivos_para_deletar = []
    
    for circulo in range(1, 6):
        num_magias, arquivos_antigos = consolidar_circulo(circulo)
        total_magias += num_magias
        arquivos_para_deletar.extend(arquivos_antigos)
    
    print("\n" + "=" * 70)
    print(f"TOTAL DE MAGIAS ÚNICAS: {total_magias}")
    print("=" * 70)
    
    # Deletar arquivos antigos com subdivisões
    print(f"\n\nDeletando {len(arquivos_para_deletar)} arquivos antigos...")
    for arquivo in arquivos_para_deletar:
        print(f"  🗑️  {arquivo.name}")
        arquivo.unlink()
    
    print("\n✓ Consolidação concluída com sucesso!")
    print(f"✓ {total_magias} magias únicas em 5 arquivos (um por círculo)")

if __name__ == "__main__":
    main()

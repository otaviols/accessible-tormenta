"""
Script para extrair conteúdo do PDF Tormenta 20 e gerar estrutura inicial
Requer: pip install PyPDF2 pdfplumber
"""

import PyPDF2
import pdfplumber
import json
import os
from pathlib import Path

def extract_pdf_content(pdf_path):
    """Extrai texto, estrutura e metadados do PDF"""
    
    print(f"Extraindo conteúdo de: {pdf_path}")
    
    # Estrutura para armazenar conteúdo extraído
    content = {
        'metadata': {},
        'toc': [],
        'pages': [],
        'tables': [],
        'images': []
    }
    
    # Extrair metadados e texto com PyPDF2
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Metadados
        if pdf_reader.metadata:
            content['metadata'] = {
                'title': pdf_reader.metadata.get('/Title', ''),
                'author': pdf_reader.metadata.get('/Author', ''),
                'pages': len(pdf_reader.pages)
            }
        
        print(f"Total de páginas: {len(pdf_reader.pages)}")
        
        # Extrair índice/bookmarks se existir
        if hasattr(pdf_reader, 'outline') and pdf_reader.outline:
            content['toc'] = extract_outline(pdf_reader.outline)
    
    # Extrair texto e tabelas com pdfplumber (melhor para tabelas)
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            print(f"Processando página {page_num}/{len(pdf.pages)}")
            
            page_data = {
                'number': page_num,
                'text': page.extract_text() or '',
                'tables': []
            }
            
            # Extrair tabelas
            tables = page.extract_tables()
            if tables:
                for table_idx, table in enumerate(tables):
                    if table:  # Verificar se tabela não está vazia
                        page_data['tables'].append({
                            'table_index': table_idx,
                            'data': table
                        })
                        content['tables'].append({
                            'page': page_num,
                            'table_index': table_idx,
                            'data': table
                        })
            
            content['pages'].append(page_data)
            
            # Detectar imagens (contagem)
            if hasattr(page, 'images'):
                for img_idx, img in enumerate(page.images):
                    content['images'].append({
                        'page': page_num,
                        'index': img_idx,
                        'x0': img.get('x0'),
                        'y0': img.get('y0'),
                        'x1': img.get('x1'),
                        'y1': img.get('y1')
                    })
    
    return content

def extract_outline(outline, level=0):
    """Extrai outline/bookmarks recursivamente"""
    toc = []
    for item in outline:
        if isinstance(item, list):
            toc.extend(extract_outline(item, level + 1))
        else:
            toc.append({
                'title': item.get('/Title', ''),
                'level': level,
                'page': item.get('/Page', None)
            })
    return toc

def save_extraction(content, output_dir):
    """Salva conteúdo extraído em arquivos"""
    
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Salvar estrutura completa em JSON
    with open(output_path / 'extracted_content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    # Salvar índice em formato legível
    with open(output_path / 'table_of_contents.txt', 'w', encoding='utf-8') as f:
        f.write("ÍNDICE DO PDF TORMENTA 20\n")
        f.write("=" * 50 + "\n\n")
        for item in content['toc']:
            indent = "  " * item['level']
            f.write(f"{indent}- {item['title']}\n")
    
    # Salvar texto completo por página
    with open(output_path / 'full_text.txt', 'w', encoding='utf-8') as f:
        for page in content['pages']:
            f.write(f"\n{'='*60}\n")
            f.write(f"PÁGINA {page['number']}\n")
            f.write(f"{'='*60}\n\n")
            f.write(page['text'])
            f.write("\n")
    
    # Salvar informações sobre tabelas
    with open(output_path / 'tables_info.txt', 'w', encoding='utf-8') as f:
        f.write(f"TOTAL DE TABELAS ENCONTRADAS: {len(content['tables'])}\n\n")
        for idx, table in enumerate(content['tables']):
            f.write(f"Tabela {idx+1} - Página {table['page']}\n")
            f.write(f"Linhas: {len(table['data'])}\n")
            if table['data']:
                f.write(f"Colunas: {len(table['data'][0])}\n")
            f.write("-" * 40 + "\n")
    
    # Salvar informações sobre imagens
    with open(output_path / 'images_info.txt', 'w', encoding='utf-8') as f:
        f.write(f"TOTAL DE IMAGENS ENCONTRADAS: {len(content['images'])}\n\n")
        pages_with_images = {}
        for img in content['images']:
            page = img['page']
            pages_with_images[page] = pages_with_images.get(page, 0) + 1
        
        for page in sorted(pages_with_images.keys()):
            f.write(f"Página {page}: {pages_with_images[page]} imagem(ns)\n")
    
    print(f"\nExtração completa! Arquivos salvos em: {output_path}")
    print(f"- Páginas: {content['metadata'].get('pages', 0)}")
    print(f"- Seções no índice: {len(content['toc'])}")
    print(f"- Tabelas: {len(content['tables'])}")
    print(f"- Imagens: {len(content['images'])}")

if __name__ == "__main__":
    pdf_path = "Tormenta 20 - Jogo do Ano (2).pdf"
    output_dir = "extracted"
    
    if not os.path.exists(pdf_path):
        print(f"ERRO: Arquivo '{pdf_path}' não encontrado!")
        print("Certifique-se de estar no diretório correto.")
    else:
        try:
            content = extract_pdf_content(pdf_path)
            save_extraction(content, output_dir)
        except Exception as e:
            print(f"ERRO durante extração: {e}")
            import traceback
            traceback.print_exc()

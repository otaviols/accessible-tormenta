"""
Script para processamento em lote de múltiplos PDFs
Lê configurações de extraction_config.json e executa extrações
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime
from extract_pdf import extract_pdf

def load_config(config_path='extraction_config.json'):
    """Carrega configurações do arquivo JSON"""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"✗ ERRO: Arquivo de configuração '{config_path}' não encontrado!")
        return None
    except json.JSONDecodeError as e:
        print(f"✗ ERRO: Arquivo de configuração inválido: {e}")
        return None

def save_config(config, config_path='extraction_config.json'):
    """Salva configurações atualizadas no arquivo JSON"""
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"✗ ERRO ao salvar configuração: {e}")
        return False

def update_extraction_entry(config, extraction_id, result):
    """Atualiza entrada de extração com resultados"""
    for entry in config['extractions']:
        if entry['id'] == extraction_id:
            entry['extraction_date'] = datetime.now().strftime('%Y-%m-%d')
            entry['status'] = 'completed' if result['success'] else 'failed'
            if result['success']:
                entry['page_count'] = result['stats']['pages']
                entry['stats'] = {
                    'toc_entries': result['stats']['toc_entries'],
                    'tables': result['stats']['tables'],
                    'images': result['stats']['images']
                }
            return True
    return False

def process_extractions(config, skip_existing=True, filter_ids=None):
    """
    Processa múltiplas extrações de PDFs
    
    Args:
        config (dict): Configuração carregada do JSON
        skip_existing (bool): Pular PDFs já extraídos (status=completed)
        filter_ids (list): Lista de IDs específicos para processar (None = todos)
    
    Returns:
        dict: Relatório com resultados de todas extrações
    """
    report = {
        'start_time': datetime.now().isoformat(),
        'total': 0,
        'processed': 0,
        'skipped': 0,
        'successful': 0,
        'failed': 0,
        'results': []
    }
    
    extractions = config.get('extractions', [])
    report['total'] = len(extractions)
    
    print(f"\n{'='*70}")
    print(f"PROCESSAMENTO EM LOTE - {len(extractions)} PDFs configurados")
    print(f"{'='*70}\n")
    
    for idx, entry in enumerate(extractions, 1):
        extraction_id = entry.get('id')
        pdf_path = entry.get('pdf_path')
        output_dir = entry.get('output_dir')
        status = entry.get('status', 'pending')
        
        # Filtrar por IDs se especificado
        if filter_ids and extraction_id not in filter_ids:
            continue
        
        print(f"\n[{idx}/{len(extractions)}] Processando: {extraction_id}")
        print(f"  PDF: {pdf_path}")
        print(f"  Status atual: {status}")
        
        # Verificar se deve pular
        if skip_existing and status == 'completed':
            print(f"  ⊘ Pulando (já extraído)")
            report['skipped'] += 1
            report['results'].append({
                'id': extraction_id,
                'action': 'skipped',
                'reason': 'already completed'
            })
            continue
        
        # Verificar se PDF existe
        if not os.path.exists(pdf_path):
            print(f"  ✗ ERRO: PDF não encontrado!")
            report['failed'] += 1
            report['results'].append({
                'id': extraction_id,
                'action': 'failed',
                'error': 'PDF file not found'
            })
            continue
        
        # Executar extração
        try:
            result = extract_pdf(pdf_path, output_dir)
            
            if result['success']:
                print(f"  ✓ Extração concluída")
                report['successful'] += 1
                report['results'].append({
                    'id': extraction_id,
                    'action': 'extracted',
                    'stats': result['stats']
                })
                
                # Atualizar configuração
                update_extraction_entry(config, extraction_id, result)
            else:
                print(f"  ✗ Extração falhou")
                report['failed'] += 1
                report['results'].append({
                    'id': extraction_id,
                    'action': 'failed',
                    'error': 'extraction returned success=False'
                })
                
        except Exception as e:
            print(f"  ✗ ERRO: {e}")
            report['failed'] += 1
            report['results'].append({
                'id': extraction_id,
                'action': 'failed',
                'error': str(e)
            })
        
        report['processed'] += 1
    
    report['end_time'] = datetime.now().isoformat()
    return report

def save_report(report, report_path='extraction_report.txt'):
    """Salva relatório consolidado em arquivo texto"""
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("=" * 70 + "\n")
            f.write("RELATÓRIO DE EXTRAÇÃO EM LOTE\n")
            f.write("=" * 70 + "\n\n")
            
            f.write(f"Início: {report['start_time']}\n")
            f.write(f"Término: {report['end_time']}\n\n")
            
            f.write(f"RESUMO:\n")
            f.write(f"  Total configurados: {report['total']}\n")
            f.write(f"  Processados: {report['processed']}\n")
            f.write(f"  Pulados: {report['skipped']}\n")
            f.write(f"  Bem-sucedidos: {report['successful']}\n")
            f.write(f"  Falharam: {report['failed']}\n\n")
            
            f.write("=" * 70 + "\n")
            f.write("DETALHES POR PDF\n")
            f.write("=" * 70 + "\n\n")
            
            for result in report['results']:
                f.write(f"ID: {result['id']}\n")
                f.write(f"  Ação: {result['action']}\n")
                
                if result['action'] == 'extracted':
                    stats = result['stats']
                    f.write(f"  Páginas: {stats['pages']}\n")
                    f.write(f"  Tabelas: {stats['tables']}\n")
                    f.write(f"  Imagens: {stats['images']}\n")
                elif result['action'] == 'failed':
                    f.write(f"  Erro: {result['error']}\n")
                elif result['action'] == 'skipped':
                    f.write(f"  Motivo: {result['reason']}\n")
                
                f.write("\n")
        
        return True
    except Exception as e:
        print(f"✗ ERRO ao salvar relatório: {e}")
        return False

def print_summary(report):
    """Imprime resumo do processamento"""
    print(f"\n{'='*70}")
    print(f"RESUMO DA EXECUÇÃO")
    print(f"{'='*70}\n")
    print(f"  Total configurados: {report['total']}")
    print(f"  Processados: {report['processed']}")
    print(f"  Pulados: {report['skipped']}")
    print(f"  ✓ Bem-sucedidos: {report['successful']}")
    print(f"  ✗ Falharam: {report['failed']}")
    print(f"\n{'='*70}\n")

def main():
    """Execução principal do processamento em lote"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Processa múltiplos PDFs configurados em extraction_config.json',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python extract_multiple.py
  python extract_multiple.py --force
  python extract_multiple.py --ids tormenta-core ameacas
        """
    )
    
    parser.add_argument(
        '--config',
        type=str,
        default='extraction_config.json',
        help='Caminho para arquivo de configuração (padrão: extraction_config.json)'
    )
    
    parser.add_argument(
        '--force',
        action='store_true',
        help='Reprocessar PDFs já extraídos (ignora status completed)'
    )
    
    parser.add_argument(
        '--ids',
        nargs='+',
        help='Processar apenas PDFs com IDs específicos'
    )
    
    parser.add_argument(
        '--report',
        type=str,
        default='extraction_report.txt',
        help='Caminho para salvar relatório (padrão: extraction_report.txt)'
    )
    
    args = parser.parse_args()
    
    # Carregar configuração
    config = load_config(args.config)
    if not config:
        return 1
    
    # Processar extrações
    skip_existing = not args.force
    report = process_extractions(config, skip_existing=skip_existing, filter_ids=args.ids)
    
    # Salvar configuração atualizada
    if report['successful'] > 0:
        if save_config(config, args.config):
            print(f"✓ Configuração atualizada em: {args.config}")
    
    # Salvar relatório
    if save_report(report, args.report):
        print(f"✓ Relatório salvo em: {args.report}")
    
    # Imprimir resumo
    print_summary(report)
    
    # Código de saída
    return 0 if report['failed'] == 0 else 1

if __name__ == "__main__":
    exit(main())

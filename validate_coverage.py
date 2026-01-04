"""
Validador de cobertura entre o PDF original (full_text.txt)
 e a documentação em Markdown na pasta docs/.

Estratégia (profunda, mas aproximada):
- Lê extracted/full_text.txt, identificando páginas e parágrafos.
- Ignora cabeçalhos de página e linhas muito curtas.
- Normaliza texto (minúsculas, espaços) para reduzir ruído.
- Agrupa linhas em parágrafos por página.
- Verifica se cada parágrafo "longo" do PDF aparece, como
  substring exata, em algum lugar do texto combinado de docs/.
- Gera um relatório com os parágrafos não encontrados
  (potenciais trechos não cobertos ou reescritos demais).

Limitações importantes:
- Apenas busca correspondência textual exata (já normalizada).
  Se o conteúdo tiver sido muito reescrito para acessibilidade,
  pode ser marcado como "não encontrado" mesmo estando coberto.
- O objetivo é servir como FERRAMENTA DE APOIO à auditoria,
  não uma prova matemática de cobertura 1:1.

Uso:
    python validate_coverage.py

Saída:
- Resumo geral no stdout.
- Arquivo "coverage_report.txt" com detalhes dos parágrafos
  considerados não cobertos.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable, List, Tuple

ROOT_DIR = Path(__file__).resolve().parent
EXTRACTED_DIR = ROOT_DIR / "extracted"
DOCS_DIR = ROOT_DIR / "docs"
FULL_TEXT_PATH = EXTRACTED_DIR / "full_text.txt"
REPORT_PATH = ROOT_DIR / "coverage_report.txt"


def normalize_text(text: str) -> str:
    """Normaliza texto para comparação.

    - Converte para minúsculas.
    - Substitui quebras de linha por espaço.
    - Colapsa espaços múltiplos.
    - Remove espaços nas pontas.
    """

    import re

    text = text.lower()
    text = text.replace("\r", " ").replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def iter_pdf_paragraphs(full_text: str) -> Iterable[Tuple[int, str]]:
    """Itera sobre parágrafos do PDF.

    Retorna tuplas (pagina_atual, paragrafo_bruto).

    Heurística:
    - Detecta páginas pelo padrão "PÁGINA X".
    - Ignora linhas de separador (====...) e linhas vazias isoladas.
    - Agrupa linhas não vazias em parágrafos, separados por linhas vazias.
    """

    lines = full_text.splitlines()
    current_page = 0
    buffer: List[str] = []

    def flush_buffer(page: int) -> Iterable[Tuple[int, str]]:
        nonlocal buffer
        if not buffer:
            return []
        paragraph = " ".join(line.strip() for line in buffer if line.strip())
        buffer = []
        if paragraph:
            return [(page, paragraph)]
        return []

    for raw_line in lines:
        line = raw_line.strip()

        # Separadores de página
        if line.startswith("PÁGINA ") and line[7:].strip().isdigit():
            # Nova página: esvaziar parágrafo anterior
            for item in flush_buffer(current_page):
                yield item
            try:
                current_page = int(line[7:].strip())
            except ValueError:
                pass
            continue

        # Linhas de separador visual
        if set(line) == {"="}:
            # Esvaziar parágrafo anterior, se houver
            for item in flush_buffer(current_page):
                yield item
            continue

        # Quebra de parágrafo
        if not line:
            for item in flush_buffer(current_page):
                yield item
            continue

        # Linha de conteúdo normal
        buffer.append(line)

    # Final do arquivo
    for item in flush_buffer(current_page):
        yield item


def load_docs_text(root: Path) -> str:
    """Carrega e combina o texto de todos os arquivos .md em docs/.

    Normaliza também para comparação.
    """

    all_text_parts: List[str] = []

    for path in root.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                text = path.read_text(encoding="latin-1")
            except Exception:
                print(f"[AVISO] Não foi possível ler {path} (problema de encoding)")
                continue
        all_text_parts.append(text)

    combined = "\n".join(all_text_parts)
    return normalize_text(combined)


def main() -> None:
    if not FULL_TEXT_PATH.exists():
        raise SystemExit(
            f"Arquivo full_text.txt não encontrado em {FULL_TEXT_PATH}. "
            "Certifique-se de ter rodado extract_pdf.py antes."
        )

    if not DOCS_DIR.exists():
        raise SystemExit(f"Pasta docs/ não encontrada em {DOCS_DIR}.")

    print("Carregando texto completo do PDF a partir de extracted/full_text.txt...")
    full_text = FULL_TEXT_PATH.read_text(encoding="utf-8", errors="ignore")

    print("Carregando e normalizando texto de todos os arquivos .md em docs/...")
    docs_text_normalized = load_docs_text(DOCS_DIR)

    print("Analisando parágrafos do PDF e verificando cobertura no Markdown...")

    MIN_PARAGRAPH_LEN = 120  # caracteres mínimos após normalização para considerar

    total_paragraphs = 0
    considered_paragraphs = 0
    covered_paragraphs = 0
    missing_paragraphs: List[Tuple[int, str]] = []

    for page, raw_paragraph in iter_pdf_paragraphs(full_text):
        total_paragraphs += 1

        normalized_para = normalize_text(raw_paragraph)
        if len(normalized_para) < MIN_PARAGRAPH_LEN:
            # Ignorar parágrafos muito curtos (títulos, cabeçalhos, etc.)
            continue

        considered_paragraphs += 1

        # Heurística simples: verificar se o parágrafo (normalizado) aparece
        # como substring do texto combinado dos .md.
        if normalized_para in docs_text_normalized:
            covered_paragraphs += 1
        else:
            missing_paragraphs.append((page, raw_paragraph))

    coverage_ratio = (
        (covered_paragraphs / considered_paragraphs) * 100.0
        if considered_paragraphs
        else 0.0
    )

    print("\n=== RESUMO DE COBERTURA (APROXIMADA) ===")
    print(f"Parágrafos totais no PDF (incluindo curtos): {total_paragraphs}")
    print(f"Parágrafos considerados (>= {MIN_PARAGRAPH_LEN} chars): {considered_paragraphs}")
    print(f"Parágrafos encontrados em docs/: {covered_paragraphs}")
    print(f"Parágrafos possivelmente ausentes: {len(missing_paragraphs)}")
    print(f"Cobertura aproximada: {coverage_ratio:.2f}%")

    # Gerar relatório detalhado
    print(f"\nGerando relatório detalhado em {REPORT_PATH}...")

    with REPORT_PATH.open("w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE COBERTURA PDF → DOCS\n")
        f.write("=" * 72 + "\n\n")
        f.write("ATENÇÃO: Este relatório é heurístico.\n")
        f.write(
            "Um parágrafo marcado como 'não encontrado' pode já estar coberto "
            "se tiver sido reescrito de forma diferente.\n\n"
        )
        f.write("Configuração usada:\n")
        f.write(f"- MIN_PARAGRAPH_LEN: {MIN_PARAGRAPH_LEN}\n")
        f.write("\n")
        f.write("RESUMO:\n")
        f.write(f"- Parágrafos considerados: {considered_paragraphs}\n")
        f.write(f"- Encontrados em docs/: {covered_paragraphs}\n")
        f.write(f"- Possivelmente ausentes: {len(missing_paragraphs)}\n")
        f.write(f"- Cobertura aproximada: {coverage_ratio:.2f}%\n")
        f.write("\n")

        if not missing_paragraphs:
            f.write("Nenhum parágrafo longo foi marcado como ausente.\n")
        else:
            f.write("PARÁGRAFOS POSSIVELMENTE NÃO COBERTOS:\n")
            f.write("-" * 72 + "\n\n")
            for idx, (page, paragraph) in enumerate(missing_paragraphs, 1):
                f.write(f"[{idx}] Página: {page}\n")
                f.write(paragraph.strip() + "\n\n")
                f.write("-" * 72 + "\n\n")

    print("Concluído. Revise coverage_report.txt para analisar os trechos sinalizados.")


if __name__ == "__main__":
    main()

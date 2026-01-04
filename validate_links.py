"""
Validador de links Markdown para o projeto Tormenta 20 acessível.

Estratégia escolhida (A):
- Nenhuma correção automática de links.
- Apenas varredura de TODOS os arquivos .md na árvore do projeto
  (a partir da raiz onde este script está), com relatório de:
  - Links quebrados (arquivo alvo inexistente).
  - Arquivos .md não referenciados por nenhum outro ("órfãos").

Uso:
    python validate_links.py

Saída:
- Resumo geral no stdout.
- Relatório detalhado em "link_report.txt" com:
  - Lista de links quebrados, com arquivo de origem e href original.
  - Lista de arquivos .md que não são referenciados por nenhum outro .md.

Observações:
- Links absolutos (http://, https://, mailto:, etc.) são ignorados.
- Links somente com âncora (por exemplo, "#secao") também são ignorados.
- Links com caminho relativo + âncora ("arquivo.md#ancora") têm apenas
  o arquivo checado; a existência da âncora não é verificada neste script.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Set

ROOT_DIR = Path(__file__).resolve().parent
REPORT_PATH = ROOT_DIR / "link_report.txt"


MD_LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


@dataclass
class BrokenLink:
    source_file: Path
    line_no: int
    link_text: str
    href: str


def is_external_link(href: str) -> bool:
    href = href.strip().lower()
    if not href:
        return True
    if href.startswith("http://") or href.startswith("https://"):
        return True
    if href.startswith("mailto:"):
        return True
    if href.startswith("tel:"):
        return True
    if href.startswith("#"):
        # Apenas âncora local
        return True
    return False


def find_markdown_files(root: Path) -> List[Path]:
    return [p for p in root.rglob("*.md") if p.is_file()]


def scan_file_for_links(path: Path) -> List[BrokenLink]:
    broken: List[BrokenLink] = []

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            text = path.read_text(encoding="latin-1")
        except Exception:
            print(f"[AVISO] Não foi possível ler {path} (problema de encoding)")
            return broken

    base_dir = path.parent

    for idx, line in enumerate(text.splitlines(), start=1):
        for match in MD_LINK_PATTERN.finditer(line):
            link_text = match.group(1).strip()
            href = match.group(2).strip()

            if is_external_link(href):
                continue

            # Separar âncora, se houver
            target_path_str, *_anchor = href.split("#", 1)
            target_path_str = target_path_str.strip()

            if not target_path_str:
                continue

            target_path = (base_dir / target_path_str).resolve()

            if not target_path.exists():
                broken.append(
                    BrokenLink(
                        source_file=path,
                        line_no=idx,
                        link_text=link_text,
                        href=href,
                    )
                )

    return broken


def build_reference_graph(md_files: List[Path]) -> Dict[Path, Set[Path]]:
    """Constroi um grafo simples de referências entre arquivos .md.

    Retorna um dicionário: arquivo_alvo -> conjunto_de_arquivos_que_referenciam.
    """

    refs: Dict[Path, Set[Path]] = {p: set() for p in md_files}
    md_set = {p.resolve() for p in md_files}

    for path in md_files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                text = path.read_text(encoding="latin-1")
            except Exception:
                continue

        base_dir = path.parent

        for line in text.splitlines():
            for match in MD_LINK_PATTERN.finditer(line):
                href = match.group(2).strip()
                if is_external_link(href):
                    continue

                target_path_str, *_anchor = href.split("#", 1)
                target_path_str = target_path_str.strip()
                if not target_path_str:
                    continue

                target_path = (base_dir / target_path_str).resolve()
                if target_path in md_set:
                    refs[target_path].add(path)

    return refs


def main() -> None:
    print("Procurando arquivos Markdown (.md) a partir da raiz do projeto...")
    md_files = find_markdown_files(ROOT_DIR)
    print(f"Encontrados {len(md_files)} arquivos .md.")

    print("\nVerificando links internos em cada arquivo...")
    all_broken_links: List[BrokenLink] = []

    for path in md_files:
        broken = scan_file_for_links(path)
        all_broken_links.extend(broken)

    print("Construindo grafo de referências entre arquivos .md...")
    refs = build_reference_graph(md_files)

    # Arquivos órfãos: não referenciados por nenhum outro .md
    orphan_files = sorted([p for p, incoming in refs.items() if not incoming])

    print("\n=== RESUMO DE LINKS ===")
    print(f"Total de arquivos .md: {len(md_files)}")
    print(f"Links quebrados encontrados: {len(all_broken_links)}")
    print(f"Arquivos .md não referenciados (órfãos): {len(orphan_files)}")

    print(f"\nGerando relatório detalhado em {REPORT_PATH}...")

    with REPORT_PATH.open("w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE LINKS MARKDOWN\n")
        f.write("=" * 72 + "\n\n")

        f.write("RESUMO:\n")
        f.write(f"- Arquivos .md analisados: {len(md_files)}\n")
        f.write(f"- Links quebrados: {len(all_broken_links)}\n")
        f.write(f"- Arquivos órfãos: {len(orphan_files)}\n")
        f.write("\n")

        if all_broken_links:
            f.write("LINKS QUEBRADOS:\n")
            f.write("-" * 72 + "\n\n")
            for bl in all_broken_links:
                rel_source = bl.source_file.relative_to(ROOT_DIR)
                f.write(f"Arquivo: {rel_source} (linha {bl.line_no})\n")
                f.write(f"  Texto: [{bl.link_text}]\n")
                f.write(f"  Href:  ({bl.href})\n")
                f.write("\n")
        else:
            f.write("Nenhum link quebrado encontrado.\n\n")

        f.write("\nARQUIVOS .MD ÓRFÃOS (não referenciados por nenhum outro .md):\n")
        f.write("-" * 72 + "\n\n")
        if orphan_files:
            for p in orphan_files:
                rel = p.relative_to(ROOT_DIR)
                f.write(f"- {rel}\n")
        else:
            f.write("Nenhum arquivo órfão detectado.\n")

    print("Concluído. Revise link_report.txt para detalhes de correções manuais.")


if __name__ == "__main__":
    main()

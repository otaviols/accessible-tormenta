#!/usr/bin/env python3
"""
Script para criar scaffold (estrutura inicial) de um novo livro de Tormenta 20.

Uso:
    python scripts/new_book_scaffold.py "nome-do-livro" "Título Completo do Livro"

Exemplo:
    python scripts/new_book_scaffold.py "ameacas-tormenta" "Ameaças da Tormenta"
"""

import os
import sys
from pathlib import Path
from datetime import datetime


def create_book_scaffold(book_slug: str, book_title: str, base_path: str = "livros"):
    """
    Cria a estrutura completa de diretórios e arquivos iniciais para um novo livro.
    
    Args:
        book_slug: Nome do livro em formato kebab-case (ex: "herois-arton")
        book_title: Título completo do livro (ex: "Heróis de Arton")
        base_path: Caminho base onde ficam os livros (padrão: "livros")
    """
    
    # Validar slug
    if not book_slug.islower() or ' ' in book_slug:
        print(f"❌ ERRO: O slug '{book_slug}' deve estar em kebab-case (minúsculas, hífens)")
        print(f"   Exemplo correto: 'herois-arton', 'ameacas-tormenta'")
        return False
    
    # Caminhos principais
    project_root = Path(__file__).parent.parent
    book_path = project_root / base_path / book_slug
    images_path = project_root / base_path / "_imagens" / book_slug
    
    # Verificar se livro já existe
    if book_path.exists():
        print(f"⚠️  AVISO: O livro '{book_slug}' já existe em {book_path}")
        response = input("Deseja sobrescrever? (s/N): ")
        if response.lower() != 's':
            print("Operação cancelada.")
            return False
    
    print(f"\n📚 Criando estrutura para: {book_title}")
    print(f"   Slug: {book_slug}")
    print(f"   Caminho: {book_path}\n")
    
    # Criar diretórios principais
    print("📁 Criando diretórios...")
    
    directories = [
        book_path,
        book_path / "01-introducao",
        book_path / "02-personagens",
        book_path / "03-racas",
        book_path / "04-classes",
        book_path / "05-pericias-poderes",
        book_path / "06-equipamento",
        book_path / "07-regras",
        book_path / "08-combate",
        book_path / "09-magia",
        book_path / "10-mestre",
        images_path,
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"   ✓ {directory.relative_to(project_root)}/")
    
    # Criar README.md principal do livro
    print("\n📄 Criando README.md...")
    
    readme_content = f"""# {book_title}

> Documentação completa do livro "{book_title}" em formato Markdown acessível

---

## 📖 Sobre Este Livro

{book_title} é [DESCRIÇÃO DO LIVRO - PREENCHER].

Esta documentação mantém todos os padrões de acessibilidade do projeto Tormenta 20:

- ✅ **Compatível com leitores de tela** (NVDA, JAWS)
- ✅ **Navegação estruturada** com links internos
- ✅ **Markdown puro** sem HTML
- ✅ **Transcrição literal** do conteúdo original

---

## 📚 Índice de Capítulos

### [01 - Introdução](01-introducao/README.md)
[DESCRIÇÃO DO CAPÍTULO]

### [02 - Personagens](02-personagens/README.md)
[DESCRIÇÃO DO CAPÍTULO]

### [03 - Raças](03-racas/README.md)
[DESCRIÇÃO DO CAPÍTULO]

### [04 - Classes](04-classes/README.md)
[DESCRIÇÃO DO CAPÍTULO]

### [05 - Perícias e Poderes](05-pericias-poderes/README.md)
[DESCRIÇÃO DO CAPÍTULO]

### [06 - Equipamento](06-equipamento/README.md)
[DESCRIÇÃO DO CAPÍTULO]

### [07 - Regras](07-regras/README.md)
[DESCRIÇÃO DO CAPÍTULO]

### [08 - Combate](08-combate/README.md)
[DESCRIÇÃO DO CAPÍTULO]

### [09 - Magia](09-magia/README.md)
[DESCRIÇÃO DO CAPÍTULO]

### [10 - Mestre](10-mestre/README.md)
[DESCRIÇÃO DO CAPÍTULO]

---

## 📊 Status da Conversão

Veja [PROGRESS.md](PROGRESS.md) para detalhes completos do progresso.

**Resumo:**
- 📄 Páginas: 0 de XXX (0%)
- 📁 Arquivos: 0 de ~XXX
- ✅ Status: EM PREPARAÇÃO

---

## 🔗 Navegação

- [← Voltar ao Índice Principal](../README.md)
- [Ver Progresso Detalhado](PROGRESS.md)

---

**Livro:** {book_title}  
**Sistema:** Tormenta 20  
**Versão da documentação:** 1.0  
**Última atualização:** {datetime.now().strftime("%d/%m/%Y")}
"""
    
    readme_path = book_path / "README.md"
    readme_path.write_text(readme_content, encoding='utf-8')
    print(f"   ✓ {readme_path.relative_to(project_root)}")
    
    # Criar PROGRESS.md
    print("\n📊 Criando PROGRESS.md...")
    
    progress_content = f"""# Progresso de Conversão - {book_title}

> **Status da conversão do livro "{book_title}" para documentação Markdown acessível**

**ÚLTIMA ATUALIZAÇÃO:** {datetime.now().strftime("%d/%m/%Y")}

---

## 📊 Progresso Geral

**Capítulos Completos:** 0 de 10 (0%)

**Estatísticas:**
- 📁 **Arquivos criados:** 0 arquivos markdown
- 📝 **Volume total:** 0 KB
- 🎯 **Páginas documentadas:** 0 de XXX (0%)
- ✅ **Status:** EM PREPARAÇÃO

---

## 📖 Status por Capítulo

### ⏳ Capítulo 1: Introdução (PENDENTE)
- 0 arquivos criados
- Páginas: [INTERVALO]
- Conteúdo esperado: [DESCRIÇÃO]

### ⏳ Capítulo 2: Personagens (PENDENTE)
- 0 arquivos criados
- Páginas: [INTERVALO]
- Conteúdo esperado: [DESCRIÇÃO]

### ⏳ Capítulo 3: Raças (PENDENTE)
- 0 arquivos criados
- Páginas: [INTERVALO]
- Conteúdo esperado: [DESCRIÇÃO]

### ⏳ Capítulo 4: Classes (PENDENTE)
- 0 arquivos criados
- Páginas: [INTERVALO]
- Conteúdo esperado: [DESCRIÇÃO]

### ⏳ Capítulo 5: Perícias e Poderes (PENDENTE)
- 0 arquivos criados
- Páginas: [INTERVALO]
- Conteúdo esperado: [DESCRIÇÃO]

### ⏳ Capítulo 6: Equipamento (PENDENTE)
- 0 arquivos criados
- Páginas: [INTERVALO]
- Conteúdo esperado: [DESCRIÇÃO]

### ⏳ Capítulo 7: Regras (PENDENTE)
- 0 arquivos criados
- Páginas: [INTERVALO]
- Conteúdo esperado: [DESCRIÇÃO]

### ⏳ Capítulo 8: Combate (PENDENTE)
- 0 arquivos criados
- Páginas: [INTERVALO]
- Conteúdo esperado: [DESCRIÇÃO]

### ⏳ Capítulo 9: Magia (PENDENTE)
- 0 arquivos criados
- Páginas: [INTERVALO]
- Conteúdo esperado: [DESCRIÇÃO]

### ⏳ Capítulo 10: Mestre (PENDENTE)
- 0 arquivos criados
- Páginas: [INTERVALO]
- Conteúdo esperado: [DESCRIÇÃO]

---

## 📝 Histórico de Sessões

### Sessão 1 - {datetime.now().strftime("%d/%m/%Y")}
- **Ação:** Criação da estrutura inicial do livro
- **Arquivos:** Scaffold criado com new_book_scaffold.py
- **Status:** Pronto para extração de conteúdo

---

## 🎯 Próximos Passos

1. Extrair PDF com `python scripts/extract_pdf.py`
2. Analisar estrutura do `full_text.txt`
3. Criar mapeamento de páginas para seções
4. Começar conversão por capítulos
5. Validar links e formatação

---

## 📚 Referências

- [Guia de Extração](../../EXTRACTION_GUIDE.md)
- [README Principal do Projeto](../../README.md)
- [README deste Livro](README.md)

---

**Livro:** {book_title}  
**Criado em:** {datetime.now().strftime("%d/%m/%Y")}
"""
    
    progress_path = book_path / "PROGRESS.md"
    progress_path.write_text(progress_content, encoding='utf-8')
    print(f"   ✓ {progress_path.relative_to(project_root)}")
    
    # Criar READMEs de exemplo para cada capítulo
    print("\n📑 Criando READMEs de capítulos...")
    
    chapters = [
        ("01-introducao", "Introdução"),
        ("02-personagens", "Personagens"),
        ("03-racas", "Raças"),
        ("04-classes", "Classes"),
        ("05-pericias-poderes", "Perícias e Poderes"),
        ("06-equipamento", "Equipamento"),
        ("07-regras", "Regras"),
        ("08-combate", "Combate"),
        ("09-magia", "Magia"),
        ("10-mestre", "Mestre"),
    ]
    
    for chapter_slug, chapter_title in chapters:
        chapter_readme = f"""# {chapter_title}

> Capítulo do livro {book_title}

---

## Conteúdo deste Capítulo

[DESCRIÇÃO DO QUE ESTE CAPÍTULO CONTÉM]

---

## Arquivos

[LISTA DE ARQUIVOS SERÁ ADICIONADA DURANTE A CONVERSÃO]

---

## Navegação

- [← Voltar ao {book_title}](../README.md)
- [Índice Principal](../../README.md)

---
"""
        chapter_path = book_path / chapter_slug / "README.md"
        chapter_path.write_text(chapter_readme, encoding='utf-8')
        print(f"   ✓ {chapter_slug}/README.md")
    
    # Resumo final
    print("\n" + "="*70)
    print(f"✅ SUCESSO! Estrutura do livro '{book_title}' criada com sucesso!")
    print("="*70)
    print(f"\n📂 Localização: {book_path.relative_to(project_root)}")
    print(f"🖼️  Imagens em: {images_path.relative_to(project_root)}")
    print(f"\n📋 Próximos passos:")
    print(f"   1. Colocar PDF em: Pdf files/{book_slug}.pdf")
    print(f"   2. Executar: python scripts/extract_pdf.py \"Pdf files/{book_slug}.pdf\" \"extracted/{book_slug}/\"")
    print(f"   3. Analisar extracted/{book_slug}/full_text.txt")
    print(f"   4. Começar conversão de conteúdo")
    print(f"   5. Atualizar PROGRESS.md conforme avança")
    print(f"\n📖 Consulte EXTRACTION_GUIDE.md para detalhes do processo completo.")
    print()
    
    return True


def main():
    """Função principal do script."""
    
    if len(sys.argv) < 3:
        print("❌ ERRO: Argumentos insuficientes")
        print("\nUso:")
        print("    python scripts/new_book_scaffold.py \"nome-do-livro\" \"Título Completo do Livro\"")
        print("\nExemplo:")
        print("    python scripts/new_book_scaffold.py \"ameacas-tormenta\" \"Ameaças da Tormenta\"")
        sys.exit(1)
    
    book_slug = sys.argv[1]
    book_title = sys.argv[2]
    
    success = create_book_scaffold(book_slug, book_title)
    
    if success:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()

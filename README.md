# Tormenta 20 - Projeto Multi-Livro

![Logo Tormenta20](livros/_imagens/tormenta20-core/logo-tormenta20.png)

Este projeto contém a conversão para Markdown dos livros do sistema Tormenta 20, organizados em uma estrutura multi-livro escalável.

## 📚 Livros Disponíveis

### [Tormenta 20 - Livro Básico](livros/tormenta20-core/README.md)
**Status:** 75% completo (9 de 12 capítulos)  
**Conteúdo:** 135 arquivos, ~990KB, ~300 páginas  
**Capítulos:** Introdução, Criação de Personagens, Raças (17), Classes (14), Perícias e Poderes, Equipamento, Regras de Jogo, Combate, Magia (186 magias), Mestre, Ambientação, Apêndices

### [Heróis de Arton](livros/herois-arton/README.md)
**Status:** 100% completo  
**Conteúdo:** 134 arquivos, ~2.7MB, 332 páginas  
**Capítulos:** Campeões de Arton (5 novas raças, classe Treinador, 14 variantes), Distinções (36), Novos Poderes, Arsenal dos Heróis (30+ magias, 100+ itens mágicos), Regras Opcionais (Bases, Domínios, 30+ regras)

## 📊 Estatísticas Gerais

| Métrica | Valor |
|---------|-------|
| **Livros** | 2 |
| **Arquivos Markdown** | 269 |
| **Tamanho Total** | ~3.7MB |
| **Páginas Totais** | ~632 |
| **Imagens** | 35+ PNG com alt-text |
| **Scripts** | 7 ferramentas de automação |

## 📁 Estrutura do Projeto

```
livros/
├── tormenta20-core/          # Livro Básico (135 arquivos)
│   ├── 01-introducao/
│   ├── 02-criacao-personagens/
│   ├── 03-racas/             # 17 raças
│   ├── 04-classes/           # 14 classes
│   ├── 05-pericias-poderes/
│   ├── 06-equipamento/
│   ├── 07-regras-jogo/
│   ├── 08-combate/
│   ├── 09-magia/             # 186 magias
│   ├── 10-mestre/
│   ├── 11-ambientacao/
│   ├── 13-apendices/
│   ├── README.md             # Índice do livro
│   └── PROGRESS.md           # Progresso de conversão
│
├── herois-arton/             # Heróis de Arton (134 arquivos)
│   ├── 01-campeoes-arton/    # 5 raças, Treinador, 14 variantes
│   ├── 02-distincoes/        # 36 distinções
│   ├── 02-novos-poderes/     # Centenas de poderes
│   ├── 03-arsenal-herois/    # 30+ magias, 100+ itens
│   ├── 04-regras-opcionais/  # Bases, Domínios, 30+ regras
│   ├── README.md
│   └── PROGRESS.md
│
└── _imagens/                 # Imagens compartilhadas
    ├── tormenta20-core/      # 35 PNGs
    ├── herois-arton/
    └── comuns/

scripts/                      # Ferramentas de automação
├── new_book_scaffold.py      # Gera estrutura de novo livro
├── migrate_links.py          # Atualiza links entre arquivos
├── normalize_frontmatter.py  # Padroniza frontmatter YAML
├── validate_links.py         # Valida todos os links
├── extract_pdf.py            # Extrai texto de PDFs
├── extract_multiple.py       # Extração em lote
└── analyze_cap4.py           # Análise de capítulos
```

## 🛠️ Scripts Disponíveis

### 1. Criar Novo Livro
```powershell
python scripts/new_book_scaffold.py nome-do-livro
```
Gera estrutura completa: diretórios, README.md, PROGRESS.md, capítulos padrão.

### 2. Migrar Links de Imagens
```powershell
# Modo visualização (dry-run)
python scripts/migrate_links.py livros/nome-do-livro --dry-run

# Executar alterações
python scripts/migrate_links.py livros/nome-do-livro
```
Atualiza caminhos: `../imagens/` → `../../_imagens/livro/`

### 3. Normalizar Frontmatter
```powershell
# Validar arquivos
python scripts/normalize_frontmatter.py livros/nome-do-livro --validate

# Corrigir frontmatter
python scripts/normalize_frontmatter.py livros/nome-do-livro --fix
```
Converte navegação inline para YAML padronizado.

### 4. Validar Links
```powershell
python scripts/validate_links.py livros/nome-do-livro
```
Verifica links quebrados, imagens ausentes, referências inválidas.

### 5. Extrair PDFs
```powershell
# Arquivo único
python scripts/extract_pdf.py caminho/para/arquivo.pdf

# Múltiplos arquivos
python scripts/extract_multiple.py pasta/com/pdfs/
```

## 📝 Padrão de Frontmatter

Todos os 269 arquivos seguem este padrão YAML:

```yaml
---
title: "Título do Arquivo"
book: "tormenta20-core" ou "herois-arton"
chapter: "nome-do-diretorio-capitulo"
navigation:
  previous: "arquivo-anterior.md"  # ou null
  next: "proximo-arquivo.md"       # ou null
  up: "README.md"
---
```

## 🎯 Padrões de Nomenclatura

- **Arquivos:** kebab-case com prefixo numérico (`01-humano.md`)
- **Diretórios:** kebab-case com prefixo numérico (`03-racas/`)
- **Imagens:** kebab-case descritivo (`humanos-vallen-drikka.png`)
- **Alt-text:** Sempre com "Descrição: " (`![Descrição: Vallen e Drikka](...)`)

## 📚 Livros Planejados

1. ✅ **Tormenta 20 - Livro Básico** (75% completo)
2. ✅ **Heróis de Arton** (100% completo)
3. ⏳ **Panteão** (planejado)
4. ⏳ **Ameaças de Arton** (planejado)
5. ⏳ **Reinos de Arton** (planejado)

## 🚀 Como Contribuir

1. Siga os padrões documentados em [EXTRACTION_GUIDE.md](EXTRACTION_GUIDE.md)
2. Use os scripts em `scripts/` para automação
3. Valide frontmatter e links antes de commit
4. Mantenha estrutura: `livros/nome-do-livro/NN-capitulo/`
5. Imagens em `livros/_imagens/nome-do-livro/`

## 📖 Documentação

- [EXTRACTION_GUIDE.md](EXTRACTION_GUIDE.md) - Guia completo de extração e conversão (28KB)
- [CHECKLIST.md](CHECKLIST.md) - Checklist de tarefas
- [extraction_config.json](extraction_config.json) - Configuração de extração
- [extraction_report.txt](extraction_report.txt) - Relatório de extração

## ⚖️ Licença

Este projeto é uma conversão educacional do sistema Tormenta 20. Todos os direitos de conteúdo pertencem à Jambô Editora.

---

**Última atualização:** Sessão 6 - Reorganização multi-livro completada  
**Arquivos processados:** 269 markdown files (100% com frontmatter YAML)  
**Links atualizados:** 42 arquivos modificados (40 imagens + 19 referências)

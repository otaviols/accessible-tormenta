# Contexto do Projeto: accessible-tormenta

> **Arquivo de referência para IA/Copilot:** Leia este arquivo ao iniciar novos chats para entender completamente o projeto, seus padrões e fluxo de trabalho.

---

## 📖 O Que é Este Projeto?

**accessible-tormenta** é um projeto de conversão de livros do RPG **Tormenta 20** (sistema brasileiro publicado pela Jambô Editora) de PDF para **Markdown acessível** para leitores de tela (NVDA, JAWS).

### Objetivo Principal
Converter livros oficiais mantendo **100% de fidelidade ao texto original**, com navegação estruturada e descrições completas de imagens.

### Status Atual
- ✅ **2 livros** migrados para estrutura multi-livro
- ✅ **269 arquivos** Markdown (~3.7MB, ~632 páginas)
- ✅ **100% dos arquivos** com frontmatter YAML padronizado
- ✅ **7 scripts** de automação criados
- ✅ **0 erros** na validação final

### Livros Disponíveis
1. **Tormenta 20 - Livro Básico** (`livros/tormenta20-core/`) - 75% completo
   - 135 arquivos: 17 raças, 14 classes, 186 magias, 79 criaturas
2. **Heróis de Arton** (`livros/herois-arton/`) - 100% completo
   - 134 arquivos: 5 raças, classe Treinador, 36 distinções, 30 origens

### Livros Planejados
- Panteão
- Ameaças de Arton
- Reinos de Arton

---

## 🏗️ Estrutura Multi-Livro

```
accessible-tormenta/
├── PROJECT_CONTEXT.md           ← VOCÊ ESTÁ AQUI
├── EXTRACTION_GUIDE.md          ← Guia detalhado (28KB) com templates
├── README.md                    ← Índice geral multi-livro
├── REORGANIZACAO_COMPLETA.md    ← Relatório de migração
│
├── livros/                      ← Estrutura principal
│   ├── tormenta20-core/         ← Livro Básico (135 arquivos)
│   │   ├── README.md            ← Índice do livro
│   │   ├── PROGRESS.md          ← Tracking de conversão
│   │   ├── 01-introducao/       ← Capítulo numerado 01-99
│   │   │   ├── README.md        ← Índice do capítulo
│   │   │   ├── 01-o-que-e-tormenta20.md
│   │   │   ├── 02-termos-importantes.md
│   │   │   └── ...
│   │   ├── 02-criacao-personagens/
│   │   ├── 03-racas/
│   │   └── ...
│   │
│   ├── herois-arton/            ← Suplemento (134 arquivos)
│   │   ├── README.md
│   │   ├── PROGRESS.md
│   │   ├── 01-campeoes-arton/
│   │   ├── 02-distincoes/
│   │   └── ...
│   │
│   └── _imagens/                ← Imagens centralizadas
│       ├── tormenta20-core/     ← Por livro
│       │   ├── racas/
│       │   ├── classes/
│       │   └── ...
│       ├── herois-arton/
│       └── comuns/              ← Logos, divisores compartilhados
│
├── scripts/                     ← Ferramentas de automação
│   ├── new_book_scaffold.py     ← Cria estrutura de novo livro
│   ├── migrate_links.py         ← Atualiza caminhos de imagens/links
│   ├── normalize_frontmatter.py ← Padroniza YAML frontmatter
│   ├── validate_links.py        ← Valida links quebrados
│   ├── extract_pdf.py           ← Extrai texto/imagens de PDFs
│   ├── extract_multiple.py      ← Extração em lote
│   └── analyze_cap4.py          ← Análise de capítulos
│
└── Pdf files/                   ← PDFs originais (fonte)
```

**Princípio:** Cada livro é **independente e auto-contido**.

---

## ⚙️ Padrões Obrigatórios

### 1. YAML Frontmatter (100% dos arquivos)

**TODO arquivo .md DEVE ter este frontmatter:**

```yaml
---
title: "Título Legível com Acentos"
book: "slug-do-livro"
chapter: "01-nome-capitulo"
navigation:
  previous: "arquivo-anterior.md"  # ou null se primeiro
  next: "proximo-arquivo.md"       # ou null se último
  up: "README.md"                  # sempre para README do capítulo
---
```

**Campos opcionais:** `section`, `page`, `tags`, `circle`, `school`

### 2. Nomenclatura de Arquivos

**Formato:** `NN-nome-descritivo.md`

- **Prefixo numérico:** 2 dígitos (`01-` até `99-`)
- **Nome:** kebab-case (lowercase, hífens)
- **Sem acentos** no nome do arquivo (mas permitido no `title`)
- **README.md:** sempre maiúsculo para índices

**Exemplos válidos:**
- ✅ `01-humano.md`
- ✅ `23-treinador.md`
- ✅ `origem-15-refugiado.md`
- ✅ `var-alquimista.md`
- ✅ `README.md`

**Exemplos inválidos:**
- ❌ `Humano.md` (sem prefixo, uppercase)
- ❌ `5-poderes.md` (1 dígito apenas)
- ❌ `01_druida.md` (underscore)
- ❌ `variante-alquimista.md` (deveria ser `var-alquimista.md`)

### 3. Nomenclatura de Diretórios

**Formato:** `NN-nome-capitulo/`

- Prefixo numérico 2 dígitos
- kebab-case, sem acentos
- Sempre termina com `/`

**Exemplos:**
- ✅ `01-introducao/`
- ✅ `03-racas/`
- ✅ `12-herois-arton/`

### 4. Alt-Text de Imagens (CRÍTICO)

**Formato obrigatório:**

```markdown
![Descrição: {descrição detalhada objetiva}](caminho-relativo.png)
```

**SEMPRE começar com "Descrição:"** para consistência de screen readers.

**Exemplo completo:**
```markdown
![Descrição: Ilustração de um guerreiro humano vestindo armadura completa de 
placas metálicas prateadas, segurando uma espada longa na mão direita e um 
escudo redondo com emblema de leão dourado na esquerda, em pose de combate 
defensiva com pernas afastadas](../../_imagens/tormenta20-core/guerreiro-combatente.png)
```

**Caminho de imagens:**
- De arquivo em capítulo: `../../_imagens/nome-livro/imagem.png`
- De README de capítulo: `../../_imagens/nome-livro/imagem.png`
- De README de livro: `../_imagens/nome-livro/imagem.png`

### 5. Formatação de Conteúdo

- ✅ **Markdown puro** - ZERO HTML tags permitidas
- ✅ **Transcrição literal** - NUNCA resumir ou parafrasear
- ✅ `##` para seções, `###` para subseções
- ✅ `-` para listas não ordenadas, `1.` para ordenadas
- ✅ `>` para blockquotes/citações
- ✅ Tabelas em formato Markdown

**Exemplo de tabela:**
```markdown
| Atributo | Bônus |
|----------|-------|
| Força | +2 |
| Destreza | +1 |
```

---

## 🔄 Workflow de Conversão (6 Fases)

### Fase 1: Extração de PDF

```powershell
python scripts/extract_pdf.py "Pdf files/livro.pdf" "extracted/nome-livro/"
```

**Saída:**
- `full_text.txt` - Texto completo extraído
- `tables_info.txt` - Informações de tabelas
- `images_info.txt` - Metadados de imagens
- `extracted_content.json` - Dados estruturados

### Fase 2: Análise de Estrutura

1. Ler `full_text.txt`
2. Identificar limites de capítulos/seções
3. Mapear intervalos de páginas
4. Identificar padrões de tabelas e blocos especiais

### Fase 3: Criar Scaffold

```powershell
python scripts/new_book_scaffold.py "nome-livro" "Título Completo do Livro"
```

**Cria:**
- Diretório `livros/nome-livro/`
- README.md e PROGRESS.md
- 10 capítulos padrão (editar conforme necessário)

### Fase 4: Conversão Manual (FASE CRÍTICA)

**ATENÇÃO:** Esta é a fase mais importante!

1. **Copiar texto LITERALMENTE** do PDF extraído
   - ❌ NÃO resumir
   - ❌ NÃO parafrasear
   - ✅ Copiar palavra por palavra

2. **Converter para Markdown:**
   - Listas → `- item` ou `1. item`
   - Tabelas → formato Markdown
   - Citações → `> texto`
   - Títulos → `##` / `###`

3. **Adicionar frontmatter YAML** em CADA arquivo

4. **Descrever TODAS as imagens** com alt-text detalhado

5. **Calcular caminhos relativos** para imagens

### Fase 5: Migração de Links

```powershell
# Visualizar mudanças (dry-run)
python scripts/migrate_links.py livros/nome-livro --dry-run

# Aplicar mudanças
python scripts/migrate_links.py livros/nome-livro
```

**O que faz:**
- Atualiza `../imagens/` → `../../_imagens/livro/`
- Corrige referências a arquivos renomeados
- Relatório estatístico completo

### Fase 6: Validação

```powershell
# 1. Validar frontmatter
python scripts/normalize_frontmatter.py livros/nome-livro --validate

# 2. Corrigir frontmatter (se necessário)
python scripts/normalize_frontmatter.py livros/nome-livro --fix

# 3. Validar links
python scripts/validate_links.py livros/nome-livro
```

**Relatório:** `link_report.txt` com links quebrados e arquivos órfãos

---

## 🎯 Princípios Críticos (LEIA COM ATENÇÃO)

### 1. Transcrição Literal Obrigatória
- ✅ Copiar texto **palavra por palavra** do PDF
- ❌ NUNCA resumir ou parafrasear
- ❌ NUNCA omitir partes do texto
- ✅ Preservar formatação original (negrito, itálico, listas)

**Por quê?** Este é um projeto de **acessibilidade**, não de resumo. Usuários de screen readers precisam do texto completo e original.

### 2. Acessibilidade em Primeiro Lugar
- ✅ TODO conteúdo deve funcionar com NVDA/JAWS
- ✅ Navegação completa (previous/next/up) em todos os arquivos
- ✅ Alt-text descritivo em TODAS as imagens
- ✅ Estrutura de headings lógica (`##` → `###`)

### 3. Markdown Puro
- ✅ 100% Markdown válido
- ❌ ZERO tags HTML (`<div>`, `<span>`, `<img>`)
- ✅ Compatível com Git, GitHub, editores Markdown

### 4. Frontmatter 100%
- ✅ TODO arquivo .md tem YAML frontmatter
- ✅ Campos obrigatórios: `title`, `book`, `chapter`, `navigation`
- ✅ Campos opcionais onde aplicável: `section`, `page`, `tags`

### 5. Zero Erros Tolerados
- ✅ Validar SEMPRE com scripts antes de commit
- ✅ Corrigir todos os links quebrados
- ✅ Verificar todas as imagens existem
- ✅ Confirmar 100% dos arquivos com frontmatter válido

---

## 🛠️ Scripts Disponíveis

### Criação de Estrutura

**`new_book_scaffold.py`** - Gera estrutura completa de novo livro
```powershell
python scripts/new_book_scaffold.py "nome-livro" "Título do Livro"
```

### Migração e Atualização

**`migrate_links.py`** - Atualiza caminhos de imagens e links
```powershell
python scripts/migrate_links.py livros/nome-livro [--dry-run]
```

**`normalize_frontmatter.py`** - Padroniza YAML frontmatter
```powershell
python scripts/normalize_frontmatter.py livros/nome-livro [--validate|--fix]
```

### Validação

**`validate_links.py`** - Detecta links quebrados e arquivos órfãos
```powershell
python scripts/validate_links.py livros/nome-livro
```

### Extração de PDFs

**`extract_pdf.py`** - Extrai texto/imagens de um PDF
```powershell
python scripts/extract_pdf.py "arquivo.pdf" "destino/"
```

**`extract_multiple.py`** - Extração em lote
```powershell
python scripts/extract_multiple.py "pasta-com-pdfs/"
```

---

## 📚 Documentação Detalhada

Para informações completas, consulte:

- **[EXTRACTION_GUIDE.md](EXTRACTION_GUIDE.md)** (28KB) - Guia completo com:
  - Templates detalhados (raça, classe, distinção, magia, origem)
  - Convenções de formatação específicas
  - Processo passo-a-passo de extração
  - Checklist para novos livros
  - Erros comuns e como evitá-los

- **[README.md](README.md)** - Índice geral multi-livro com estatísticas

- **[REORGANIZACAO_COMPLETA.md](REORGANIZACAO_COMPLETA.md)** - Relatório da migração multi-livro

---

## ❌ Erros Comuns (NÃO FAZER)

### 1. Resumir ao Invés de Transcrever
```markdown
❌ ERRADO: "O humano tem +2 em um atributo"
✅ CORRETO: [texto literal completo do PDF com toda a descrição]
```

### 2. Usar HTML
```markdown
❌ ERRADO: <img src="imagem.png" alt="Guerreiro">
✅ CORRETO: ![Descrição: Guerreiro em armadura...](../../_imagens/livro/imagem.png)
```

### 3. Alt-text Vago
```markdown
❌ ERRADO: ![Imagem de guerreiro](imagem.png)
✅ CORRETO: ![Descrição: Guerreiro humano vestindo armadura de placas, 
segurando espada longa...](../../_imagens/livro/imagem.png)
```

### 4. Frontmatter Incompleto ou Ausente
```markdown
❌ ERRADO: Arquivo sem frontmatter ou com campos faltando
✅ CORRETO: Todos os campos obrigatórios presentes e válidos
```

### 5. Nomenclatura Incorreta
```markdown
❌ ERRADO: Humano.md, 5-poderes.md, variante_alquimista.md
✅ CORRETO: 01-humano.md, 05-poderes.md, var-alquimista.md
```

---

## 🚀 Quick Start para Novo Livro

```powershell
# 1. Extrair PDF
python scripts/extract_pdf.py "Pdf files/novo-livro.pdf" "extracted/novo-livro/"

# 2. Criar estrutura
python scripts/new_book_scaffold.py "novo-livro" "Título do Novo Livro"

# 3. Converter conteúdo manualmente (LITERAL!)
# - Ler extracted/novo-livro/full_text.txt
# - Criar arquivos .md em livros/novo-livro/NN-capitulo/
# - Adicionar frontmatter YAML
# - Descrever imagens com alt-text

# 4. Migrar links
python scripts/migrate_links.py livros/novo-livro --dry-run
python scripts/migrate_links.py livros/novo-livro

# 5. Validar tudo
python scripts/normalize_frontmatter.py livros/novo-livro --validate
python scripts/validate_links.py livros/novo-livro

# 6. Corrigir erros e re-validar até 0 erros
```

---

## 📞 Resumo para IA/Copilot

**Ao trabalhar neste projeto:**

1. ✅ **SEMPRE transcrever literalmente** - nunca resumir
2. ✅ **SEMPRE usar Markdown puro** - zero HTML
3. ✅ **SEMPRE adicionar frontmatter YAML** - 100% dos arquivos
4. ✅ **SEMPRE descrever imagens** - "Descrição: ..." detalhado
5. ✅ **SEMPRE validar** - use os scripts antes de finalizar
6. ✅ **SEMPRE seguir nomenclatura** - `NN-nome-kebab-case.md`
7. ✅ **SEMPRE consultar EXTRACTION_GUIDE.md** para templates e detalhes

**Projeto:** Acessibilidade para RPG Tormenta 20  
**Formato:** Markdown multi-livro com navegação estruturada  
**Objetivo:** 100% fidelidade ao original + screen reader friendly  
**Status:** 269 arquivos, 2 livros, 0 erros ✅

---

**Última atualização:** Janeiro 2026 - Reorganização multi-livro completa

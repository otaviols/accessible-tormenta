# Guia de Extração e Padrões - Projeto Tormenta 20 Acessível

> **Documento de referência para o GitHub Copilot e colaboradores**  
> Explica o objetivo, estrutura e padrões do projeto de conversão de livros de Tormenta 20 para Markdown acessível

---

## 🎯 Objetivo do Projeto

Este projeto converte livros do sistema **Tormenta 20** (RPG de mesa brasileiro) de PDF para **Markdown acessível**, com foco em:

- ✅ **Acessibilidade total** para leitores de tela (NVDA, JAWS, etc.)
- ✅ **Navegação estruturada** com links internos e hierarquia clara
- ✅ **Fidelidade ao conteúdo** original (transcrição literal, não resumo)
- ✅ **Organização multi-livro** para suportar livro básico + suplementos
- ✅ **Markdown puro** sem HTML, compatível com Git/GitHub

---

## 📁 Estrutura de Diretórios

### Estrutura Geral do Projeto

```
accessible-tormenta/
├── README.md                      # Índice principal com lista de todos os livros
├── EXTRACTION_GUIDE.md            # Este documento (padrões e referência)
├── livros/                        # Todos os livros convertidos
│   ├── tormenta20-core/           # Livro básico oficial
│   ├── herois-arton/              # Suplemento "Heróis de Arton"
│   ├── ameacas-tormenta/          # (futuro) Suplemento "Ameaças da Tormenta"
│   └── _imagens/                  # Imagens compartilhadas entre livros
│       ├── tormenta20-core/       # Imagens específicas do livro básico
│       ├── herois-arton/          # Imagens específicas de Heróis
│       └── comuns/                # Logos, divisores, etc.
├── scripts/                       # Scripts Python de automação
│   ├── extract_pdf.py             # Extração de PDF para texto
│   ├── validate_links.py          # Validação de links internos
│   ├── normalize_frontmatter.py   # Padronização de YAML
│   ├── migrate_links.py           # Migração de caminhos
│   └── new_book_scaffold.py       # Scaffold para novos livros
├── extracted/                     # Arquivos temporários de extração
│   ├── tormenta20-core/
│   └── herois-arton-cap4/
└── Pdf files/                     # PDFs originais (não versionados)
```

---

### Estrutura de Um Livro Individual

```
livros/{nome-do-livro}/
├── README.md                      # Índice do livro com navegação para capítulos
├── PROGRESS.md                    # Tracking de progresso da conversão
├── 01-introducao/                 # Capítulos sempre numerados 01-99
│   ├── README.md                  # Índice do capítulo
│   ├── 01-primeiro-topico.md
│   ├── 02-segundo-topico.md
│   └── ...
├── 02-criacao-personagens/
├── 03-racas/
├── 04-classes/
└── ...

Nota: Cada livro é independente e autocontido.
```

---

## 📝 Convenções de Nomenclatura

### Nomes de Arquivos

**REGRAS OBRIGATÓRIAS:**

1. **Kebab-case minúsculo**: `01-nome-do-arquivo.md`
2. **Sempre prefixo numérico**: `01-` a `99-` (dois dígitos)
3. **Sem acentos ou caracteres especiais** nos nomes de arquivo
4. **README.md** maiúsculo para índices de capítulos/livros
5. **Descritivo mas conciso**: máximo 3-5 palavras

**Exemplos corretos:**
- `01-humano.md`
- `05-poderes-combate.md`
- `23-treinador.md`
- `var-01-alquimista.md` (variantes com prefixo `var-`)
- `origem-15-refugiado.md` (origens com prefixo `origem-`)

**Exemplos INCORRETOS:**
- `Humano.md` (sem número, maiúscula)
- `5-poderes.md` (número com 1 dígito)
- `variante_alquimista.md` (underscore, sem número)
- `origem-refugiado-de-hongari.md` (muito específico no nome)

---

### Nomes de Diretórios

**REGRAS:**

1. **Kebab-case minúsculo**: `01-nome-diretorio/`
2. **Prefixo numérico de dois dígitos**: `01-` a `99-`
3. **Sem acentos**: `03-racas/` não `03-raças/`
4. **Plural quando apropriado**: `04-classes/`, `05-pericias-poderes/`

**Prefixos especiais:**
- `_imagens/` - Diretório de recursos compartilhados (prefixo `_`)
- `extracted/` - Dados temporários (sem prefixo numérico)
- `scripts/` - Ferramentas (sem prefixo numérico)

---

## 🔖 Padrões de Frontmatter YAML

### Template Padrão (OBRIGATÓRIO em todos .md)

```yaml
---
title: "Título Completo da Seção"
book: "nome-do-livro"
chapter: "01-introducao"
section: "primeiro-topico"
navigation:
  previous: "00-capitulo-anterior.md"
  next: "02-proximo-topico.md"
  up: "README.md"
---
```

**Campos obrigatórios:**
- `title`: Título legível para humanos (com acentos, espaços)
- `book`: Slug do livro (`tormenta20-core`, `herois-arton`)
- `chapter`: Nome do diretório do capítulo
- `navigation.previous`: Link relativo para arquivo anterior (ou `null`)
- `navigation.next`: Link relativo para próximo (ou `null`)
- `navigation.up`: Link para README do capítulo

**Campos opcionais:**
- `section`: Identificador da seção atual
- `page`: Número da página no PDF original
- `tags`: Array de tags para busca

---

### Exemplos por Tipo de Conteúdo

#### Raça

```yaml
---
title: "Humano"
book: "tormenta20-core"
chapter: "03-racas"
section: "humano"
page: 52
tags: ["raça", "comum", "versátil"]
navigation:
  previous: "README.md"
  next: "02-anao.md"
  up: "README.md"
---
```

#### Classe

```yaml
---
title: "Arcanista"
book: "tormenta20-core"
chapter: "04-classes"
section: "arcanista"
page: 84
tags: ["classe", "conjurador", "mana"]
navigation:
  previous: "README.md"
  next: "02-barbaro.md"
  up: "README.md"
---
```

#### Distinção (Heróis de Arton)

```yaml
---
title: "Aeronauta Goblin"
book: "herois-arton"
chapter: "02-distincoes"
section: "aeronauta-goblin"
page: 115
tags: ["distinção", "goblin", "tecnologia"]
navigation:
  previous: "README.md"
  next: "02-algoz-da-tormenta.md"
  up: "README.md"
---
```

#### Magia

```yaml
---
title: "Bola de Fogo"
book: "tormenta20-core"
chapter: "09-magia"
section: "3-circulo-af"
circle: 3
school: "evocação"
tags: ["magia", "arcana", "fogo", "dano"]
navigation:
  previous: "03-descricao-magias-3-circulo-af.md#area-escorregadia"
  next: "03-descricao-magias-3-circulo-af.md#clarividencia"
  up: "README.md"
---
```

---

## 📄 Templates de Conteúdo

### Template: Raça

```markdown
---
title: "Nome da Raça"
book: "nome-livro"
chapter: "03-racas"
section: "slug-raca"
navigation:
  previous: "arquivo-anterior.md"
  next: "proximo-arquivo.md"
  up: "README.md"
---

# Nome da Raça

> "Citação icônica ou frase de efeito que representa a raça"
> 
> — Atribuição da citação (personagem famoso, ditado popular, etc.)

---

## Descrição

[Parágrafo introdutório sobre a raça: origem, aparência geral, papel em Arton]

![Descrição: Descrição detalhada da ilustração mostrando características visuais da raça](../../_imagens/nome-livro/raca-exemplo.png)

[Mais parágrafos descritivos sobre características físicas, culturais, etc.]

---

## Cultura e Sociedade

[Informações sobre como a raça vive, se organiza, tradições, valores]

### [Subtópico Cultural, ex: "Estrutura Social"]

[Conteúdo]

### [Outro Subtópico, ex: "Religião e Crenças"]

[Conteúdo]

---

## Relações com Outras Raças

[Como a raça se relaciona com outras raças de Arton]

---

## Nomes Típicos

[Exemplos de nomes masculinos, femininos, sobrenomes, etc.]

**Exemplos:** Nome1, Nome2, Nome3, Nome4, Nome5

---

## Habilidades de Raça

### Modificadores de Atributo

Você recebe +2 em um atributo e +1 em outro OU +1 em três atributos diferentes (escolha sua distribuição).

### Nome da Habilidade Racial

**Descrição completa da habilidade com regras mecânicas.**

### Outra Habilidade Racial

**Descrição completa.**

[Continue para todas as habilidades raciais]

---

## Jogando com [Nome da Raça]

### Pontos Fortes

- **Característica 1:** Explicação
- **Característica 2:** Explicação
- **Característica 3:** Explicação

### Pontos Fracos

- **Limitação 1:** Explicação
- **Limitação 2:** Explicação

### Dicas de Interpretação

[Sugestões para interpretar personagens desta raça]

### Combinações Recomendadas

**Classes:** [Lista de classes que combinam bem]
**Origens:** [Lista de origens temáticas]
**Deuses:** [Deuses comumente cultuados]

---

## [Nome da Raça] Famosos

**Nome do Personagem**, **Outro Personagem**, **Mais Um Personagem**

---

[← Anterior: Raça Anterior](arquivo.md) | [Próximo: Próxima Raça →](arquivo.md)
```

---

### Template: Classe

```markdown
---
title: "Nome da Classe"
book: "nome-livro"
chapter: "04-classes"
section: "slug-classe"
navigation:
  previous: "arquivo-anterior.md"
  next: "proximo-arquivo.md"
  up: "README.md"
---

# Nome da Classe

> "Citação icônica representando a filosofia da classe"
> 
> — Atribuição

---

## Descrição

[Parágrafo introdutório: o que é a classe, seu papel, temática]

![Descrição: Descrição da ilustração mostrando um membro típico da classe](../../_imagens/nome-livro/classe-exemplo.png)

[Mais parágrafos sobre a natureza da classe, origens, papel no mundo]

---

## [Seção Temática Específica da Classe]

[Conteúdo específico - varia por classe]
[Ex: "O Código do Paladino", "Escolas de Magia", "Estilos de Combate"]

---

## [Nome da Classe] Famosos

**Personagem 1**, **Personagem 2**, **Personagem 3**

---

## Características de Classe

### Pontos de Vida

Você começa com **[valor]** pontos de vida (+ modificador de Constituição) e ganha **[valor]** PV (+ mod. Con) por nível.

### Pontos de Mana

**[valor]** PM por nível (+ modificador de [atributo]).

### Perícias

Escolha **[número]** entre [lista de perícias] (mais [perícias da inteligência] se aplicável).

### Proficiências

Armas [lista]. Armaduras [lista]. [Outros itens se aplicável].

---

## Habilidades de Classe

### Nome da Habilidade (ex: "Magia", "Fúria", etc.)

[Descrição completa da habilidade central da classe]

### Habilidade Especial de [Nível]º Nível

[Descrição]

[Continue para todas habilidades por nível: 1, 2, 3, 5, 10, 14, 17, 20]

---

## Poderes de [Nome da Classe]

[Introdução sobre como funcionam os poderes desta classe]

### Nome do Poder 1

**[Pré-requisitos se houver]**

[Descrição completa com regras mecânicas, custos, durações, etc.]

### Nome do Poder 2

**[Pré-requisitos]**

[Descrição]

[Continue para todos os poderes da classe, geralmente 20-30 poderes]

---

[← Anterior: Classe Anterior](arquivo.md) | [Próximo: Próxima Classe →](arquivo.md)
```

---

### Template: Distinção (Heróis de Arton)

```markdown
---
title: "Nome da Distinção"
book: "herois-arton"
chapter: "02-distincoes"
section: "slug-distincao"
navigation:
  previous: "arquivo-anterior.md"
  next: "proximo-arquivo.md"
  up: "README.md"
---

# Nome da Distinção

[Parágrafo introdutório explicando o que é a distinção, seu propósito, origens]

[Parágrafos adicionais com contexto histórico, temático, cultural]

---

## Admissão

[Lista de requisitos para obter a distinção]

**Exemplo:**
- Ser treinado em [perícia]
- Ter pelo menos [atributo] 13
- [Outros requisitos narrativos ou mecânicos]

---

## Marca da Distinção

### Nome da Habilidade Central

[Descrição completa da habilidade que define a distinção - mecânica principal]

**Regras:**
[Detalhes de funcionamento]

---

## Poderes da Distinção

### Nome do Poder 1

**Pré-requisito:** [Se houver]

[Descrição completa com mecânicas]

### Nome do Poder 2

**Pré-requisito:** [Se houver]

[Descrição]

[Continue para todos os poderes exclusivos da distinção, geralmente 5-8 poderes]

---

[← Anterior: Distinção Anterior](arquivo.md) | [Próximo: Próxima Distinção →](arquivo.md)
```

---

### Template: Magia

```markdown
---
title: "Nome da Magia"
book: "nome-livro"
chapter: "09-magia"
section: "circulo-faixa"
circle: [número]
school: "escola-de-magia"
navigation:
  previous: "#magia-anterior"
  next: "#proxima-magia"
  up: "README.md"
---

### Nome da Magia

**[Escola] [Círculo]**

**Execução:** [padrão/completa/livre/reação/movimento]  
**Alcance:** [toque/curto/médio/longo/pessoal/etc.]  
**Alvo/Área:** [descrição do alvo ou área]  
**Duração:** [instantânea/cena/sustentada/etc.]  
**Resistência:** [Fortitude/Reflexos/Vontade/nenhuma]

[Descrição completa do efeito da magia em linguagem clara e precisa]

[Se houver: tabelas de progressão, exemplos, notas especiais]

**[Se aplicável] Verdadeiro:** [Descrição da versão aprimorada +5 PM]

**[Se aplicável] Discente (Arcanista X):** [Modificação específica de poder]

---
```

**NOTA:** Magias geralmente ficam em um único arquivo grande organizado por círculo e ordem alfabética, não em arquivos individuais. Use âncoras `#` para navegação interna.

---

## 🔄 Processo de Extração (Passo a Passo)

### Fase 1: Extração do PDF

1. **Obter o PDF oficial** do livro (comprado legalmente)
2. **Colocar em** `Pdf files/nome-do-livro.pdf`
3. **Executar extração:**
   ```powershell
   python scripts/extract_pdf.py "Pdf files/nome-do-livro.pdf" extracted/nome-do-livro/
   ```
4. **Resultado:** Cria `extracted/nome-do-livro/full_text.txt` com texto completo

---

### Fase 2: Análise da Estrutura

1. **Ler `full_text.txt`** e identificar:
   - Marcadores de página (ex: "PÁGINA 15")
   - Títulos de capítulos (geralmente em MAIÚSCULAS)
   - Títulos de seções
   - Início/fim de tabelas
   - Blocos de conteúdo distintos (raças, classes, magias, etc.)

2. **Criar mapeamento** de páginas para seções:
   ```
   Páginas 10-45: Capítulo 1 - Raças
     Página 10-13: Humano
     Página 14-17: Anão
     ...
   Páginas 46-103: Capítulo 2 - Classes
     ...
   ```

3. **Identificar padrões de formatação:**
   - Como tabelas são representadas
   - Como títulos/subtítulos aparecem
   - Quebras de seção, boxes especiais, etc.

---

### Fase 3: Criação da Estrutura de Diretórios

1. **Criar diretório do livro:**
   ```powershell
   python scripts/new_book_scaffold.py "nome-do-livro" "Título Completo do Livro"
   ```

2. **Criar subpastas de capítulos** baseado no mapeamento:
   ```powershell
   mkdir livros/nome-do-livro/01-introducao
   mkdir livros/nome-do-livro/02-racas
   # etc.
   ```

---

### Fase 4: Conversão de Conteúdo

**CRÍTICO: Transcrição Literal, NÃO Resumo**

- ✅ **CORRETO:** Copiar texto exatamente como está no PDF
- ❌ **ERRADO:** Resumir, parafrasear, omitir detalhes

**Processo por arquivo:**

1. **Localizar intervalo de linhas** em `full_text.txt` (ex: linhas 1500-1800 = Humano)
2. **Copiar texto literal** respeitando:
   - Parágrafos originais
   - Listas (converter para markdown `- item` ou `1. item`)
   - Tabelas (converter para markdown tables)
   - Blocos de citação (usar `> texto`)
   - Títulos/subtítulos (converter para `##`, `###`)

3. **Adicionar frontmatter YAML** no topo
4. **Adicionar navegação** no rodapé (se não usar frontmatter)
5. **Verificar formatação:**
   - Quebras de linha corretas
   - Tabelas alinhadas
   - Links internos funcionando

**Exemplo de conversão de tabela:**

**FONTE (full_text.txt):**
```
Nível  Bônus  Habilidades
1      +1     Magia, Poder
2      +2     Poder
3      +3     Poder, Característica
```

**CONVERTIDO (markdown):**
```markdown
| Nível | Bônus | Habilidades |
|-------|-------|-------------|
| 1 | +1 | Magia, Poder |
| 2 | +2 | Poder |
| 3 | +3 | Poder, Característica |
```

---

### Fase 5: Revisão e Validação

1. **Executar validador de links:**
   ```powershell
   python scripts/validate_links.py livros/nome-do-livro/
   ```

2. **Verificar:**
   - Todos os arquivos têm frontmatter
   - Navegação funciona (previous/next)
   - Imagens têm alt-text descritivo
   - Tabelas renderizam corretamente
   - Não há `[TODO]` ou `[PENDENTE]` no texto

3. **Atualizar PROGRESS.md** do livro com estatísticas

---

### Fase 6: Integração Final

1. **Atualizar README.md** do livro com índice completo
2. **Atualizar README.md** raiz do projeto adicionando novo livro
3. **Commit no Git** com mensagem descritiva:
   ```
   git add livros/nome-do-livro/
   git commit -m "feat: adiciona livro 'Nome Completo' (XXX páginas, YY arquivos)"
   ```

---

## 🎨 Padrões de Imagens

### Convenções de Alt-Text

**Template obrigatório:**
```markdown
![Descrição: [descrição detalhada e objetiva da imagem]](caminho/imagem.png)
```

**SEMPRE começar com "Descrição:"** para consistência com leitores de tela.

**Exemplos de alt-text descritivo:**

✅ **BOM:**
```markdown
![Descrição: Ilustração de um guerreiro humano vestindo armadura completa de placas, segurando uma espada longa e um escudo com emblema de leão, em pose de combate defensiva](../../_imagens/tormenta20-core/guerreiro-combatente.png)
```

❌ **RUIM:**
```markdown
![Guerreiro](imagem.png)
```

❌ **RUIM:**
```markdown
![](../../_imagens/guerreiro.png)
```

---

### Organização de Imagens

**Estrutura:**
```
livros/_imagens/
├── tormenta20-core/
│   ├── racas/
│   │   ├── humano-vallen-drikka.png
│   │   ├── anao-golinda-ingram.png
│   │   └── ...
│   ├── classes/
│   │   ├── arcanista-conjurador.png
│   │   └── ...
│   └── logo-tormenta20.png
├── herois-arton/
│   ├── racas/
│   ├── distincoes/
│   └── ...
└── comuns/
    ├── divisor-ornamental.png
    └── icone-dado-d20.png
```

**Nomenclatura:**
- Kebab-case: `nome-descritivo.png`
- Prefixo com contexto: `raca-humano.png`, `classe-guerreiro.png`
- Sem espaços, sem acentos
- Formato PNG preferencial (suporta transparência)

---

## 📊 Arquivos de Tracking

### PROGRESS.md (em cada livro)

**Template:**

```markdown
# Progresso de Conversão - [Nome do Livro]

**Última Atualização:** DD/MM/AAAA

---

## Status Geral

**Capítulos Completos:** X de Y (ZZ%)

**Estatísticas:**
- 📁 Arquivos criados: XXX arquivos markdown
- 📝 Volume total: ~X.XMB
- 🎯 Páginas documentadas: XXX de XXX (100%)
- ✅ Status: [EM ANDAMENTO / COMPLETO]

---

## Status por Capítulo

### ✅ Capítulo 1: Nome do Capítulo (100% COMPLETO)
- XX arquivos criados
- Páginas XX-YY do PDF
- Conteúdo: [resumo]

### ⏳ Capítulo 2: Nome do Capítulo (50% PENDENTE)
- XX de YY arquivos criados
- Páginas XX-YY do PDF
- Pendente: [o que falta]

---

## Histórico de Sessões

### Sessão 1 - DD/MM/AAAA
- **Conteúdo:** [O que foi feito]
- **Arquivos:** [quantidade e tipos]
- **Páginas:** [intervalo processado]

---
```

---

## 🛠️ Scripts de Automação

### extract_pdf.py

**Uso:**
```powershell
python scripts/extract_pdf.py "caminho/arquivo.pdf" "extracted/nome-livro/"
```

**Saída:**
- `full_text.txt` - Texto completo extraído
- `tables_info.txt` - Informações sobre tabelas
- `images_info.txt` - Lista de imagens e posições
- `extracted_content.json` - Metadados estruturados

---

### validate_links.py

**Uso:**
```powershell
python scripts/validate_links.py livros/nome-livro/
```

**Verifica:**
- Links internos quebrados (`[texto](arquivo-inexistente.md)`)
- Imagens faltando
- Âncoras (#seção) inválidas
- Frontmatter malformado

---

### normalize_frontmatter.py

**Uso:**
```powershell
python scripts/normalize_frontmatter.py livros/nome-livro/ --fix
```

**Corrige:**
- Adiciona frontmatter YAML ausente
- Padroniza campos (`title`, `book`, `chapter`, etc.)
- Converte navegação inline para YAML

---

### new_book_scaffold.py

**Uso:**
```powershell
python scripts/new_book_scaffold.py "nome-do-livro" "Título Completo do Livro"
```

**Cria:**
- Diretório `livros/nome-do-livro/`
- `README.md` inicial
- `PROGRESS.md` com template
- Estrutura de subpastas comum (01-introducao, etc.)

---

## ✅ Checklist para Novos Livros

### Antes de Começar

- [ ] PDF adquirido legalmente e colocado em `Pdf files/`
- [ ] Nome do livro definido (slug kebab-case)
- [ ] Título completo do livro confirmado
- [ ] Número total de páginas conhecido

---

### Fase 1: Extração

- [ ] Executar `extract_pdf.py` com sucesso
- [ ] Verificar `full_text.txt` gerado e legível
- [ ] Analisar estrutura do texto extraído
- [ ] Criar mapeamento páginas → seções

---

### Fase 2: Scaffold

- [ ] Executar `new_book_scaffold.py`
- [ ] Criar todas as subpastas de capítulos necessárias
- [ ] Copiar imagens para `livros/_imagens/nome-livro/`

---

### Fase 3: Conversão

- [ ] Criar README.md de cada capítulo
- [ ] Converter seções para arquivos .md com frontmatter
- [ ] Adicionar alt-text em todas as imagens
- [ ] Converter todas as tabelas para markdown
- [ ] Manter formatação de listas, citações, etc.
- [ ] **Garantir transcrição literal, não resumo**

---

### Fase 4: Navegação

- [ ] Adicionar navegação previous/next em todos arquivos
- [ ] Configurar links "up" para READMEs
- [ ] Testar todos os links internos
- [ ] Adicionar links do capítulo no README do livro

---

### Fase 5: Validação

- [ ] Executar `validate_links.py` sem erros
- [ ] Executar `normalize_frontmatter.py` sem warnings
- [ ] Revisar amostra de arquivos manualmente
- [ ] Testar navegação em leitor de tela (se possível)

---

### Fase 6: Documentação

- [ ] Atualizar PROGRESS.md do livro (status 100%)
- [ ] Adicionar livro ao README.md raiz
- [ ] Documentar decisões específicas (se houve casos especiais)
- [ ] Commit final no Git

---

## 🚨 Erros Comuns a Evitar

### ❌ Resumir ao invés de transcrever

**ERRADO:**
```markdown
A classe Guerreiro é boa em combate e ganha bônus.
```

**CORRETO:**
```markdown
O guerreiro é o mestre das armas e armaduras. Seja um soldado, um mercenário, 
um gladiador ou um simples brigão de taverna, o guerreiro está sempre pronto 
para o combate. Guerreiros são proficientes com todas as armas e armaduras...
[texto completo literal do PDF]
```

---

### ❌ Usar HTML ao invés de Markdown

**ERRADO:**
```markdown
<h2>Título</h2>
<p>Parágrafo</p>
<ul><li>Item</li></ul>
```

**CORRETO:**
```markdown
## Título

Parágrafo

- Item
```

---

### ❌ Links relativos incorretos

**ERRADO:**
```markdown
![Imagem](imagens/guerreiro.png)  # Caminho errado
```

**CORRETO:**
```markdown
![Descrição: ...](../../_imagens/tormenta20-core/classes/guerreiro.png)
```

---

### ❌ Frontmatter ausente ou incompleto

**ERRADO:**
```markdown
# Título do Arquivo

Conteúdo...
```

**CORRETO:**
```markdown
---
title: "Título do Arquivo"
book: "nome-livro"
chapter: "01-introducao"
navigation:
  previous: null
  next: "02-proximo.md"
  up: "README.md"
---

# Título do Arquivo

Conteúdo...
```

---

### ❌ Alt-text vago ou ausente

**ERRADO:**
```markdown
![](imagem.png)
![Guerreiro](imagem.png)
```

**CORRETO:**
```markdown
![Descrição: Ilustração de um guerreiro humano usando armadura de placas 
completa, capacete com penacho vermelho, empunhando espada longa e escudo 
redondo com brasão de dragão dourado, em pose heroica de combate](caminho.png)
```

---

## 📖 Referências e Exemplos

### Exemplo Completo: Arquivo de Raça

Ver: `livros/tormenta20-core/03-racas/01-humano.md`

### Exemplo Completo: Arquivo de Classe

Ver: `livros/tormenta20-core/04-classes/01-arcanista.md`

### Exemplo Completo: Arquivo de Distinção

Ver: `livros/herois-arton/02-distincoes/01-aeronauta-goblin.md`

### Exemplo de README de Capítulo

Ver: `livros/tormenta20-core/03-racas/README.md`

### Exemplo de README de Livro

Ver: `livros/tormenta20-core/README.md`

---

## 🎯 Princípios Finais

1. **Acessibilidade primeiro** - Tudo deve funcionar perfeitamente em leitores de tela
2. **Fidelidade ao original** - Transcrição literal, não interpretação
3. **Markdown puro** - Sem HTML, sem plugins, compatível com qualquer renderizador
4. **Navegação intuitiva** - Links claros, hierarquia lógica, breadcrumbs funcionais
5. **Consistência** - Seguir os padrões deste guia em 100% dos arquivos
6. **Documentação viva** - Atualizar este guia quando novos padrões surgirem

---

**Última atualização:** 10/01/2026  
**Versão:** 1.0  
**Mantido por:** Projeto Tormenta 20 Acessível

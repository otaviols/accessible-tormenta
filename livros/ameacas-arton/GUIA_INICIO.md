# GUIA RÁPIDO: Como Começar a Conversão

**📍 Você está aqui:** Estrutura criada, pronto para conversão manual

---

## ✅ O Que Já Foi Feito

1. ✅ PDF extraído → `extracted/ameacas-arton/`
2. ✅ Estrutura de pastas criada → `livros/ameacas-arton/`
3. ✅ README.md e PROGRESS.md criados
4. ✅ 8 capítulos com READMEs iniciais
5. ✅ Pasta de imagens criada
6. ✅ Plano detalhado documentado → `PLANO_AMEACAS_ARTON.md`

---

## 🎯 Próximo Passo: Fase 1 - Estabelecer Padrões

### O Que Fazer Agora

**Tarefa:** Converter a seção de referência (Fichas de Criaturas)

**Localização no PDF:** Páginas 12-14  
**Localização no texto:** `extracted/ameacas-arton/full_text.txt` ~linha 500-700

---

## 📋 Passo a Passo para Primeira Conversão

### 1. Abrir arquivos necessários

```powershell
# Abrir o texto extraído
code extracted/ameacas-arton/full_text.txt

# Abrir o PROGRESS.md para ir atualizando
code livros/ameacas-arton/PROGRESS.md

# Abrir exemplo de livro completo (referência)
code livros/dragao-brasil/01-racas/00-introducao.md
```

### 2. Localizar conteúdo no full_text.txt

Busque por: `PÁGINA 12` ou `Fichas de Criaturas`

### 3. Copiar texto literal

**IMPORTANTE:** Copiar EXATAMENTE como está, palavra por palavra

### 4. Criar arquivo markdown

```powershell
# Criar o arquivo
code livros/ameacas-arton/01-ameacas/00-fichas-criaturas.md
```

### 5. Adicionar estrutura básica

```markdown
---
title: "Fichas de Criaturas"
book: "ameacas-arton"
chapter: "01-ameacas"
navigation:
  previous: "README.md"
  next: "00-tipos-criaturas.md"
  up: "README.md"
---

# Fichas de Criaturas

[COLAR TEXTO LITERAL AQUI]
```

### 6. Converter formatação

- Negrito: `**texto**`
- Itálico: `*texto*`
- Listas: `-` ou `1.`
- Tabelas: formato Markdown table
- Headers: `##` para seções, `###` para subseções

### 7. Adicionar imagens (se houver)

```markdown
![Descrição: [descrição detalhada objetiva da imagem]](../../_imagens/ameacas-arton/introducao/imagem.png)
```

### 8. Atualizar PROGRESS.md

Marcar a seção como ✅ COMPLETA

---

## 🎨 Template de Ficha de Criatura

Para quando começar a converter criaturas (Fase 1.3):

```markdown
---
title: "Nome da Criatura"
book: "ameacas-arton"
chapter: "01-ameacas"
section: "mascotes-familiares"
navigation:
  previous: "criatura-anterior.md"
  next: "proxima-criatura.md"
  up: "README.md"
---

# Nome da Criatura

![Descrição: [Descrição detalhada: aparência física, pose, características 
distintivas, cores, tamanho aparente, contexto do cenário se relevante]](../../_imagens/ameacas-arton/mascotes-familiares/criatura.png)

[Texto introdutório literal do PDF]

## Atributos

| Atributo | Valor |
|----------|-------|
| ND | X |
| Tamanho e Tipo | Médio Animal |
| Deslocamento | 9m |
| PV | XX |
| CA | XX (armadura natural) |

## Perícias

[Lista de perícias]

## Resistências e Imunidades

[Se houver]

## Sentidos

Percepção +X, visão no escuro 18m

## Idiomas

[Idiomas que fala/entende]

## Habilidades

### Nome da Habilidade

[Descrição literal]

## Ações

### Ação Padrão

[Descrição literal]

### Ação Extra

[Se houver]

## Reações

[Se houver]

## Tesouro

[Se houver]
```

---

## 🔍 Exemplo Real (referência)

Veja um arquivo já convertido de outro livro:

**Arquivo:** `livros/dragao-brasil/01-racas/01-bugbear.md`

Este arquivo mostra:
- ✅ Frontmatter correto
- ✅ Formatação adequada
- ✅ Estrutura de navegação
- ✅ Descrição de imagem (alt-text)

---

## ⚠️ Regras de Ouro

### 1. SEMPRE LITERAL
❌ "O bugbear é uma criatura forte"  
✅ "Bugbears são goblinoides grandes e peludos conhecidos por sua força bruta"

### 2. ALT-TEXT DESCRITIVO
❌ `![Bogum](imagem.png)`  
✅ `![Descrição: Ilustração de um bogum, pequena criatura peluda azul com olhos grandes e expressivos, orelhas pontiagudas, sentado em posição amigável](imagem.png)`

### 3. FRONTMATTER COMPLETO
Todos os arquivos DEVEM ter:
- title
- book
- chapter
- navigation (previous, next, up)

### 4. MARKDOWN PURO
❌ `<div class="stat-block">` (HTML)  
✅ `## Atributos` (Markdown)

### 5. NAVEGAÇÃO CONSISTENTE
- previous: arquivo anterior na sequência (ou null se primeiro)
- next: próximo arquivo (ou null se último)
- up: sempre README.md do capítulo

---

## 📊 Checklist da Primeira Conversão

Use esta checklist para sua primeira seção:

- [ ] Texto copiado literalmente (100% igual ao PDF)
- [ ] Frontmatter YAML presente e correto
- [ ] Formatação Markdown aplicada (negrito, itálico, listas)
- [ ] Tabelas convertidas para formato Markdown
- [ ] Imagens com alt-text começando com "Descrição:"
- [ ] Links de navegação (previous/next/up) corretos
- [ ] Headers hierárquicos (H1 título, H2 seções, H3 subseções)
- [ ] Arquivo salvo com extensão .md
- [ ] PROGRESS.md atualizado

---

## 🆘 Dúvidas Comuns

### Como saber se copiei literalmente?
Compare lado a lado com o `full_text.txt`. Deve ser palavra por palavra.

### E se o texto extraído estiver quebrado/malformatado?
Isso pode acontecer com tabelas ou textos em colunas. Nesse caso:
1. Tente reorganizar manualmente mantendo o conteúdo
2. Consulte o PDF original se necessário
3. NUNCA invente ou resuma - transcreva o que está lá

### Como descrever imagens de criaturas?
Seja objetivo e específico:
- Aparência física (tamanho, forma, cores)
- Características distintivas (chifres, asas, garras)
- Pose ou ação (em pé, agachado, atacando)
- Contexto mínimo (cenário se relevante)

### Quantas imagens devo descrever por vez?
Faça conforme conseguir, mas priorize qualidade sobre quantidade. Uma descrição bem feita é melhor que 10 genéricas.

---

## 🎯 Meta da Primeira Sessão

**Objetivo mínimo:**
- [ ] 1 seção convertida completamente
- [ ] Template de ficha estabelecido
- [ ] Padrão de alt-text definido
- [ ] PROGRESS.md atualizado

**Objetivo ideal:**
- [ ] 3 seções de referência convertidas
- [ ] 1 categoria pequena iniciada (ex: Mascotes)
- [ ] 3-5 criaturas convertidas com fichas completas

---

## 📞 Onde Pedir Ajuda

1. **Plano completo:** `PLANO_AMEACAS_ARTON.md`
2. **Contexto do projeto:** `PROJECT_CONTEXT.md`
3. **Guia de extração:** `EXTRACTION_GUIDE.md`
4. **Exemplos prontos:** `livros/dragao-brasil/` e `livros/herois-arton/`

---

## 🚀 Comando para Começar

```powershell
# Abra os 3 arquivos principais
code extracted/ameacas-arton/full_text.txt
code livros/ameacas-arton/PROGRESS.md
code livros/ameacas-arton/01-ameacas/00-fichas-criaturas.md

# Busque "PÁGINA 12" no full_text.txt
# Comece a copiar e converter!
```

---

**BOA CONVERSÃO! 🎲📚**

Lembre-se: qualidade e literalidade > velocidade  
Cada arquivo bem feito ajuda milhares de jogadores com leitores de tela!

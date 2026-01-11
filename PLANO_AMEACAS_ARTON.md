# PLANO DE EXECUÇÃO: Ameaças de Arton

**CRIADO EM:** 10/01/2026  
**STATUS:** ✅ FASE INICIAL COMPLETA - Pronto para conversão manual

---

## ✅ ETAPAS CONCLUÍDAS

### 1. Extração do PDF ✅
- **PDF:** `AmeacasdeArtonv1017112023.pdf` (436 páginas)
- **Resultado:**
  - ✅ `extracted/ameacas-arton/full_text.txt` (29.349 linhas)
  - ✅ `extracted/ameacas-arton/table_of_contents.txt` (413 seções)
  - ✅ `extracted/ameacas-arton/tables_info.txt` (283 tabelas)
  - ✅ `extracted/ameacas-arton/images_info.txt` (1869 imagens)
  - ✅ `extracted/ameacas-arton/extracted_content.json`

### 2. Análise da Estrutura ✅
- **Capítulos identificados:** 3 principais + 4 apêndices
- **Maior desafio:** Capítulo 1 (~361 páginas, ~300-350 criaturas)
- **Organização:** 30+ categorias temáticas de criaturas

### 3. Criação do Scaffold ✅
- **Diretórios criados:** 8 pastas de capítulos
- **Arquivos criados:** 10 arquivos markdown
  - README.md principal
  - PROGRESS.md
  - 8 README.md de capítulos
- **Pasta de imagens:** `livros/_imagens/ameacas-arton/` criada

---

## 📋 PRÓXIMAS ETAPAS (Conversão Manual)

### FASE 1: Estabelecer Padrões 🔴

**Objetivo:** Criar templates e estabelecer padrão de conversão

#### Ação 1.1: Converter seção de referência
- Ler páginas 12-17 do PDF (`full_text.txt` linhas ~500-900)
- Converter manualmente:
  - "Fichas de Criaturas" (como ler fichas)
  - "Tipos de Criaturas" (classificação)
  - "Habilidades Gerais" (poderes comuns)
- Criar arquivos:
  - `01-ameacas/00-fichas-criaturas.md`
  - `01-ameacas/00-tipos-criaturas.md`
  - `01-ameacas/00-habilidades-gerais.md`

#### Ação 1.2: Criar template de ficha de criatura
Estabelecer formato padrão:
```markdown
---
title: "Nome da Criatura"
book: "ameacas-arton"
chapter: "01-ameacas"
section: "categoria-tematica"
navigation:
  previous: "criatura-anterior.md"
  next: "proxima-criatura.md"
  up: "README.md"
---

# Nome da Criatura

![Descrição: [descrição detalhada]](../../_imagens/ameacas-arton/categoria/criatura.png)

[Texto literal do PDF]

## Atributos

| Atributo | Valor |
|----------|-------|
| ND | X |
| Tamanho | Médio/Grande/etc |
| Tipo | Animal/Morto-vivo/etc |

[continuar com formato consistente]
```

#### Ação 1.3: Converter primeira categoria completa (teste)
- Escolher categoria pequena: **"Mascotes & Familiares"** (8 criaturas)
- Converter todas literalmente
- Descrever todas as imagens
- Validar padrão estabelecido

---

### FASE 2: Conversão por Categoria 🔴

**Objetivo:** Converter sistematicamente todas as categorias de criaturas

#### Ordem sugerida (do menor para o maior):

1. **Mascotes & Familiares** (8 criaturas) - TESTE INICIAL ✅ fase 1
2. **Capangas & Bandoleiros** (7 criaturas)
3. **Brutos & Indomáveis** (9 criaturas)
4. **Áreas de Tormenta** (~12 criaturas)
5. **Gnolls** (7 criaturas)
6. **Kobolds** (9 criaturas)
7. **Culto de Aharadak** (7-8 criaturas + regras)
8. **Igreja de Arsenal** (6 criaturas)
9. **Igreja de Kallyadranoch** (6 criaturas)
10. **Império de Jade** (8 criaturas)
11. **Império de Tauron** (8 criaturas)
12. **Duyshidakk** (9 criaturas)
13. **Piratas & Pistoleiros** (10 criaturas)
14. **Povos-Trovão** (4 criaturas + totens)
15. **Puristas** (8 criaturas + regras)
16. **Reino dos Mortos** (8 criaturas)
17. **Reinos de Moreania** (6 criaturas + regras)
18. **Sszzaazitas** (11 criaturas)
19. **Trolls Nobres** (8 criaturas)
20. **Uivantes** (9 criaturas)
21. **Sanguinárias** (7 criaturas)
22. **Ermos** (9 criaturas)
23. **Masmorras** (11 criaturas)
24. **Sob as Ondas** (10 criaturas)
25. **Dragões** (7 tipos + regras)
26. **Golens** (11 tipos + regras)
27. **Elementais** (13 criaturas)
28. **Mortos-Vivos** (10 criaturas)
29. **Mundo Perdido** (10 dinossauros)
30. **Montarias** (22 montarias) - CATEGORIA GRANDE
31. **Novos Perigos** (perigos ambientais)
32. **Chefe Final** (regras especiais)

**Para cada categoria:**
1. Criar subpasta em `01-ameacas/categoria-nome/`
2. Criar README.md da categoria
3. Converter cada criatura em arquivo separado
4. Descrever todas as imagens
5. Converter tabelas para Markdown
6. Adicionar frontmatter YAML completo
7. Validar navegação (previous/next/up)
8. **Atualizar PROGRESS.md** após cada categoria

---

### FASE 3: Capítulos 2 e 3 🔴

#### Capítulo 2: Regras Avançadas
- Páginas 372-389 (18 páginas)
- 2 arquivos principais:
  - `02-regras-avancadas/01-regras-adicionais.md`
  - `02-regras-avancadas/02-manual-criacao.md`
- Conversão mais simples (texto + algumas tabelas)

#### Capítulo 3: Bazar Monstruoso
- Páginas 390-407 (18 páginas)
- 8 arquivos:
  - Armas, armaduras, itens gerais, itens superiores
  - Recursos naturais
  - 6 itens mágicos (1 arquivo cada)
  - 2 artefatos (1 arquivo cada)
  - 7 magias (1 arquivo ou arquivo consolidado)

---

### FASE 4: Apêndices 🔴

#### Apêndice A: Raças e Parceiros
- 1 arquivo: lista organizada
- Conversão rápida (2 páginas)

#### Apêndice B: Alfabético
- 1 arquivo: índice alfabético com links
- Criar links para cada criatura convertida
- Automatizável parcialmente com script

#### Apêndice C: Por ND
- 1 arquivo: criaturas agrupadas por ND
- Criar links para cada criatura
- Automatizável parcialmente

#### Apêndice D: Encontros Aleatórios
- 19 arquivos (11 terrenos + 8 regiões)
- Tabelas de encontros aleatórios
- Conversão sistemática de tabelas

---

### FASE 5: Introdução 🔴

**Por que no final?** Porque requer contexto do livro completo

- Páginas 6-9 (4 páginas)
- 2 arquivos:
  - `00-introducao/01-sonho-monstruoso.md` (prefácio narrativo)
  - `00-introducao/02-mundo-ameacador.md` (conceitos de ameaças)

---

### FASE 6: Validação Final 🔴

#### 6.1: Executar Scripts de Validação
```powershell
# Validar frontmatter
python scripts/normalize_frontmatter.py livros/ameacas-arton --validate

# Corrigir se necessário
python scripts/normalize_frontmatter.py livros/ameacas-arton --fix

# Validar links
python scripts/validate_links.py livros/ameacas-arton

# Migrar links (se necessário)
python scripts/migrate_links.py livros/ameacas-arton --dry-run
python scripts/migrate_links.py livros/ameacas-arton
```

#### 6.2: Checklist de Qualidade
- [ ] 100% dos arquivos têm frontmatter YAML válido
- [ ] Todos os links internos funcionam
- [ ] Todas as imagens têm alt-text começando com "Descrição:"
- [ ] Navegação previous/next/up completa
- [ ] Nenhum arquivo órfão
- [ ] 0 erros de validação
- [ ] PROGRESS.md reflete 100% de conclusão

#### 6.3: Integração com Projeto Principal
- [ ] Atualizar `README.md` principal do projeto
- [ ] Adicionar estatísticas de Ameaças de Arton
- [ ] Criar PR ou commit final

---

## 📊 ESTIMATIVAS

### Volume de Trabalho
- **Arquivos a criar:** ~400 arquivos markdown
- **Imagens a descrever:** 1869 imagens (média 4 por página)
- **Tabelas a converter:** 283 tabelas
- **Páginas a documentar:** 436 páginas

### Tempo Estimado (baseado em livros anteriores)
- **Dragão Brasil:** 75 arquivos (~40 horas)
- **Heróis de Arton:** 136 arquivos (~70 horas)
- **Ameaças de Arton:** ~400 arquivos (**estimativa: 150-200 horas**)

### Por Fase
1. **Fase 1 (Padrões):** 8-10 horas
2. **Fase 2 (Categorias):** 100-120 horas
3. **Fase 3 (Cap 2-3):** 15-20 horas
4. **Fase 4 (Apêndices):** 15-20 horas
5. **Fase 5 (Introdução):** 2-3 horas
6. **Fase 6 (Validação):** 5-8 horas

---

## 🎯 CHECKPOINTS DE PROGRESSO

### Checkpoint 1: Padrão Estabelecido (Meta: Fase 1 completa)
- [ ] Template de criatura criado e validado
- [ ] Categoria "Mascotes" 100% convertida
- [ ] Padrão de alt-text definido
- [ ] PROGRESS.md atualizado

### Checkpoint 2: 25% de Conversão (Meta: 7-8 categorias)
- [ ] ~100 arquivos criados
- [ ] ~7-8 categorias completas
- [ ] PROGRESS.md: 25%

### Checkpoint 3: 50% de Conversão (Meta: 15-16 categorias)
- [ ] ~200 arquivos criados
- [ ] ~15-16 categorias completas
- [ ] PROGRESS.md: 50%

### Checkpoint 4: 75% de Conversão (Meta: 23-25 categorias)
- [ ] ~300 arquivos criados
- [ ] Todas categorias pequenas/médias completas
- [ ] PROGRESS.md: 75%

### Checkpoint 5: Cap 1 Completo (Meta: Todas 32 categorias)
- [ ] ~350-380 arquivos criados
- [ ] Capítulo 1 100% completo
- [ ] PROGRESS.md: 85%

### Checkpoint 6: Livro Completo
- [ ] ~400 arquivos criados
- [ ] Todos capítulos e apêndices completos
- [ ] PROGRESS.md: 100%
- [ ] 0 erros de validação

---

## 🔑 REGRAS CRÍTICAS DE ACESSIBILIDADE

### Alt-Text de Imagens
**SEMPRE começar com "Descrição:"**

**Exemplo ruim:**
```markdown
![Dragão vermelho](imagem.png)
```

**Exemplo BOM:**
```markdown
![Descrição: Ilustração de um dragão vermelho adulto em pose ameaçadora, 
com asas abertas medindo aproximadamente 15 metros de envergadura, escamas 
vermelhas brilhantes reflexivas à luz, garras afiadas curvadas, olhos 
amarelos flamejantes e intensos, soltando chamas alaranjadas pela boca 
aberta sobre um campo de batalha rochoso](../../_imagens/ameacas-arton/dragoes/dragao-vermelho.png)
```

### Descrições Objetivas
- ✅ Aparência física detalhada
- ✅ Pose e posicionamento
- ✅ Cores, texturas, tamanho relativo
- ✅ Elementos de cenário quando relevantes
- ❌ Interpretações subjetivas ("parece malvado")
- ❌ Emoções não visíveis ("está com raiva")
- ❌ Suposições sobre intenções

### Fichas de Criaturas
**Estrutura consistente:**
1. Título (H1)
2. Imagem principal com alt-text
3. Texto introdutório literal
4. Tabela de atributos (ND, Tamanho, Tipo, etc)
5. Estatísticas de combate
6. Habilidades especiais
7. Ações
8. Reações (se houver)
9. Táticas (se houver)
10. Tesouro/Recompensas (se houver)

### Frontmatter YAML
**Campos obrigatórios:**
```yaml
---
title: "Título com Acentos"
book: "ameacas-arton"
chapter: "01-ameacas"
section: "categoria-especifica"  # opcional mas recomendado
navigation:
  previous: "arquivo-anterior.md"  # ou null
  next: "proximo-arquivo.md"       # ou null
  up: "README.md"
---
```

### Transcrição Literal
- ❌ NUNCA resumir
- ❌ NUNCA parafrasear
- ❌ NUNCA omitir informações
- ✅ Copiar palavra por palavra
- ✅ Manter formatação original
- ✅ Preservar todas as regras e números

---

## 📁 ESTRUTURA DE PASTAS PARA IMAGENS

```
livros/_imagens/ameacas-arton/
├── introducao/
├── areas-tormenta/
├── brutos-indomaveis/
├── capangas-bandoleiros/
├── culto-aharadak/
├── dragoes/
├── duyshidakk/
├── elementais/
├── ermos/
├── gnolls/
├── golens/
├── igreja-arsenal/
├── igreja-kallyadranoch/
├── imperio-jade/
├── imperio-tauron/
├── kobolds/
├── mascotes-familiares/
├── masmorras/
├── montarias/
├── mortos-vivos/
├── mundo-perdido/
├── piratas-pistoleiros/
├── povos-trovao/
├── puristas/
├── reino-mortos/
├── reinos-moreania/
├── sanguinarias/
├── sob-ondas/
├── sszzaazitas/
├── trolls-nobres/
├── uivantes/
├── perigos/
├── chefe-final/
├── bazar-monstruoso/
└── apendices/
```

---

## 🚀 COMO COMEÇAR

### Passo 1: Abrir arquivos de referência
```powershell
# Abrir texto extraído
code extracted/ameacas-arton/full_text.txt

# Abrir TOC
code extracted/ameacas-arton/table_of_contents.txt

# Abrir PROGRESS.md
code livros/ameacas-arton/PROGRESS.md
```

### Passo 2: Localizar primeira seção no full_text.txt
- Buscar por "PÁGINA 12" (início das Fichas de Criaturas)
- Ou buscar por "Fichas de Criaturas"

### Passo 3: Converter primeira seção
- Copiar texto literal
- Criar arquivo markdown
- Adicionar frontmatter
- Converter formatação
- Descrever imagens

### Passo 4: Atualizar progresso
- Editar PROGRESS.md
- Marcar seção como completa
- Atualizar estatísticas

### Passo 5: Repetir sistematicamente
- Seguir ordem do plano
- Manter padrões consistentes
- Validar periodicamente

---

## 📞 SUPORTE E REFERÊNCIAS

### Documentação do Projeto
- `PROJECT_CONTEXT.md` - Visão geral e objetivos
- `EXTRACTION_GUIDE.md` - Guia completo de extração
- `livros/dragao-brasil/` - Exemplo de livro completo
- `livros/herois-arton/` - Exemplo de livro completo

### Scripts Disponíveis
- `scripts/extract_pdf.py` - ✅ Usado
- `scripts/validate_links.py` - Usar na Fase 6
- `scripts/normalize_frontmatter.py` - Usar na Fase 6
- `scripts/migrate_links.py` - Usar se necessário

---

**FIM DO PLANO**

✅ Estrutura inicial completa  
🔴 Pronto para iniciar conversão manual (Fase 1)

**Última atualização:** 10/01/2026

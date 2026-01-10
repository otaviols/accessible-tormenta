# Plano de Conversão - Dragão Brasil

## ✅ Etapas Concluídas

### 1. Extração do PDF ✓
- **Arquivo:** `Pdf files/Dragao-Brasil-compilado-Tormenta-20.pdf`
- **Destino:** `extracted/dragao-brasil/`
- **Resultados:**
  - 180 páginas extraídas
  - 125 seções no índice
  - 55 tabelas detectadas
  - 1552 imagens identificadas
- **Arquivos gerados:**
  - `full_text.txt` - Texto completo com marcadores de página
  - `table_of_contents.txt` - Índice estruturado
  - `tables_info.txt` - Metadados de tabelas
  - `images_info.txt` - Localização de imagens
  - `extracted_content.json` - Dados estruturados completos

### 2. Análise da Estrutura ✓
- **Organização identificada:** Conteúdo temático (não por edições)
- **Capítulos mapeados:**
  1. Raças (36 novas + 10 variantes + artigos especiais)
  2. Classes (15 classes com variantes)
  3. Origens (condicionais e regionais)
  4. Perícias e Poderes (6 categorias + devoções)
  5. Distinções (17 organizações)
  6. Equipamentos (mundanos, superiores, mágicos, artefatos)
  7. Magias (novas magias)
  8. Regras (opcionais e variantes)

### 3. Configuração Atualizada ✓
- Entrada adicionada em `extraction_config.json`
- Status: `in-progress`
- Metadados completos registrados

### 4. Estrutura de Diretórios ✓
- **Localização:** `livros/dragao-brasil/`
- **Capítulos criados:**
  - `01-racas/`
  - `02-classes/`
  - `03-origens/`
  - `04-pericias-poderes/`
  - `05-distincoes/`
  - `06-equipamentos/`
  - `07-magias/`
  - `08-regras/`
- **Imagens:** `livros/_imagens/dragao-brasil/`
- **READMEs:** Todos os capítulos com frontmatter e estrutura completa

---

## 📋 Próximas Etapas (Conversão Manual)

### Fase 1: Preparação
- [ ] Revisar `extracted/dragao-brasil/full_text.txt` para mapear conteúdo exato
- [ ] Identificar páginas de início/fim de cada seção
- [ ] Planejar divisão de arquivos (estimativa: ~150 arquivos)

### Fase 2: Conversão por Capítulo

#### Capítulo 01 - Raças (~40 arquivos estimados)
- [ ] `01-costumes-raciais.md` - Artigo sobre bons e maus costumes
- [ ] `02-golens-despertos.md` - Artigo sobre golens
- [ ] `03-suraggel-mundo-deuses.md` - Artigo sobre heranças divinas
- [ ] `var-01-anao-svartalfheim.md` a `var-10-aberrante-ghanor.md` - Variantes
- [ ] `01-bugbear.md` a `28-yidishan.md` - 36 raças novas

#### Capítulo 02 - Classes (~20 arquivos estimados)
- [ ] `01-arcanista.md` a `15-samurai.md` - 15 classes
- [ ] `perfis-personagem.md` - Toques finais

#### Capítulo 03 - Origens (~10 arquivos estimados)
- [ ] `01-origens-condicionais.md`
- [ ] `02-origens-regionais.md`
- [ ] Arquivos individuais conforme necessário

#### Capítulo 04 - Perícias e Poderes (~30 arquivos estimados)
- [ ] `01-pericias.md`
- [ ] `02-poderes-gerais.md`
- [ ] `03-poderes-combate.md`
- [ ] `04-poderes-destino.md`
- [ ] `05-poderes-magia.md`
- [ ] `06-poderes-concedidos.md`
- [ ] `07-escola-combate.md`
- [ ] `08-novas-devocoes.md`
- [ ] `09-remanescencia.md`

#### Capítulo 05 - Distinções (~20 arquivos estimados)
- [ ] `01-distincoes-em-jogo.md` - Artigo introdutório
- [ ] `02-admissao.md` - Processo de admissão
- [ ] `03-usando-distincoes.md` - Mecânicas
- [ ] `01-aeronauta-goblin.md` a `18-xerife-azgher.md` - 18 distinções

#### Capítulo 06 - Equipamentos (~20 arquivos estimados)
- [ ] `01-novas-armas.md`
- [ ] `02-novas-armaduras-escudos.md`
- [ ] `03-itens-gerais.md`
- [ ] `04-itens-superiores.md`
- [ ] `05-materiais-especiais.md`
- [ ] `06-itens-magicos-especificos.md`
- [ ] `07-runas-magicas.md`
- [ ] `08-artefatos.md`

#### Capítulo 07 - Magias (~5 arquivos estimados)
- [ ] Magias organizadas por círculo ou tema

#### Capítulo 08 - Regras (~15 arquivos estimados)
- [ ] `01-idiomas.md`
- [ ] `02-objetivos-heroicos.md`
- [ ] `03-regra-idade.md`
- [ ] `04-desvantagens-gerais.md`
- [ ] `05-favor-sombra.md`
- [ ] `06-overdose-mana.md`
- [ ] `07-persona-non-grata.md`
- [ ] `08-questao-carater.md`
- [ ] `09-regra-alimentacao.md`
- [ ] `10-invocacoes-final-fantasy.md`
- [ ] `11-invocacoes.md`
- [ ] `12-chocobos.md`
- [ ] `13-sumo-sacerdotes.md`
- [ ] `14-tipos-descanso.md`
- [ ] `15-regra-grupos-fim-tempos.md`

### Fase 3: Processamento de Imagens
- [ ] Extrair todas as 1552 imagens do PDF
- [ ] Organizar em `livros/_imagens/dragao-brasil/`
- [ ] Criar subpastas por categoria (racas/, classes/, etc.)
- [ ] Renomear imagens com nomes descritivos

### Fase 4: Validação
- [ ] Executar `python scripts/migrate_links.py livros/dragao-brasil/`
- [ ] Executar `python scripts/normalize_frontmatter.py livros/dragao-brasil/ --validate`
- [ ] Executar `python scripts/validate_links.py livros/dragao-brasil/`
- [ ] Corrigir todos os erros até zero

---

## 📐 Padrões de Conversão (OBRIGATÓRIOS)

### Frontmatter YAML
```yaml
---
title: "Título Legível com Acentos"
book: "dragao-brasil"
chapter: "NN-capitulo"
navigation:
  previous: "arquivo-anterior.md"  # ou null
  next: "proximo-arquivo.md"       # ou null
  up: "README.md"
---
```

### Imagens
```markdown
![Descrição: {30-80 palavras objetivas descrevendo visual completo da imagem, incluindo personagem, pose, equipamento, ambiente e tema}](../../_imagens/dragao-brasil/categoria/imagem.png)
```

### Tabelas
```markdown
| Coluna 1 | Coluna 2 | Coluna 3 |
|----------|----------|----------|
| Valor 1  | Valor 2  | Valor 3  |
```

### Listas
```markdown
- Item não ordenado
  - Subitem (2 espaços de indentação)

1. Item ordenado
2. Segundo item
```

### Ênfase
- **Negrito:** `**termo de jogo**`, `**nome de habilidade**`
- *Itálico:* `*ênfase*` (uso raro)

### Citações/Boxes
```markdown
> "Citação de personagem ou provérbio"
> 
> — Atribuição

> ### Título do Box
> 
> Conteúdo explicativo de regra especial ou contexto.
```

---

## ⚠️ Lembretes Críticos

1. **Transcrição 100% LITERAL** - Nunca resumir, parafrasear ou omitir
2. **Alt-text SEMPRE inicia com "Descrição:"** - Padrão obrigatório
3. **Zero HTML** - Apenas Markdown puro
4. **Frontmatter em TODOS os arquivos** - Sem exceções
5. **Nomenclatura:** `NN-nome-kebab-case.md` (2 dígitos + kebab-case sem acentos)
6. **Validar continuamente** - Executar scripts de validação frequentemente

---

## 📊 Estimativa de Esforço

- **Páginas:** 180
- **Arquivos estimados:** ~150
- **Imagens:** 1552
- **Tabelas:** 55

**Tempo estimado (baseado em Heróis de Arton):**
- Conversão de texto: ~30-40 horas
- Processamento de imagens: ~15-20 horas
- Validação e correções: ~5-10 horas
- **Total:** ~50-70 horas de trabalho

---

## 🎯 Status Atual

**Progresso geral:** 30% (preparação completa, conversão pendente)

- ✅ Extração: 100%
- ✅ Estrutura: 100%
- ⏳ Conversão: 0%
- ⏳ Imagens: 0%
- ⏳ Validação: 0%

**Próximo passo:** Iniciar conversão do Capítulo 01 - Raças, começando pelos artigos especiais.

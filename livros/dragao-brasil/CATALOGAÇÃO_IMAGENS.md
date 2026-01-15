# Catalogação de Imagens - Dragão Brasil

## Status

**Total de imagens no PDF**: 1.552 imagens (segundo images_info.txt)
**Páginas**: 180 páginas  
**Diretório**: `livros/_imagens/dragao-brasil/`  
**Status do diretório**: Vazio (imagens ainda não extraídas do PDF)

---

## Visão Geral

Este documento serve como referência para a futura extração de imagens do PDF "Dragão Brasil". As imagens precisam ser extraídas do PDF original e catalogadas seguindo o padrão definido no [ACCESSIBILITY_GUIDE.md](../../ACCESSIBILITY_GUIDE.md).

### Distribuição de Imagens por Capítulo

Baseado no arquivo [images_info.txt](../../extracted/dragao-brasil/images_info.txt):

| Capítulo | Páginas | Imagens Estimadas | Prioridade |
|----------|---------|-------------------|------------|
| 01 - Raças | 2-19 | ~150 imagens | Média |
| 02 - Classes | 20-48 | ~300 imagens | **Alta** |
| 03 - Origens | 49-60 | ~100 imagens | Média |
| 04 - Deuses | 61-63 | ~30 imagens | Baixa |
| 05 - Distinções | 64-102 | ~350 imagens | Alta |
| 06 - Perícias/Poderes | 106-118 | ~120 imagens | Média |
| 07 - Equipamentos | 119-144 | ~250 imagens | **Alta** |
| 08 - Magias | 145-151 | ~70 imagens | Baixa |
| 09 - Regras | 152-180 | ~180 imagens | Média |

---

## Tipos de Imagens Esperadas

### 1. Personagens e Raças (~150 imagens)
Ilustrações de personagens das novas raças:
- Golens Despertos (diversos chassis)
- Suraggel (22 heritages planares)
- Variantes raciais
- Arte conceitual de personagens

**Padrão de nomenclatura**: `raca-[nome-raca]-[variante].jpg`
- Exemplo: `raca-golem-despertado-chassi-acrobata.jpg`
- Exemplo: `raca-suraggel-heritage-celestial.jpg`

### 2. Classes (~300 imagens)
Maior concentração de imagens do livro:
- Druidas de Aharadak, Tenebra e Arton
- Samurai (classe completa)
- Miragem (classe completa)
- Místico (variantes elementais)
- Poderes de classe ilustrados

**Padrão de nomenclatura**: `classe-[nome-classe]-[conceito].jpg`
- Exemplo: `classe-samurai-katana-ancestral.jpg`
- Exemplo: `classe-druida-aharadak-forma-aberrante.jpg`
- Exemplo: `classe-mistico-elemento-fogo.jpg`

### 3. Origens (~100 imagens)
- Origens regionais de Arton
- Origens de outros mundos
- Locais e cenários

**Padrão de nomenclatura**: `origem-[tipo]-[nome].jpg`
- Exemplo: `origem-regional-estudante-colegio-real.jpg`
- Exemplo: `origem-regional-pescador-khubar.jpg`

### 4. Distinções (~350 imagens)
Uma das maiores seções:
- 19 classes de prestígio
- Habilidades e poderes característicos
- Equipamento temático

**Padrão de nomenclatura**: `distincao-[nome].jpg`
- Exemplo: `distincao-aeronauta-goblin.jpg`
- Exemplo: `distincao-cavaleiro-corvo.jpg`
- Exemplo: `distincao-inquisidor-wynna.jpg`

### 5. Equipamentos (~250 imagens)
Segunda maior seção:
- Novas armas (exóticas, marciais)
- Armaduras e escudos
- Itens mágicos
- Runas e artefatos
- Materiais especiais

**Padrão de nomenclatura**: `equip-[categoria]-[nome].jpg`
- Exemplo: `equip-arma-wakizashi.jpg`
- Exemplo: `equip-arma-balestra.jpg`
- Exemplo: `equip-artefato-[nome].jpg`
- Exemplo: `equip-runa-[tipo].jpg`

### 6. Magias (~70 imagens)
- Efeitos visuais de magias
- Componentes materiais
- Áreas de efeito

**Padrão de nomenclatura**: `magia-[circulo]-[nome].jpg`
- Exemplo: `magia-1-criar-elementos.jpg`
- Exemplo: `magia-3-bola-fogo-tamuraniana.jpg`

### 7. Regras e Mecânicas (~180 imagens)
- Chocobos (destaque especial)
- Invocações de Final Fantasy
- Diagramas de regras
- Tabelas ilustradas

**Padrão de nomenclatura**: `regra-[conceito].jpg`
- Exemplo: `regra-chocobo-amarelo.jpg`
- Exemplo: `regra-invocacao-ifrit.jpg`
- Exemplo: `regra-descanso-diagrama.jpg`

### 8. Imagens Decorativas
- Bordas e divisores
- Símbolos de capítulo
- Arte de fundo

**Padrão de nomenclatura**: `decorativo-[tipo]-[numero].jpg`
- Exemplo: `decorativo-divisor-01.jpg`
- Exemplo: `decorativo-simbolo-capitulo-02.jpg`

---

## Processo de Extração

### Fase 1: Extração do PDF
1. Usar ferramenta de extração de imagens do PDF (pdfimages, Adobe Acrobat, etc.)
2. Organizar imagens por página/seção
3. Identificar e separar por tipo

### Fase 2: Nomenclatura e Organização
1. Renomear seguindo padrões acima
2. Criar subpastas por capítulo:
   ```
   _imagens/dragao-brasil/
   ├── 01-racas/
   ├── 02-classes/
   ├── 03-origens/
   ├── 04-deuses/
   ├── 05-distincoes/
   ├── 06-pericias-poderes/
   ├── 07-equipamentos/
   ├── 08-magias/
   ├── 09-regras/
   └── decorativos/
   ```

### Fase 3: Descrições de Acessibilidade
Para cada imagem, criar alt text descritivo seguindo [ACCESSIBILITY_GUIDE.md](../../ACCESSIBILITY_GUIDE.md):

**Exemplo para personagem:**
```markdown
![Samurai tamurano empunhando katana ancestral. Guerreiro vestindo armadura laqueada vermelha e preta, em postura de guarda. A lâmina brilha com energia mágica azulada.](../../_imagens/dragao-brasil/02-classes/classe-samurai-katana-ancestral.jpg)
```

**Exemplo para equipamento:**
```markdown
![Wakizashi - espada curta tamurana com lâmina ligeiramente curva, guarda circular ornamentada e cabo enrolado em seda preta.](../../_imagens/dragao-brasil/07-equipamentos/equip-arma-wakizashi.jpg)
```

**Exemplo para decorativo:**
```markdown
![Imagem decorativa: divisor de seção com padrão geométrico](../../_imagens/dragao-brasil/decorativos/decorativo-divisor-01.jpg)
```

### Fase 4: Atualização dos Arquivos Markdown
Adicionar referências às imagens nos arquivos markdown existentes, substituindo placeholders ou adicionando onde apropriado.

---

## Priorização

### Prioridade Alta (Fazer primeiro)
1. **Classes** (~300 imagens) - Maior seção, muito visual
2. **Equipamentos** (~250 imagens) - Essencial para referência de jogadores
3. **Distinções** (~350 imagens) - Classes de prestígio importantes

### Prioridade Média
4. **Raças** (~150 imagens)
5. **Origens** (~100 imagens)
6. **Perícias/Poderes** (~120 imagens)
7. **Regras** (~180 imagens) - Especialmente Chocobos e Invocações

### Prioridade Baixa
8. **Magias** (~70 imagens)
9. **Deuses** (~30 imagens)
10. **Decorativas** (variadas)

---

## Checklist de Progresso

- [ ] Extrair imagens do PDF
- [ ] Organizar em subpastas por capítulo
- [ ] Renomear seguindo padrão de nomenclatura
- [ ] Criar descrições alt text para todas as imagens
- [ ] Atualizar arquivos markdown com referências
- [ ] Validar acessibilidade das descrições
- [ ] Revisar qualidade e resolução das imagens
- [ ] Documentar imagens faltantes ou problemáticas

---

## Notas

- As imagens devem ser extraídas em alta qualidade (mínimo 300 DPI quando possível)
- Formato preferencial: JPG para fotos/arte, PNG para diagramas/ícones
- Tamanho máximo por imagem: 2MB (comprimir se necessário)
- Sempre incluir alt text descritivo
- Imagens puramente decorativas devem ser marcadas como tal

---

**Última atualização**: 15 de janeiro de 2026  
**Status**: Aguardando extração de imagens do PDF

# Guia de Acessibilidade - Tormenta20

Este guia estabelece padrões de formatação para garantir que todo o conteúdo de Tormenta20 seja acessível a leitores de tela e outras tecnologias assistivas.

## Índice

1. [Tabelas Acessíveis](#tabelas-acessíveis)
2. [Hierarquia de Cabeçalhos](#hierarquia-de-cabeçalhos)
3. [Formatação de Itens e Descrições](#formatação-de-itens-e-descrições)
4. [Placeholders e Células Vazias](#placeholders-e-células-vazias)
5. [Exemplos Práticos](#exemplos-práticos)

---

## Tabelas Acessíveis

### ✅ Formato Correto

Tabelas devem ter estrutura consistente, com cabeçalhos de seção **fora** da tabela, usando cabeçalhos markdown (H3 ou H4):

```markdown
### Armas Simples

#### Corpo a Corpo — Leves

| Arma | Preço | Dano | Crítico | Alcance | Tipo | Espaços |
|------|-------|------|---------|---------|------|---------|
| Adaga | T$ 2 | 1d4 | 19 | Curto | Perfuração | 1 |
| Espada curta | T$ 10 | 1d6 | 19 | — | Perfuração | 1 |

#### Corpo a Corpo — Uma Mão

| Arma | Preço | Dano | Crítico | Alcance | Tipo | Espaços |
|------|-------|------|---------|---------|------|---------|
| Machado de guerra | T$ 20 | 1d8 | x3 | — | Corte | 1 |
| Maça | T$ 12 | 1d8 | x2 | — | Impacto | 1 |
```

**Por quê?** Leitores de tela identificam o cabeçalho como estrutura de navegação, permitindo que usuários pulem entre seções facilmente.

### ❌ Formato Inacessível

**Nunca** use linhas de tabela como cabeçalhos de seção:

```markdown
### Armas Simples

| Arma | Preço | Dano | Crítico | Alcance | Tipo | Espaços |
|------|-------|------|---------|---------|------|---------|
| **Corpo a Corpo — Leves** |  |  |  |  |  |  |
| Adaga | T$ 2 | 1d4 | 19 | Curto | Perfuração | 1 |
| **Corpo a Corpo — Uma Mão** |  |  |  |  |  |  |
| Machado de guerra | T$ 20 | 1d8 | x3 | — | Corte | 1 |
```

**Problema:** Leitores de tela anunciam isto como uma linha de dados normal, não como cabeçalho de seção. Usuários não conseguem navegar entre categorias.

---

## Hierarquia de Cabeçalhos

### ✅ Estrutura Correta

Siga sempre a hierarquia sem pular níveis:

```markdown
# Nome da Classe (H1)

## Descrição (H2)

### História e Lore (H3)

## Características de Classe (H2)

### Pontos de Vida (H3)

### Pontos de Mana (H3)

## Habilidades de Classe (H2)

### Caminho do Guerreiro (H3)

#### Investida Brutal (H4)

#### Defesa Impenetrável (H4)
```

**Por quê?** Leitores de tela usam a hierarquia para criar um "índice" mental do documento. Pular níveis quebra essa navegação.

### ❌ Hierarquia Incorreta

**Nunca** pule níveis de cabeçalho:

```markdown
# Nome da Classe (H1)

## Descrição (H2)

#### História (H4) ← ERRO: pulou do H2 para H4
```

---

## Formatação de Itens e Descrições

### ✅ Itens com Cabeçalho

Use cabeçalhos (H3 ou H4) para nomes de itens, magias, poderes e habilidades:

```markdown
## Descrição das Armas

### Adaga

Esta faca afiada é usada por muitos habitantes adultos do Reinado, embora seja favorita de ladrões e assassinos, por ser facilmente escondida (fornece **+5 em testes de Ladinagem para ocultá-la**).

### Espada Longa

A arma preferida de cavaleiros e guerreiros. Uma espada longa causa 1d8 pontos de dano e tem crítico 19.
```

**Por quê?** Cabeçalhos aparecem na navegação por estrutura de documentos, permitindo que usuários encontrem rapidamente o item desejado.

### ❌ Itens sem Cabeçalho

**Evite** usar apenas negrito para nomes de itens:

```markdown
## Descrição das Armas

**Adaga.** Esta faca afiada é usada por muitos habitantes adultos do Reinado...

**Espada Longa.** A arma preferida de cavaleiros e guerreiros...
```

**Problema:** Leitores de tela não diferenciam esses itens de texto enfatizado comum. Usuários não conseguem pular entre itens facilmente.

### Exceções

Listas curtas com descrições de uma linha podem usar formato de lista:

```markdown
## Benefícios

- **Ataque Poderoso:** +2 em rolagens de dano corpo a corpo
- **Defesa Sólida:** +1 na Defesa quando usar escudo
- **Reflexos Rápidos:** +2 em testes de Reflexos
```

---

## Placeholders e Células Vazias

### Regras para Tabelas

| Situação | Use | Exemplo |
|----------|-----|---------|
| Não aplicável | `—` (em dash) | Alcance de arma corpo a corpo |
| Valor zero | `0` | Penalidade de armadura acolchoada |
| Célula vazia em cabeçalho de seção | deixar vazio | Linhas de categoria |

### ✅ Exemplos Corretos

```markdown
| Arma | Preço | Dano | Crítico | Alcance | Tipo | Espaços |
|------|-------|------|---------|---------|------|---------|
| Espada curta | T$ 10 | 1d6 | 19 | — | Perfuração | 1 |
| Arco curto | T$ 30 | 1d6 | x3 | Curto | Perfuração | 1 |
| Balas (20) | T$ 20 | — | — | — | — | 1 |
```

```markdown
| Armadura | Preço | Bônus | Penalidade | Espaços |
|----------|-------|-------|------------|---------|
| Acolchoada | T$ 5 | +1 | 0 | 2 |
| Couro batido | T$ 35 | +3 | –1 | 2 |
```

### ❌ Placeholders Incorretos

**Nunca** use `**` como placeholder:

```markdown
| Arma | Preço | Dano | Crítico | Alcance | Tipo | Espaços |
|------|-------|------|---------|---------|------|---------|
| Pistola | T$ 250 | 2d6 | 19/x3 | Curto | Perfuração | 1 |
| Balas (20) | T$ 20 | ** | ** | ** | ** | 1 |
```

**Problema:** `**` é código markdown que pode confundir leitores de tela.

---

## Listas de Propriedades vs. Tabelas

Para equipamentos e itens com muitas propriedades (7+ colunas), use **listas de propriedades** ao invés de tabelas largas.

### ✅ Formato Acessível (Lista de Propriedades)

```markdown
### Espada Longa
**Preço:** T$ 15 | **Dano:** 1d8 | **Crítico:** 19 | **Alcance:** — | **Tipo:** Corte | **Espaços:** 1

A arma preferida de cavaleiros e guerreiros. Uma espada longa causa 1d8 pontos de dano e tem crítico 19.

### Armadura de Couro
**Preço:** T$ 20 | **Defesa:** +2 | **Penalidade:** 0 | **Espaços:** 2

Feita de couro endurecido, esta armadura leve é popular entre aventureiros ágeis.
```

**Por quê?** Cada item tem seu próprio cabeçalho H3, permitindo navegação direta. Propriedades em linha única são mais fáceis de ler em leitores de tela que 7+ colunas de tabela.

### ❌ Formato Menos Acessível (Tabela Larga)

```markdown
| Arma | Preço | Dano | Crítico | Alcance | Tipo | Espaços |
|------|-------|------|---------|---------|------|---------|
| Espada longa | T$ 15 | 1d8 | 19 | — | Corte | 1 |
| Machado | T$ 20 | 1d8 | x3 | — | Corte | 1 |
```

**Problema:** Em telas estreitas ou leitores de tela, tabelas com 7+ colunas são difíceis de navegar. Propriedades ficam separadas do nome do item.

### Tabelas de Resumo (Opcionais)

Você pode incluir uma tabela resumida ao final para referência rápida:

```markdown
## Armas (Descrições Completas)

### Espada Longa
**Preço:** T$ 15 | **Dano:** 1d8 | **Crítico:** 19 | **Alcance:** — | **Tipo:** Corte | **Espaços:** 1

Descrição completa aqui...

### Machado de Guerra
**Preço:** T$ 20 | **Dano:** 1d8 | **Crítico:** x3 | **Alcance:** — | **Tipo:** Corte | **Espaços:** 1

Descrição completa aqui...

## Tabela de Referência Rápida

| Arma | Preço |
|------|-------|
| Espada longa | T$ 15 |
| Machado de guerra | T$ 20 |
```

---

## Exemplos Práticos

### Exemplo 1: Capítulo de Magia

```markdown
# Magia

## Lista de Magias

### 1º Círculo

**Abjuração**

Escudo arcano • Proteção contra mal • Resistência a energia

**Encantamento**

Compreensão • Enfeitiçar pessoa • Sono

## Descrição das Magias

### Escudo Arcano

Arcana 1 (Abjuração)

**Execução:** padrão; **Alcance:** pessoal; **Alvo:** você; **Duração:** cena.

Você cria um campo de força invisível que fornece +4 na Defesa.

**+2 PM:** muda o alcance para toque e o alvo para 1 criatura.

### Proteção Contra o Mal

Divina 1 (Abjuração)

**Execução:** padrão; **Alcance:** toque; **Alvo:** 1 criatura; **Duração:** cena.

O alvo recebe +2 na Defesa e em testes de resistência contra criaturas malignas.
```

### Exemplo 2: Lista de Equipamentos

```markdown
# Equipamentos

## Armas

### Tabela de Armas

#### Armas Simples de Corpo a Corpo

| Arma | Preço | Dano | Crítico | Alcance | Tipo | Espaços |
|------|-------|------|---------|---------|------|---------|
| Adaga | T$ 2 | 1d4 | 19 | Curto | Perfuração | 1 |
| Lança | T$ 5 | 1d6 | x3 | — | Perfuração | 2 |

#### Armas Simples à Distância

| Arma | Preço | Dano | Crítico | Alcance | Tipo | Espaços |
|------|-------|------|---------|---------|------|---------|
| Arco curto | T$ 30 | 1d6 | x3 | Curto | Perfuração | 1 |
| Flechas (20) | T$ 2 | — | — | — | — | 1 |

### Descrição das Armas

#### Adaga

Esta faca afiada é usada por muitos habitantes adultos do Reinado. Quando ataca com uma adaga, você pode usar sua **Destreza em vez de Força** nos testes de ataque. Uma adaga **pode ser arremessada**.

#### Lança

Uma haste de madeira com ponta de metal afiada. Uma lança **pode ser arremessada** e causa **dano dobrado** em uma investida.
```

### Exemplo 3: Poderes de Classe

```markdown
# Poderes

## Poderes Gerais

### Acuidade com Arma

**Pré-requisito:** Des 1

Quando usa uma **arma corpo a corpo leve** ou uma **arma de arremesso**, você pode usar sua **Destreza em vez de Força** nos testes de ataque e rolagens de dano.

### Ataque Poderoso

**Pré-requisito:** For 1

Quando faz um ataque corpo a corpo, você pode sofrer uma penalidade em seu teste de ataque para causar dano adicional. A penalidade e o bônus são iguais ao seu **bônus de Força**, até um máximo de –5 no teste de ataque e +5 no dano.

### Foco em Arma

Escolha uma arma. Você recebe **+2 em testes de ataque** com essa arma. Você pode escolher este poder várias vezes para armas diferentes.
```

---

## Validação

Para verificar se seu conteúdo está acessível, use o script de validação:

```bash
# Validar um livro específico
python scripts/validate_accessibility.py --book dragao-brasil

# Validar todos os livros (resumo)
python scripts/validate_accessibility.py --summary

# Validar com detalhes completos
python scripts/validate_accessibility.py --verbose
```

O script detecta automaticamente:

- ✓ Cabeçalhos de categoria dentro de linhas de tabela
- ✓ Itens usando `**Nome.** ` em vez de cabeçalhos
- ✓ Placeholders inválidos (`**`) em células
- ✓ Pulos na hierarquia de cabeçalhos
- ✓ Tabelas incompletas ou truncadas

---

## Benefícios da Acessibilidade

Seguindo esses padrões, você garante que:

1. **Usuários de leitores de tela** podem navegar eficientemente pelo conteúdo
2. **Todos os jogadores** se beneficiam de uma estrutura clara e consistente
3. **Buscas e índices** funcionam melhor com cabeçalhos apropriados
4. **Ferramentas de conversão** (PDF, EPUB, etc.) produzem resultados melhores
5. **Manutenção futura** é mais fácil com estrutura previsível

---

## Referências

Este guia é baseado nas melhores práticas de:

- [WCAG 2.1 (Web Content Accessibility Guidelines)](https://www.w3.org/WAI/WCAG21/quickref/)
- [Markdown Accessibility Guide](https://www.markdownguide.org/basic-syntax/)
- Padrões estabelecidos no **Tormenta20 - Livro Básico**

Para dúvidas ou sugestões sobre acessibilidade, abra uma issue no repositório do projeto.

---
title: "Perícias - Sistema Básico"
book: "tormenta20-core"
chapter: "05-pericias-poderes"
navigation:
  previous: "README.md"
  next: "02-pericias-lista.md"
  up: "README.md"
---

# Perícias - Sistema Básico

> "Perícias medem suas capacidades mundanas. São usadas para realizar todo tipo de façanha, de saltar sobre um desfiladeiro a acertar um monstro com sua espada e decifrar um pergaminho antigo."

---

## O Que São Perícias?

Perícias medem suas **capacidades mundanas**. São usadas para realizar todo tipo de façanha, desde saltar sobre um desfiladeiro até acertar um monstro com sua espada e decifrar um pergaminho antigo.

---

## Escolhendo Perícias

### Perícias Treinadas

Ao escolher sua **classe**, você recebe um número de **perícias treinadas** (ou seja, nas quais é mais competente).

Você também recebe um número de perícias treinadas igual a sua **Inteligência** (se positiva).

**Perícias ganhas por Inteligência** não precisam pertencer à lista de sua classe.

### Ganhando Novas Perícias

Você pode ganhar novas perícias treinadas com:
- O poder **Treinamento em Perícia**
- Aumentando sua **Inteligência** (exceto aumentos temporários)

---

## Usando Perícias

A descrição de cada perícia explica o que você pode fazer com ela, junto com exemplos de usos e suas respectivas regras.

**Testes de perícia** seguem a mecânica básica do jogo, apresentada na Introdução e detalhada no Capítulo 5: Jogando.

---

## Bônus de Perícia

Quando faz um teste de perícia, você soma seu **bônus de perícia** ao resultado do d20.

Esse número é uma medida de sua competência com a perícia em questão.

### Fórmula do Bônus

```
Bônus de Perícia = 
  Metade do Nível (arredondado para baixo) 
  + Atributo-chave 
  + Bônus de Treinamento (se for treinado)
```

### Bônus de Treinamento

Nas perícias **treinadas**, você recebe um bônus adicional:
- **+2** do 1º ao 6º níveis
- **+4** do 7º ao 14º níveis  
- **+6** do 15º nível em diante

### Exemplo de Cálculo

**Personagem de 3º nível com Força 4:**
- Bônus nas perícias baseadas em Força (Atletismo e Luta): **+5**
  - +1 da metade do nível (3÷2 = 1)
  - +4 da Força

**Se for treinado em Atletismo:**
- Bônus em Atletismo: **+7**
  - +1 da metade do nível
  - +4 da Força
  - +2 do treinamento (níveis 1-6)

---

## Atributo-Chave

O **atributo usado com a perícia**. Afeta seu bônus de perícia.

### Exemplos

- **Diplomacia** envolve **lábia** e **capacidade de argumentação**, por isso seu atributo-chave é **Carisma**
- **Conhecimento** envolve **estudo** e **memória**, por isso seu atributo-chave é **Inteligência**

Consulte a [Tabela Resumo de Perícias](README.md#tabela-resumo-perícias) para ver o atributo-chave de cada perícia.

---

## Treinamento e Testes

### Perícias Somente Treinadas

Algumas perícias **só podem ser usadas quando você é treinado nelas**.

**Exemplo:** Se você não é treinado em **Ladinagem**, não tem o conhecimento necessário para desarmar uma armadilha, independentemente de seu nível ou Destreza.

### Identificação na Lista

Quando a palavra **"treinada"** aparece após o nome da perícia, você **só poderá usá-la se for treinado nela**.

Além disso, algumas perícias possuem **usos específicos** que exigem treinamento (marcados como "Apenas Treinado" na descrição do uso).

---

## Penalidade de Armadura

Algumas perícias exigem **liberdade de movimento**.

Quando a palavra **"armadura"** aparece após o nome da perícia, você sofrerá uma **penalidade nos testes** dela se estiver usando armadura ou escudo.

Veja o **Capítulo 3: Equipamento** para detalhes sobre a penalidade específica de cada armadura.

### Perícias Afetadas

As perícias que sofrem penalidade de armadura são:
- **Acrobacia**
- **Atletismo** (apenas para nadar)
- **Furtividade**
- **Ladinagem**

---

## Tabela Completa de Perícias

| Perícia | Atributo-chave | Somente Treinada? | Penalidade de Armadura? |
|---------|----------------|-------------------|-------------------------|
| **Acrobacia** | Des | — | Sim |
| **Adestramento** | Car | Sim | — |
| **Atletismo** | For | — | — |
| **Atuação** | Car | Sim | — |
| **Cavalgar** | Des | — | — |
| **Conhecimento** | Int | Sim | — |
| **Cura** | Sab | — | — |
| **Diplomacia** | Car | — | — |
| **Enganação** | Car | — | — |
| **Fortitude** | Con | — | — |
| **Furtividade** | Des | — | Sim |
| **Guerra** | Int | Sim | — |
| **Iniciativa** | Des | — | — |
| **Intimidação** | Car | — | — |
| **Intuição** | Sab | — | — |
| **Investigação** | Int | — | — |
| **Jogatina** | Car | Sim | — |
| **Ladinagem** | Des | Sim | Sim |
| **Luta** | For | — | — |
| **Misticismo** | Int | Sim | — |
| **Nobreza** | Int | Sim | — |
| **Ofício** | Int | Sim | — |
| **Percepção** | Sab | — | — |
| **Pilotagem** | Des | Sim | — |
| **Pontaria** | Des | — | — |
| **Reflexos** | Des | — | — |
| **Religião** | Sab | Sim | — |
| **Sobrevivência** | Sab | — | — |
| **Vontade** | Sab | — | — |

---

## Perícias de Resistência

**Fortitude, Reflexos e Vontade** são usadas para resistir a efeitos negativos, como uma explosão ou um encantamento de controle mental. Por isso, são chamadas de **perícias de resistência**.

### Como Funcionam

Efeitos que afetem seus **"testes de resistência"** afetam **todos os testes** destas perícias.

**Exemplo:** Um efeito que forneça **+1 em testes de resistência** fornece +1 em **Fortitude, Reflexos e Vontade**.

### As Três Perícias

- **Fortitude (Con):** Resistir a doenças, venenos, exaustão
- **Reflexos (Des):** Resistir a explosões, armadilhas, efeitos de área
- **Vontade (Sab):** Resistir a controle mental, intimidação, encantamentos

---

## Usos Comuns das Perícias

Cada perícia tem diversos usos, mas alguns padrões são comuns:

### Testes Simples
Você faz um teste e compara com uma CD (Classe de Dificuldade):
- **CD 15:** Tarefa desafiadora
- **CD 20:** Tarefa difícil
- **CD 25:** Tarefa muito difícil
- **CD 30:** Tarefa quase impossível

### Testes Opostos
Seu teste é comparado ao teste de outra criatura. Quem tiver maior resultado vence.

**Exemplo:** **Enganação** (mentir) vs **Intuição** (perceber mentira)

### Testes de Resistência
Usado para resistir a efeitos nocivos. A CD é determinada pelo efeito.

**Exemplo:** Resistir a um veneno com **Fortitude CD 20**

---

## Próximos Passos

Agora que você entende o sistema básico, veja:

- **[Lista Completa de Perícias →](02-pericias-lista.md)** - Todas as 33 perícias detalhadas com usos e exemplos
- **[Poderes Gerais - Sistema →](03-poderes-gerais-sistema.md)** - Sistema de poderes gerais

---
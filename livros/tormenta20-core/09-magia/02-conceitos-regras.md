---
title: "Conceitos Fundamentais de Magia"
book: "tormenta20-core"
chapter: "09-magia"
navigation:
  previous: null
  next: null
  up: "README.md"
---

# Conceitos Fundamentais de Magia

[◄ Voltar para Magia](README.md)

## 🎯 Lançando Magias

### Atributo-Chave

O atributo-chave define o poder de suas magias e depende da sua classe:

| Classe | Atributo-Chave |
|--------|----------------|
| Mago, Clérigo | Inteligência |
| Feiticeiro, Bardo | Carisma |
| Druida, Paladino | Sabedoria |

### CD das Magias

A Classe de Dificuldade (CD) das suas magias é calculada como:

**CD = 10 + círculo da magia + modificador do atributo-chave**

**Exemplo**: Um mago com Inteligência 18 (+4) lançando Bola de Fogo (2º círculo) terá CD 16 (10 + 2 + 4).

### Componentes

Magias podem exigir três tipos de componentes:

- **Verbais (V)**: Palavras mágicas que devem ser pronunciadas claramente
- **Gestuais (G)**: Movimentos específicos com as mãos
- **Materiais (M)**: Itens físicos consumidos ou utilizados

**Importante**: 
- Componentes verbais exigem que você possa falar
- Componentes gestuais exigem pelo menos uma mão livre
- Componentes materiais custosos são especificados na descrição da magia

### Pontos de Mana (PM)

Magias custam Pontos de Mana para serem lançadas. O custo base depende do círculo:

| Círculo | Custo Base |
|---------|------------|
| 1º | 1 PM |
| 2º | 2 PM |
| 3º | 5 PM |
| 4º | 10 PM |
| 5º | 15 PM |

## 🎨 Aprimoramentos

Você pode gastar PM adicionais para aprimorar uma magia, tornando-a mais poderosa. Cada magia lista seus aprimoramentos possíveis.

### Aprimoramentos Comuns

**+1 PM**: Geralmente aumenta número de alvos ou área  
**+2 PM**: Aumenta dano, duração, alcance ou muda componentes  
**+3 PM**: Muda tipo de alvo ou resistência  
**+5 PM**: Efeito significativo (pode requerer círculo superior)  
**+9 PM ou mais**: Efeito muito poderoso (geralmente requer 4º ou 5º círculo)

### Limitações

- Só pode usar aprimoramentos que exijam um círculo que você pode lançar
- Exemplo: Um conjurador de 5º nível (máximo 2º círculo) não pode usar aprimoramentos que exijam 3º círculo

## ✨ Truques

Truques são versões econômicas de magias de 1º círculo. Eles custam **0 PM** mas têm efeitos reduzidos.

**Características dos Truques:**
- Não contam como magia conhecida (você os ganha automaticamente)
- São ações menores da magia original
- Não podem ser aprimorados
- Úteis para preservar PM em situações simples

**Exemplo**: O truque de Luz cria uma luz fraca, enquanto a magia completa ilumina uma área maior.

## 📖 Escolas de Magia

As magias são organizadas em oito escolas:

### Abjuração (Abjur)
Proteção, barreiras, dispersão de efeitos mágicos  
**Exemplos**: Armadura Arcana, Dissipar Magia, Escudo da Fé

### Adivinhação (Adiv)
Conhecimento, previsão do futuro, detecção  
**Exemplos**: Detectar Ameaças, Lendas e Histórias, Vidência

### Convocação (Conv)
Criação de matéria/energia, transporte, invocação de criaturas  
**Exemplos**: Conjurar Monstro, Salto Dimensional, Teletransporte

### Encantamento (Encan)
Controle mental, influência sobre vontade  
**Exemplos**: Enfeitiçar, Comando, Sono

### Evocação (Evoc)
Manipulação de energia, cura, dano direto  
**Exemplos**: Bola de Fogo, Curar Ferimentos, Relâmpago

### Ilusão
Enganação sensorial, disfarces, imagens falsas  
**Exemplos**: Criar Ilusão, Invisibilidade, Miragem

### Necromancia (Necro)
Vida, morte, energia negativa, mortos-vivos  
**Exemplos**: Conjurar Mortos-Vivos, Infligir Ferimentos, Toque Vampírico

### Transmutação (Trans)
Alteração de forma, movimento, propriedades físicas  
**Exemplos**: Alterar Tamanho, Metamorfose, Voo

## ⚔️ Lançando em Combate

### Tempo de Execução

**Ação Padrão**: A maioria das magias  
**Ação de Movimento**: Magias rápidas (ex: Salto Dimensional com +2 PM)  
**Ação Completa**: Magias complexas (ex: 1d3+1 rodadas para Banimento)  
**Reação**: Magias defensivas instantâneas (ex: Escudo da Fé)

### Concentração

Algumas magias têm duração "sustentada", exigindo que você mantenha concentração:

- Requer uma ação de movimento por rodada
- Sofrer dano exige teste de Misticismo (CD 10 + dano sofrido)
- Falhar no teste encerra a magia

### Lançar na Defensiva

Se estiver ameaçado por um inimigo, você pode:
- **Lançar normalmente**: Provoca ataque de oportunidade
- **Lançar na defensiva**: Faça teste de Misticismo (CD 15 + círculo da magia). Falhar gasta a magia sem efeito

## 🎭 Tradições Mágicas

### Magia Arcana
Obtida através de estudo (magos) ou talento inato (feiticeiros)

**Classes Arcanas**: Mago, Feiticeiro, Bardo  
**Características**:
- Maior variedade de magias ofensivas
- Foco em dano e controle de campo
- Magias de utilidade e transporte

### Magia Divina  
Concedida por deuses (clérigos) ou pela natureza (druidas)

**Classes Divinas**: Clérigo, Druida, Paladino  
**Características**:
- Maior foco em cura e suporte
- Magias de proteção e bênção
- Controle de natureza e invocações

## 📊 Alcance das Magias

| Alcance | Distância | Observações |
|---------|-----------|-------------|
| Pessoal | Você | Apenas o conjurador |
| Toque | Adjacente | Requer toque físico |
| Curto | 9m | Básico para magias de toque |
| Médio | 30m | Padrão para magias de combate |
| Longo | 90m | Magias de longa distância |
| Ilimitado | Qualquer | Requer condições específicas |

## ⏱️ Duração das Magias

**Instantânea**: Efeito imediato e permanente  
**1 rodada**: 6 segundos  
**Cena**: Até o fim do encontro atual  
**1 dia**: 24 horas  
**Permanente**: Dura até ser dissipada  
**Sustentada**: Enquanto mantiver concentração

## 🛡️ Testes de Resistência

Quando um alvo pode resistir a uma magia:

**Fortitude (Fort)**: Resistência física, venenos, petrificação  
**Reflexos (Ref)**: Agilidade, esquiva de explosões  
**Vontade (Von)**: Resistência mental, ilusões, encantamentos

**Resultado do Teste**:
- **Anula**: Sucesso = sem efeito; Falha = efeito completo
- **Parcial**: Sucesso = efeito reduzido; Falha = efeito completo  
**Reduz à metade**: Sucesso = metade do dano; Falha = dano completo

## 🎯 Tipos de Alvo

**Criatura**: Um ser vivo ou morto-vivo  
**Objeto**: Item inanimado  
**Área**: Zona geométrica (cone, esfera, linha, cubo)  
**Efeito**: Cria algo novo (conjurações, ilusões)

### Formas de Área Comuns

**Cone**: Área que se expande a partir de você  
**Esfera/Cilindro**: Área circular centrada em um ponto  
**Linha**: Área reta e estreita  
**Cubo/Quadrado**: Área com cantos definidos

## 💡 Dicas Importantes

1. **Planeje seus PM**: Magias poderosas custam muito. Reserve PM para emergências
2. **Use Truques**: Economize PM em situações simples
3. **Aprimoramentos Táticos**: Às vezes +2 PM para aumentar dano vale mais que uma segunda magia
4. **Combine Magias**: Névoa + Invisibilidade = furtividade extrema
5. **Respeite Resistências**: Criaturas podem ser imunes a certos tipos de dano
6. **Leia Completamente**: Aprimoramentos podem mudar radicalmente uma magia

---

## 📝 Exemplo de Uso Completo

**Situação**: Um mago de 7º nível (máximo 3º círculo) com Inteligência 18 (+4) enfrenta 3 orcs.

**Magia Escolhida**: Bola de Fogo (2º círculo, área esfera 6m de raio)
- **Custo Base**: 2 PM
- **Aprimoramento**: +2 PM para aumentar dano em +2d6
- **Custo Total**: 4 PM

**Cálculo**:
- **CD**: 10 + 2 (círculo) + 4 (Int) = 16
- **Dano**: 6d6 (base) + 2d6 (aprimoramento) = 8d6
- **Teste**: Cada orc faz Reflexos CD 16
  - Sucesso = 4d6 de dano
  - Falha = 8d6 de dano

---

[◄ Voltar para Magia](README.md) | [Ver Listas de Magias ►](01-listas-magias.md)

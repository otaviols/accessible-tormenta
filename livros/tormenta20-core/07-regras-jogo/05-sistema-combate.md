---
title: "Sistema de Combate Completo"
book: "tormenta20-core"
chapter: "07-regras-jogo"
navigation:
  previous: null
  next: null
  up: "README.md"
---

# Sistema de Combate Completo

[◂ Voltar ao Índice](README.md)

---

## 📌 Visão Geral

Embora seja possível superar obstáculos e vencer inimigos de muitas formas, às vezes os heróis ficam sem escolha além de sacar suas armas, preparar suas magias e partir para a batalha.

---

## 📊 Estatísticas de Combate

### Teste de Ataque

Este é um tipo específico de teste de perícia, para acertar um alvo com um ataque. Normalmente é um teste de **Luta** (para ataques corpo a corpo) ou de **Pontaria** (para ataques à distância).

```
Teste de Ataque = 1d20 + Bônus de Ataque
```

A dificuldade do teste é a **Defesa do alvo**. Se o resultado é igual ou maior que a Defesa do alvo, você acerta e causa dano.

Um teste de ataque pode sofrer modificadores por habilidades, arma e condições.

### Dano

Quando você acerta um ataque, causa dano. Esse dano reduz os pontos de vida do inimigo.

Você rola dados para descobrir quanto dano causou. O tipo de dado depende da arma ou ataque utilizado — por exemplo, **1d4** para uma adaga ou **1d8** para uma espada longa.

O dano de cada arma é descrito no Capítulo 3: Equipamento.

#### Dano Corpo a Corpo ou Arremesso
```
Dano = Dano da Arma + Força do Atacante
```

Para ataques corpo a corpo ou com armas de arremesso, você soma sua Força na rolagem de dano.

#### Dano com Arma de Disparo
```
Dano = Dano da Arma
```

Para armas de disparo (arcos, bestas, armas de fogo), você NÃO soma a Força.

**Exemplo:** Um personagem com Força 3 usando uma espada longa causa **1d8+3** pontos de dano (1d8 da espada longa mais 3 da Força).

### Acertos Críticos

Um acerto crítico é um ataque especialmente certeiro, que atinge pontos vitais ou vulneráveis.

A tabela de armas do Capítulo 3: Equipamento possui uma coluna "Crítico". Cada arma tem:
- **Margem de ameaça:** Que pode ser 18, 19 ou 20
- **Multiplicador:** Que pode ser x2, x3 ou x4

Quando nenhuma margem aparece, será **20**. Quando nenhum multiplicador aparece, será **x2**.

#### Como Funciona

Você faz um acerto crítico quando acerta um ataque rolando um valor **igual ou maior que a margem de ameaça da arma**. Neste caso, multiplica os **dados de dano** do ataque (incluindo quaisquer aumentos por passos) pelo multiplicador da arma.

**Bônus numéricos de dano**, assim como **dados extras** (como pela habilidade Ataque Furtivo) **não são multiplicados**.

**Certas criaturas são imunes a acertos críticos.** Um alvo imune a acertos críticos ainda sofre o dano de um ataque normal.

### Iniciativa

A cada rodada, todo personagem tem um turno — sua vez de agir. A Iniciativa determina a **ordem dos turnos** dentro da rodada.

#### Teste de Iniciativa
```
Teste de Iniciativa = 1d20 + Destreza
```

No início do combate, cada jogador faz um teste de Iniciativa para seu personagem. O mestre faz um único teste para os inimigos (caso haja inimigos com bônus de Iniciativa diferentes, o mestre usa o menor valor).

**Aqueles com os resultados mais altos agem primeiro.**

#### Empates
No caso de empates, o personagem com o **maior modificador de perícia** age primeiro. Se o empate persistir, eles fazem um novo teste de Iniciativa entre si, para decidir quem age primeiro.

**Não é preciso fazer novos testes de Iniciativa a cada rodada**; a ordem se mantém durante todo o combate.

#### Entrando na Batalha
Se um personagem entra na batalha depois que ela começou, faz um teste de Iniciativa e age quando seu turno chegar, **na rodada seguinte**.

#### Surpresa
Quando o combate começa, se você não percebeu seus inimigos, está **surpreendido**. Se você está ciente de seus inimigos, mas eles não estão cientes de você, **eles é que estão surpreendidos**. Caso os dois lados tenham se percebido, ninguém está surpreendido. E se nenhum lado percebe o outro... bem, nenhum combate acontece!

**Um personagem surpreendido:**
- Fica **desprevenido** (–5 na Defesa)
- **Não age na primeira rodada**

#### Percebendo os Inimigos
O mestre diz quem está ciente de seus inimigos no começo do combate. Em geral, ele diz aos jogadores para fazerem testes de **Percepção** contra uma dificuldade ou opostos pelo teste de **Furtividade** dos inimigos (caso estes estejam sendo cautelosos).

**Um personagem que nunca fica surpreendido** (por exemplo, se tiver a habilidade Esquiva Sobrenatural) pode rolar a Iniciativa e agir mesmo que falhe em seu teste de Percepção; de alguma maneira ele já esperava o perigo, ou reage com reflexos impossivelmente rápidos.

---

## ⚔️ Como Funciona o Combate?

O combate acontece em uma série de **rodadas**. Uma rodada é o tempo necessário para que todos os personagens no combate tenham seu turno. Um **turno** é o tempo que cada personagem tem para agir.

### Sequência do Combate

**Passo 1. Iniciativa**
Cada personagem faz um teste de Iniciativa. O mestre faz um único teste para os inimigos.

**Passo 2. Surpresa**
O mestre diz quais personagens estão cientes de seus inimigos. Aqueles que não percebem a presença de inimigos começam o combate surpreendidos. Um personagem surpreendido fica desprevenido e não age na primeira rodada.

**Passo 3. Turnos**
Todos os personagens têm seu turno na ordem da Iniciativa (exceto aqueles surpreendidos, que não agem na primeira rodada).

**Passo 4. Nova Rodada**
Quando todos os personagens tiverem seu turno, a rodada termina. Uma outra rodada se inicia, com todos os personagens agindo novamente, na mesma ordem. Mesmo aqueles que estavam surpreendidos agora podem agir.

---

## 🕐 A Rodada de Combate

Uma rodada representa cerca de **seis segundos** no mundo de jogo. Durante a rodada, cada jogador (incluindo o mestre) tem o seu turno, a sua vez de realizar ações.

### Rodada como Medida de Tempo

Pense em "rodada" como se fosse uma medida de tempo, como "mês": o mês representa os dias marcados no calendário, mas também determina o tempo entre um dia e o mesmo dia no mês seguinte.

Assim, a rodada começa no turno do primeiro personagem (aquele que teve Iniciativa mais alta) e termina após o turno do último (aquele com Iniciativa mais baixa). Mas a rodada também é o tempo entre uma Iniciativa e a mesma Iniciativa na rodada seguinte.

**Efeitos que duram certo número de rodadas** terminam imediatamente antes do mesmo resultado de Iniciativa quando se iniciaram, após o número apropriado de rodadas.

---

## 🎯 Tipos de Ações

No seu turno, você pode fazer uma **ação padrão** e uma **ação de movimento**, em qualquer ordem.

Você pode trocar sua ação padrão por uma ação de movimento, para fazer duas ações de movimento, mas não pode fazer o inverso.

Você também pode abrir mão das duas ações (tanto a padrão quanto a de movimento) para fazer uma **ação completa**.

### Portanto, em um turno você pode fazer:
- Uma ação padrão e uma ação de movimento; OU
- Duas ações de movimento; OU
- Uma ação completa

Você também pode executar qualquer quantidade de **ações livres** e **reações**.

### Ação Padrão
Basicamente, uma ação padrão permite que você execute uma tarefa. Fazer um ataque ou lançar uma magia são as ações padrão mais comuns.

### Ação de Movimento
Esta ação representa algum tipo de movimento físico. Seu uso mais comum é percorrer uma distância igual a seu deslocamento. Levantar-se, sacar uma arma, pegar um item de sua mochila, abrir uma porta e subir numa montaria também são ações de movimento.

### Ação Completa
Este tipo de ação exige todo o tempo e esforço normal de uma rodada. Para uma ação completa, você deve abrir mão de sua ação padrão e de sua ação de movimento — mas, normalmente, você ainda pode realizar ações extras, ações livres e reações.

### Ação Livre
Esta ação não exige quase nenhum tempo e esforço, mas ainda só pode ser feita em seu turno. Jogar-se no chão ou gritar uma ordem são ações livres — mas o mestre pode decidir que algo é complicado demais para ser livre. Dar uma ordem curta é uma ação livre, explicar um plano inteiro, não!

### Reação
Uma reação acontece em resposta a outra coisa. Como ações livres, reações tomam tão pouco tempo que você pode realizar qualquer quantidade delas. A diferença é que uma ação livre é uma escolha consciente, executada no turno do personagem. Já uma reação é um reflexo ou uma resposta automática, que pode ocorrer mesmo fora do seu turno. Você pode reagir mesmo se não puder realizar ações normais, como quando estiver atordoado. Um teste de Percepção para perceber um troll escondido no pântano, ou um teste de Reflexos para escapar de uma explosão, são exemplos de reações.

---

## ⚔️ Ações Padrão

### Agredir

Você faz um ataque com uma arma corpo a corpo ou à distância.

#### Armas Corpo a Corpo
Com uma arma corpo a corpo, você pode atacar qualquer inimigo dentro de seu **alcance natural** (1,5m para criaturas Pequenas e Médias ou um inimigo adjacente no mapa). Personagens maiores, ou usando certas armas, podem atacar mais longe.

Você pode substituir um ataque corpo a corpo por uma **manobra de combate**.

#### Armas de Ataque à Distância
Com uma arma de ataque à distância, você pode atacar qualquer inimigo que consiga ver e que esteja no alcance da arma (ou até o dobro do alcance, sofrendo uma penalidade de –5).

##### Atirando em Combate Corpo a Corpo
Quando faz um ataque à distância contra uma criatura em combate corpo a corpo, você sofre **–5 no teste de ataque**. Uma criatura está em combate corpo a corpo se estiver dentro do alcance natural de qualquer inimigo (incluindo você).

### Atropelar

Você usa uma ação padrão durante um movimento para avançar pelo espaço ocupado por uma criatura (normalmente, você não pode fazer uma ação padrão durante um movimento; isto é uma exceção). A criatura pode lhe dar passagem ou resistir.

- **Se der passagem:** Você avança pelo espaço dela; nenhum teste é necessário.
- **Se resistir:** Faça um **teste de manobra oposto**; se você vencer, deixa a criatura caída e continua seu avanço. Se o alvo vencer, continua de pé e detém seu avanço.

**Atropelar é uma ação livre se tentada durante uma investida.**

### Fintar

Faça um teste de **Enganação** oposto ao teste de **Reflexos** de uma criatura em alcance curto. Se você passar, ela fica **desprevenida** contra seu próximo ataque, mas apenas até o fim de seu próximo turno.

### Lançar uma Magia

A maioria das magias exige uma ação padrão para ser executada.

### Preparar

Você prepara uma ação (padrão, de movimento ou livre) para realizar mais tarde, após seu turno, mas antes de seu turno na próxima rodada. Diga a ação que vai fazer e em quais circunstâncias.

**Exemplo:** "Disparar minha besta na primeira criatura que passar pela porta."

A qualquer momento antes de seu próximo turno, você pode fazer a ação preparada como uma **reação** a essas circunstâncias.

Se, no seu próximo turno, você ainda não tiver realizado sua ação preparada, não pode mais realizá-la (embora possa preparar a mesma ação de novo).

**Pelo resto do combate, sua Iniciativa fica imediatamente acima da qual você fez a ação preparada.**

### Usar uma Habilidade ou Item Mágico

Algumas habilidades e itens mágicos, como poções, exigem uma ação padrão para serem usadas.

---

## 🏃 Ações de Movimento

### Levantar-se
Levantar do chão (ou de uma cama, cadeira...) exige uma ação de movimento.

### Manipular Item
Muitas vezes, manipular um item exige uma ação de movimento. Pegar um objeto em uma mochila, abrir ou fechar uma porta e atirar uma corda para alguém são ações de movimento.

### Mirar
Você mira em um alvo que possa ver, dentro do alcance de sua arma. Isso **anula a penalidade de –5** em testes de Pontaria realizados neste turno contra aquele alvo caso ele esteja engajado em combate corpo a corpo.

### Movimentar-se
Você pode percorrer uma distância igual a seu **deslocamento** (tipicamente 9m para raças de tamanho Médio). Outros tipos de movimento, como nadar, escalar ou cavalgar, também usam esta ação.

### Sacar ou Guardar Item
Sacar ou guardar um item exige uma ação de movimento.

---

## 🏃‍♂️ Ações Completas

### Corrida
Você corre mais rapidamente que seu deslocamento normal. Veja a perícia Atletismo.

### Golpe de Misericórdia
Você desfere um golpe letal em um oponente adjacente e indefeso. Um golpe de misericórdia é um **acerto crítico automático**.

Além de sofrer dano, a vítima tem uma chance de morrer instantaneamente:
- **25% (1 em 1d4)** para personagens e NPCs importantes
- **75% (1 a 3 em 1d4)** para NPCs secundários

### Investida
Você avança até o **dobro de seu deslocamento** (e no mínimo 3m) em linha reta e, no fim do movimento, faz um ataque corpo a corpo.

- Você recebe **+2 no teste de ataque**
- Você sofre **–2 na Defesa** até o seu próximo turno, porque sua guarda fica aberta
- Você **não pode** fazer uma investida em terreno difícil

Durante uma investida, você pode fazer a manobra **atropelar** como uma ação livre (mas não pode atropelar e atacar o mesmo alvo).

### Lançar uma Magia
Ao lançar magias com execução maior do que uma ação completa, você gasta uma ação completa a cada rodada.

---

## 🎪 Ações Livres

### Atrasar
Escolhendo atrasar sua ação, você age mais tarde na ordem de Iniciativa, em relação à Iniciativa que rolou. Isto é o mesmo que reduzir sua Iniciativa voluntariamente pelo resto do combate.

Quando sua nova Iniciativa chegar, você age normalmente. Você pode especificar este novo valor de Iniciativa ou apenas esperar até algum momento e então agir, fixando sua nova Iniciativa neste ponto. **Atrasar é útil para ver o que seus amigos ou inimigos farão, antes de decidir o que você mesmo fará.**

#### Limites para Atrasar
Você pode atrasar sua Iniciativa até **–10 menos seu bônus de Iniciativa**. Quando a contagem de Iniciativa chega a esse ponto, você deve agir ou abrir mão de qualquer ação na rodada.

**Exemplo:** Um personagem com um bônus de Iniciativa +3 pode esperar até a contagem de Iniciativa chegar a –13. Nesse ponto, deve agir ou desistir de seu turno.

#### Vários Atrasos
Se vários personagens estão atrasando suas ações, aquele com o maior bônus de Iniciativa (ou a maior Destreza, em caso de empate) tem a vantagem. Se dois ou mais personagens que estejam atrasando quiserem agir na mesma contagem de Iniciativa, aquele com o maior bônus age primeiro. Se dois ou mais personagens estão tentando agir um depois do outro, aquele com o maior bônus de Iniciativa tem o direito de agir depois.

### Falar
Em geral, falar é uma ação livre. Lançar magias ou usar habilidades de classe que dependem da voz não são ações livres. O mestre também pode limitar aquilo que você consegue falar durante uma rodada (**vinte palavras são o limite padrão**).

### Jogar-se no Chão
Jogar-se no chão é uma ação livre. Você recebe os benefícios e penalidades normais por estar caído, mas normalmente não sofre dano ao se jogar no chão.

### Largar um Item
- Deixar cair um item que esteja segurando é uma **ação livre**
- Deixar cair (ou jogar) um item com a intenção de acertar algo é uma **ação padrão**
- Deixar cair (ou jogar) um item para que outra pessoa agarre é uma **ação de movimento**

---

## 🤼 Manobras de Combate

Uma manobra é um ataque corpo a corpo para fazer algo diferente de causar dano — como arrancar a arma do oponente ou empurrá-lo para um abismo. **Não é possível fazer manobras de combate com ataques à distância.**

### Como Funcionam

Faça um **teste de manobra** (um teste de ataque corpo a corpo) oposto com a criatura. Mesmo que ela esteja usando uma arma de ataque à distância, deve fazer o teste usando seu valor de Luta.

- **Em caso de empate:** O personagem com o maior bônus vence
- **Se os bônus forem iguais:** Outro teste deve ser feito

Em geral, você pode usar qualquer arma corpo a corpo para fazer manobras de combate.

### Tipos de Manobras

#### Agarrar
Você segura uma criatura (por seu braço, sua roupa etc.). Uma criatura agarrada:
- Fica **desprevenida** e **imóvel**
- Sofre **–2 nos testes de ataque**
- Só pode atacar com **armas leves**

A criatura pode se soltar com uma ação padrão, vencendo um teste de manobra oposto.

**Você só pode agarrar com um ataque desarmado ou arma natural** e, enquanto agarra, fica com essa mão ou arma natural ocupada. Além disso, move-se metade do deslocamento normal, mas arrasta a criatura que estiver agarrando. Você pode soltá-la com uma ação livre.

Você pode atacar uma criatura agarrada com sua mão livre. Se preferir, pode substituir um ataque por um teste de agarrar contra a criatura. Se vencer, causa dano de impacto igual a um ataque desarmado. Isso significa que você está esmagando ou sufocando o inimigo.

**Um personagem fazendo um ataque à distância contra um alvo envolvido na manobra agarrar tem 50% de chance de mirar no alvo errado!**

#### Derrubar
Você deixa o alvo **caído**. Esta queda normalmente não causa dano. Se você vencer o teste oposto por **5 pontos ou mais**, derruba o oponente com tanta força que também o empurra um quadrado em uma direção a sua escolha. Se isso o jogar além de um parapeito ou precipício, ele pode fazer um teste de Reflexos (CD 20) para se agarrar numa beirada.

#### Desarmar
Você derruba um item que a criatura esteja segurando. Normalmente o item cai no mesmo lugar em que o alvo está (a menos que o alvo esteja voando, sobre uma ponte etc.). Se você vencer o teste oposto por **5 pontos ou mais**, derruba o item com tanta força que também o empurra um quadrado em uma direção a sua escolha.

#### Empurrar
Você empurra a criatura **1,5m**. Para cada 5 pontos de diferença entre os testes, você empurra o alvo mais 1,5m. Você pode gastar uma ação de movimento para avançar junto com a criatura (até o limite do seu deslocamento).

#### Quebrar
Você atinge um item que a criatura esteja segurando. Veja adiante em "Quebrando Objetos".

---

## 💔 Ferimentos & Morte

### Pontos de Vida

Sempre que você sofre dano — golpeado pelo tacape de um ogro, atingido por uma Bola de Fogo ou caindo em uma armadilha —, perde pontos de vida. Você anota seus pontos de vida na ficha de personagem ou em qualquer rascunho. Quando sofre dano, subtrai este valor de seus pontos de vida.

O dano pode deixar cicatrizes, amassar sua armadura e sujar sua roupa de sangue, mas não o impede de agir. **Isso só muda quando seus pontos de vida chegam a 0 ou menos.**

### 0 PV ou Menos

Se ficar com 0 PV ou menos, você **cai inconsciente** e começa a **sangrar**. No início de seu turno, faça um **teste de Constituição (CD 15)**:
- **Se passar:** Você estabiliza e não precisa mais fazer esse teste
- **Se falhar:** Você perde **1d6 pontos de vida** e continua sangrando

Você deve repetir o teste a cada rodada, até estabilizar ou morrer.

**Um personagem sangrando pode ser estabilizado com:**
- Um teste de **Cura (CD 15)**; OU
- Qualquer efeito que cure pelo menos 1 PV

### Recuperando Consciência

Um personagem com 0 ou menos pontos de vida que recupere PV até um valor positivo (1 ou mais) por causa de uma habilidade, magia ou descanso, recobra a consciência e pode agir normalmente.

### Morte

Quando seus pontos de vida chegam a **–10** ou a **um número negativo igual à metade de seus PV totais** (o que for menor), você **morre**.

**Exemplo:** Oberon, o Martelo, um arcanista com 12 PV, morre se chegar a –10 PV. Mais tarde na campanha, Oberon sobe vários níveis e chega a 30 PV. Agora, ele só morre se chegar a –15 PV.

### Dano Não Letal

Dano não letal se soma ao dano letal para determinar quando você cai inconsciente, mas **não conta** para determinar quando você começa a sangrar ou morre. Se você tem dano letal e não letal e é curado, cura primeiro o dano não letal.

Quase todo dano causado em condições normais (armas, armadilhas, magias...) é letal. Você pode usar uma arma para causar dano não letal (batendo com as partes não afiadas da arma, controlando a força dos golpes ou evitando pontos vitais), mas sofre uma penalidade de **–5 no teste de ataque**.

Ataques desarmados e certas armas específicas causam dano não letal. Você pode usar esses ataques e armas para causar dano letal, mas sofre a mesma penalidade de **–5 no teste de ataque**.

---

[▸ Próximo: Movimentação e Situações Especiais](06-movimentacao-situacoes.md)

[◂ Anterior: Tipos de Efeitos e Dano](04-tipos-efeitos-dano.md)

[◂ Voltar ao Índice](README.md)

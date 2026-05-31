# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Escreva aqui o nome provisório do jogo.

Exemplo: Nave Py

> Corrida dos Obstáculos

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Pedro Henrique Alves Ferreira
- Nome 2: Enzo Bonzi Cassilhas
- Nome 3: Mateus Evaristo Melo
- Nome 4: Bernardo Calegari

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

>Nave desviando de meteoros

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

- O que aparece na tela?
- Aparecerão meteoros e terá a nave, o jogador, que deverá atirar nos meteoros e
  desviar caso necessário.
- O que o jogador controla?
- O jogador controla a nave.
- O que o jogador precisa fazer?
- Destruir meteoros e desviar caso necessário.
- Quais desafios aparecem durante a partida?
- Objetos indo em direção ao jogador, inimigos que disparam projeteis.


## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

- Acumular pontos e sobreviver o máximo de tempo possível.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1: 3 vidas iniciais.
- Regra 2: cada colisão remove 1 vida.
- Regra 3: sistema baseado em partidas.
- Regra 4: inimigos em posições aleatórias.
- Regra 5: dificuldade progressiva.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

- Para vencer o jogador deverá derrotar o chefão.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

Caso perca todas as vidas, o jogador perderá e deverá recomeçar. Caso derrotar
o chefe final, terá a partida finalizado por vitória.

## 9. Elementos previstos no jogo

Sistema de upgrades baseado em hordas.
Upgrades ao final de cada horda.
Sistema de moedas.
Ranking baseado em hordas.
Loja de skins.

## Jogador ou elemento principal

Exemplo:

Uma nave controlada pelas setas do teclado ou pelas teclas "wasd"

Descrição:

Ao clicar nas teclas do teclado, o personagem poderá se movimentar para a esquerda,
direita, para baixo e para cima.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

Obstáculos que disparam projeteis em direção ao jogador e se movimentam da ale
atoriamente, obstáculos que se movimentam em um linha reta em direção ao jogador.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> Alvos: Meteoros e aliens.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> O jogador começa com 3 vidas e recebe um upgrade para cada 5 hordas, melhorando
> a performance da nave.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando: Seta para cima: mover para cima
- Tecla/comando: Seta para baixo: mover para baixo
- Tecla/comando:
- Tecla/comando: ESC: pausar o jogo

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

> main.py: Inicia o jogo
> src/jogo.py: contém o loop principal
> src/config.py: guarda configurações como tamanho da tela e cores
> src/funcoes.py: contém funções auxiliares
> src/dados.py: contém funções de leitura e escrita de arquivos



## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

> sprite de nave
> sprite de nave inimiga
> sprite de meteoro
> sons gratuitos
> tutorial básico


Caso não pretenda utilizar recursos externos, escreva:

> Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: Desviar de projetil
- Dificuldade 2: Acertar os tiros
- Dificuldade 3: Derrotar o chefão

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> O mínimo seria a nave do jogador se movimentando e atirando para que posso destruir os obstáculos.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1: Skins
- Melhoria 2: Inimigos novos
- Melhoria 3: Modo infinito
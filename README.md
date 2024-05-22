# Projeto-final-PYGAME

TÍTULO

membros:
- Enzo Savino
- Gabriel Sallum
- Davi Körber

Explicações de como jogar o jogo:
  Ao clicar para rodar o código, aparecerá uma tela de login para colocar seu nome e os seus pontos serem guardados num arquivo .json . Após isso, aparecerá o jogo da cobrinha. Para controlar a cobrinha, podem ser usadas as setas ou WASD. Lembre-se que a cobrinha não pode mudar de direção oposta, pois senão bate nela mesma, inclusive quando ela é apenas um bloco. O objetivo é coletar as bitcoins que serão os pontos que poderão ser apostados posteriormente. Cada bitcoin vale 10 pontos e a cada moeda coletada, o corpo da cobrinha cresce 1 bloco e sua velocidade aumenta. Para perder, o jogador faz a cobrinha bater no prórpio corpo ou faz ela bater nas bordas da tela.
  Ao perder, é mostrado quantos pontos o jogador possui. Agora, o jogador tem a opção de apostar seus pontos.
  A aposta é feita da seguinte maneira: Serão rodados 4 dados, 2 vermelhos e 2 azuis. Antes disso, o jogador deve escolher uma cor - azul ou vermelho ou verde(para empate)- e a quantidade de pontos que quer apostar. Ganha os dados da mesma cor com maior soma. Se o jogador acertar, ele ganha o dobro do que apostou, considerando que os pontos são retirados quando são apostados. Se errar, perde os pontos que apostou.Caso o jogador acerte que a partida empatará, sua aposta será multiplicada por 8x. O jogador pode parar quando quiser, clicando para fechar a janela.
  O arquivo .json é um dicionário em que as chaves são os logins e os valores são os pontos do respectivo jogador. A cada vez que o código é rodado, o dicionário é reordenado de forma que monte um ranking dos jogadores com maior pontuação.


Link apresentando jogo:
  https://drive.google.com/file/d/1i2moFDUhHTVGvW2arcClWotElFQYYqKF/view?usp=sharing

Quais bibliotecas/modules a instalar:

Referências e Inspirações:
  - Cobrinha: https://youtu.be/bgsmYOm-W80?si=VcoeS6BtTXdUKvLk
  - Jogo dados aposta - referência no jogo de apostas de cassino on-line, conhecido como back bo

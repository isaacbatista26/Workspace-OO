# ***TETRIS*** - Block Puzzle

### Introdução:

O Tetris é um clássico jogo de quebra-cabeça que desafia os jogadores a organizar e empilhar blocos em queda de forma estratégica. O objetivo principal do jogo é preencher linhas horizontais completas com os blocos, impedindo que eles alcancem o topo da tela. 


Limpeza de Linhas: Quando uma linha é preenchida completamente, ela desaparece e os blocos acima dela caem para preencher o espaço vazio. Isso libera espaço na tela e permite continuar o jogo.

    Pontuação: Os jogadores recebem pontos à medida que empilham blocos e eliminam linhas. A pontuação geralmente aumenta à medida que você completa múltiplas linhas simultaneamente.

    Fim de Jogo: O jogo termina quando os blocos empilhados atingem o topo da tela, bloqueando o espaço disponível para o próximo bloco.

    Desafio Estratégico: O Tetris se torna mais desafiador à medida que os blocos caem mais rapidamente, exigindo decisões rápidas e estratégicas dos jogadores para evitar o fim do jogo.


### O Universo:

- O jogo ocorre em um **Grid** de dimensões 20x10.
- No início da rodada, as peças compostas por quatro quadrados menores cai do topo da tela.
- O objetivo é criar linhas horizontais completas de blocos, para obter a maior pontuação possível.
- A dificuldade do jogo aumenta gradualmente à medida que o numero de pontos cresce.
- O jogo termina quando o jogador não consegue alocar a peça dentro da tela.
- No final do jogo, o jogador pode escolher entre jogar novamente ou sair do jogo.
- Quando uma linha é preenchida completamente, ela desaparece e os blocos acima dela caem para preencher o espaço vazio

### As Peças:

- As Peças alternam entre sete formas e cores diferentes.
- São fornecidas ao jogador de forma aleatória.

### O jogador:

- Cada jogador é identificado por seu nome e têm registros de pontuação.
- Os jogadores são classificados com base em seus registros. Pontuações mais altas resultam em classificações melhores.
- Os jogadores devem empilhar os blocos de forma a preencher as lacunas na tela.
- Os jogadores têm a capacidade de mover as peças lateralmente, girá-las e acelerar sua queda.
- A aceleração das peças pelo jogador resulta em uma pontuação adicional.

### Banco de dados:

- O jogo inclui um banco de dados que armazena as estatísticas dos jogadores, como pontuações e níveis.
- Se o jogador precisar sair de uma partida não concluída, os dados não serão registrados no banco de dados.
- Se a partida for finalizada, o recorde será salvo no banco de dados.

### Dinâmica:

- Na tela inicial é possível visualizar os Scores do jogador anteriormente armazenados no banco de dados.
- Ao clicar Play, o jogo inicia e as peças começam a cair.
- Quando o jogador completa uma linha inteira horizontalmente no grid, eles recebem uma pontuação com base na função **f(x) = 100xy + 50z**, onde:
    - x = nível atual do jogador.
    - y = quantidade de linhas completadas de uma vez.
    - z = quantidade de linhas consecutivas completadas a cada nova peça que cai.
- À medida que o jogador pontua, ele avança de nível, e por consequência a velocidade de queda das peças aumenta, tornando o jogo mais desafiador.
- Quando o jogador começa a empilhar peças de forma que uma delas chegue ao topo da tela e não possa ser visualizada, o jogo dá **Game Over**
- Na tela de Game Over é possível ver um botão para ""Iniciar"" uma nova partida, um botão de ""Sair"" do jogo e uma tabela de Score.

# Pseudocode
Este pseudocodigo foi desenvolvido utilizando o paradigma orientado a objetos, foram criadas as seguintes classes: Forma, Ponto, Linha, Circulo, Quadrado e Triangulo. 
O código organiza as funcionalidades de cálculo, desenho e verificação de formas geométricas em classes separadas. Cada classe tem seu próprio conjunto de métodos para realizar tarefas específicas relacionadas à forma geométrica. 

OBS: Algumas classes receberam apenas funções/métodos de outras classes, e por isso foram nomeadas como "mixins_Forma" para deixar isso mais claro.

Classe Forma - É a base de todas as outras, e através dela foram criados métodos públicos que são utilizados nas demais classes.
- area() -> Calcula a área da forma.
- perimetro() -> Calcula o perímetro.
- desenhar() -> Desenha a forma desejada no console.
- estaDentroDe() -> Verifica se a forma está dentro de outra forma.

Classe Ponto - Possui um único método que calcula a distância entre dois pontos.

Classe Linha - Herda o método "distancia()" da classe Ponto com o objetivo de calcular o tamanho da linha.
- Também foi criado um método privado chamado "pontoMedio()" para calcular o ponto médio do segmento de reta.

Classe Círculo - Esta classe herda funcionalidades das classes Forma e Ponto para representar um círculo.
- O construtor recebe o raio do círculo como parâmetro e utiliza os métodos da classe Forma para calcular a área e o perímetro.
- Também utiliza o método "desenhar()" da classe Forma para representar o círculo no console.

Classe Quadrado - Esta classe herda funcionalidades das classes Forma e Ponto para representar um quadrado.
- O construtor recebe o lado do quadrado como parâmetro e utiliza os métodos da classe Forma para calcular a área e o perímetro.
- Também utiliza o método "desenhar()" da classe Forma para representar o quadrado no console.

Classe Triângulo - Esta classe herda funcionalidades das classes Forma e Ponto para representar um triângulo.
- O construtor recebe a base e a altura do triângulo como parâmetros e utiliza o método da classe Forma para calcular a área.
- Também utiliza o método "desenhar()" da classe Forma para representar o triângulo no console.
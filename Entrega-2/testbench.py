from my_libraries.shape2d import *
import time
import math

# Shape
print("Nova forma:\n")
forma = Shape("Circulo")
print(forma.shape)
forma.printCoord(2, 3)
time.sleep(1)
print("")

#Criação e update de coordenadas do Point
ponto_a = Point(0, 0)
print(ponto_a.getType())
ponto_a.printCoord(0, 0)
ponto_a.updateCoord(10, 20)
ponto_b = Point(3, 5)

time.sleep(1)

#Line
# Criar uma linha usando os dois pontos
line_ab = Line(ponto_a, ponto_b)
# Calcular o comprimento da linha
length_ab = line_ab.length()
print(f'O comprimento da linha de A para B é: {length_ab:.2f}')

#Calcular o ponto méedio da linha
midpoint_ab = line_ab.midpoint()
print(f'O ponto medio da linha de A para B é: {midpoint_ab}')

time.sleep(1)
print("")
# Circulo

circ = Circle(3, 3, 10)
print(circ.getType())
circ.printCoord()
circ.pointIn(ponto_a)

resultado_area = circ.area()
print(f'A área do círculo é: {resultado_area:.2f}')

# Perímetro
resultado_perimetro = circ.perimeter()
print(f'O perímetro do círculo é: {resultado_perimetro:.2f}')

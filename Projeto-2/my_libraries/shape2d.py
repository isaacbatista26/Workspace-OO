import math


class Shape():
    def __init__(self, shape):
        self.shape = shape

    def area(self, base, high):
        return base * high

    def perimeter(self, x, y):
        return ((2*x)+(2*y))

    def printCoord(self, x, y):
        print(f'({x}, {y})')


class Point():

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def updateCoord(self, x, y):
        self.x = x
        self.y = y
        self._x = self.x
        self._y = self.x
        print(f'Coordenadas atualizadas: ({x}, {y})')

    def getType(self):
        return 'Point'

    def printCoord(self, x, y):
        self._x = x
        self._y = y
        print(f'Coordenadas do ponto: ({x}, {y})')


class Line(Point):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return math.sqrt((self.point2._x - self.point1._x)**2 + (self.point2._y - self.point1._y)**2)

    def midpoint(self):
        mid_x = (self.point1._x + self.point2._x) / 2
        mid_y = (self.point1._y + self.point2._y) / 2
        return (mid_x, mid_y)


class Circle(Point, Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def getType(self):
        return 'Circle'

    def updateCoord(self, x, y, radius):
        super().updateCoord(x, y)
        self.radius = radius

    def printCoord(self):

        print(f'O círculo possui origem em: ({self.x}, {self.y})')
        print(f'E o seu raio é {self.radius}')

    def pointIn(self, point):
        distance = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        if distance <= self.radius:
            print("Ponto dentro do círculo!!")
        else:
            print("Ponto fora do círculo!!")

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter


class Square(Point, Shape):
    def __init__(self, side):
        self.side = side

    def area(self, side):
        return side*side

    def perimeter(x, y):
        return (2*x)+(2*y)


class Triangle(Point, Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self, base, high):
        return (base*high)/2

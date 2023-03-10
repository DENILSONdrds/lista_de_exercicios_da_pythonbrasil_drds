"""
 Classe Quadrado: Crie uma classe que modele um quadrado:

a. Atributos: Tamanho do lado

b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

>>> q1 = Quadrado()
>>> q1.lado
2
>>> q1.calcular_area()
4

>>> q1.mudar_valor(4)
>>> q1.lado
4
>>> q1.calcular_area()
16

>>> q2 = Quadrado(3)
>>> q2.lado
3
>>> q2.calcular_area()
9

>>> q2.mudar_valor(5)
>>> q2.lado
5
>>> q2.calcular_area()
25

"""


class Quadrado:
    def __init__(self, lado=2):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def mudar_valor(self, lado):
        self.lado = lado



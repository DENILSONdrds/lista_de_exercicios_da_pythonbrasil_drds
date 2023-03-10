"""
Classe Retangulo: Crie uma classe que modele um retangulo:

a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)

b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois,
 deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.


>>> retangulo = Retangulo(10, 5)
>>> retangulo.calcular_area()
50
>>> retangulo.calcular_perimetro()
30
>>> retangulo.mudar_lados(15, 8)
>>> retangulo.retornar_lados()
(15, 8)

>>> retangulo2 = Retangulo(2.5, 3.5)
>>> retangulo2.calcular_area()
8.75
>>> retangulo2.calcular_perimetro()
12.0
>>> retangulo2.mudar_lados(4.0, 2.0)
>>> retangulo2.retornar_lados()
(4.0, 2.0)


"""


class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lados(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def retornar_lados(self):
        return self.lado_a, self.lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)


if __name__ == '__main__':
    base = float(input('Digite a medida da base: '))
    altura = float(input('Digite a medida da altura: '))

    retangulo = Retangulo(base, altura)

    area = retangulo.calcular_area()
    perimetro = retangulo.calcular_perimetro()

    print(f'Área: {area:.2f} m²')
    print(f'Perímetro: {perimetro:.2f} m')

    tamanho_piso = float(input('Digite o tamanho do piso em metros: '))
    tamanho_rodape = float(input('Digite o tamanho do rodapé em metros: '))

    area_piso = area / tamanho_piso
    comprimento_rodape = perimetro + (2 * tamanho_rodape)

    print(f'Quantidade de pisos necessários: {area_piso:.2f}')
    print(f'Comprimento de rodapé necessário: {comprimento_rodape:.2f} m')

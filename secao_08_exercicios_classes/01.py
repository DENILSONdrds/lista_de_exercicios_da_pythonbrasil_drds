"""
Classe Bola: Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor

>>> bola1 = Bola()
>>> bola1.cor
'Azul'

>>> bola1.troca_cor('Vermelho')
>>> bola1.cor
'Vermelho'

>>> bola2 = Bola()
>>> bola2.cor
'Azul'

>>> bola2.troca_cor('Verde')
>>> bola2.cor
'Verde'

>>> bola3 = Bola()
>>> bola3.cor
'Azul'

>>> bola3.troca_cor('Amarelo')
>>> bola3.cor
'Amarelo'

"""


class Bola:
    def __init__(self):
        self.cor = 'Azul'
        self.circuferencia = 4
        self.material = 'Papel'

    def mostra_cor(self):
        return self.cor

    def troca_cor(self, cor):
        self.cor = cor


bola_primeiro = Bola()

bola_segundo = Bola()

bola_segundo.troca_cor('Amarelo')

print(bola_primeiro.cor, bola_segundo.cor)

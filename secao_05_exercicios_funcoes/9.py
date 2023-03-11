"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""


def numero_invertido():
    numero = int(input('Digite um número inteiro: '))
    numero = str(numero)
    numero = ''.join(reversed(numero))
    return numero


print(f'Número reverso: {numero_invertido()}')

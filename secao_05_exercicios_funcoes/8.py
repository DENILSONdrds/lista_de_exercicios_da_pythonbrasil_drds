"""Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""


def contar_digitos():
    numero = int(input('Digite um número inteiro: '))
    numero = str(numero)
    return len(numero)


print(f'O número informado possui {contar_digitos()} digitos.')



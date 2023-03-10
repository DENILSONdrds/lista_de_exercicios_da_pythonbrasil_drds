"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A) o produto do dobro do primeiro com metade do segundo.
B) a soma do triplo do primeiro com o terceiro.
C) o terceiro elevado ao cubo.
"""

num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input('Digite um número inteiro: '))
num_3 = float(input('Digite um número Real: '))


resp_1 = (num_1 * 2) + (num_2 / 2)

resp_2 = (num_1 * 3) + num_3

resp_3 = num_3 ** 3

print(f'O produto do dobro do primeiro com metade do segundo: {resp_1}')
print()
print(f'A soma do triplo do primeiro com o terceiro: {resp_2}')
print()
print(f'O terceiro elevado ao cubo: {resp_3}')
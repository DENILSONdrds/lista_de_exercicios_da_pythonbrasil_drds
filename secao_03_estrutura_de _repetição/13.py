"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""

base = int(input('Digite o valor de base :'))

expoente = int(input('Digite o valor do expoente :'))

potencia = base

for n in range(1, expoente):
    potencia *= base

print(f'{base} ^ {expoente} = {potencia}')

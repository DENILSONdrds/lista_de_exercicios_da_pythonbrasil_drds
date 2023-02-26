"""Faça um Programa que leia um vetor de 5 números inteiros,
mostre a soma, a multiplicação e os números.
"""

numeros = []
numero_multiplicado = 1

for numero in range(5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    numero_multiplicado *= numero


print(f'Os números são : {numeros}')
print()
print(f'A soma dos números é : {sum(numeros)}.')
print()
print(f'O resultado da multiplicação dos numeros é : {numero_multiplicado}')


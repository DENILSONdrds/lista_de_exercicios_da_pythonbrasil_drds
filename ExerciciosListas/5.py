"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
 Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
 """

numeros_pares = []
numeros_impares = []
numeros_digitados = []

for i in range(20):
    numero = int(input("Digite um número inteiro: "))
    numeros_digitados.append(numero)
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print(f'Os números digitados sao: {numeros_digitados}')
print()
print(f'Os números pares sao: {numeros_pares}')
print()
print(f'Os números impares sao: {numeros_impares}')
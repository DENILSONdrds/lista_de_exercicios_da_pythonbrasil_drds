"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""

n_1 = int(input('Digite um número: '))
n_2 = int(input('Digite outro número: '))

if n_1 < n_2:
    print(f'Os números entre o intervalo de : {n_1} e {n_2} são :')
    for n in range(n_1, n_2):
        print(n, end=', ')

elif n_1 > n_2:
    print(f'Os números entre o intervalo de : {n_2} e {n_1} são :')
    for n in range(n_2, n_1):
        print(n, end=', ')

else:
    print('Os dois números são iguais, digite números diferentes.')

"""Altere o programa anterior para mostrar no final a soma dos números.
"""

n_1 = int(input('Digite um número: '))
n_2 = int(input('Digite outro número: '))
soma = 0

if n_1 < n_2 and n_2 - n_1 != 1:
    print(f'Os números entre o intervalo de : {n_1} e {n_2} são :')
    for n in range(n_1+1, n_2):
        print(n, end=', ')
        soma += n
    print(f'E a soma deles é : {soma}.')

elif n_1 > n_2 and n_1 - n_2 != 1:
    print(f'Os números entre o intervalo de : {n_2} e {n_1} são :')
    for n in range(n_2+1, n_1):
        print(n, end=', ')
        soma += n
    print(f'E a soma deles é : {soma}.')

else:
    print('Os dois números são iguais ou não existe números entre eles, digite números diferentes.')


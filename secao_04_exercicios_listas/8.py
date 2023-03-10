"""Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

idades_pessoas = []
altura_pessoas = []

for i in range(1, 6):
    idade = int(input(f'Digite a {i}° idade: '))
    idades_pessoas.append(idade)
    altura = int(input(f'Digite a {i}° altura em cm : '))
    altura_pessoas.append(altura)

altura_pessoas.reverse()
idades_pessoas.reverse()

print(f'Idades das pessoas na ordem inversa que foi fornecida {(idades_pessoas)}')
print()
print(f'Altura das pessoas na ordem inversa que foi fornecida {(altura_pessoas)}')
"""Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""

media_aluno = []
alunos_bom = 0

for i in range(1, 11):
    print(f'{i}° aluno')
    for nota in range(4):
        nota = float(input('Digite a nota do aluno: '))
        media_aluno.append(nota)
        media = sum(media_aluno) / len(media_aluno)
    media_aluno = []
    if media >= 7:
        alunos_bom += 1

print(f'{alunos_bom} Aluno(s) com média maior ou igual a 7.0:.')

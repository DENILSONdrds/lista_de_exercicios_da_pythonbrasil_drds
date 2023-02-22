"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês.
 """

valor_hora = int(input('Digte o valor das horas: '))
horas_trabalhada = int(input('Digite a quantidade de horas trabalhada: '))

salario = valor_hora * horas_trabalhada

print(f'Seu salario no mês é : R$ {salario}.')


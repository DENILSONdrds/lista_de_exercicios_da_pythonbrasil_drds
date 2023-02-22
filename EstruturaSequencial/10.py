"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

c = float(input('Digite a temperatura em graus Celsius: '))

f = (c * 9 / 5) + 32

print(f'{c} graus Celsius é igual a {f:.2f} graus Fahrenheit. ')
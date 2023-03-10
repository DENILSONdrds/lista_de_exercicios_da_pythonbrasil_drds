""" Faça um Programa que leia um vetor de 10 caracteres,
 e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

import string

vogais = set('AEIOU')

consoantes = set(string.ascii_uppercase) - vogais
consoantes_lidas = set()
soma = 0

for caracter in range(10):
  caracter = input('Digite uma letra : ').upper()
  if caracter in consoantes:
    soma += 1
    consoantes_lidas.add(caracter)

print(f' Foram lidas: {soma} consoantes.\n As consoates lidas são: {consoantes_lidas}.')
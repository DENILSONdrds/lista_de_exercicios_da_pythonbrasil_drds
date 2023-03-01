"""Conta espaços e vogais. Dado uma ‘string’ com uma frase informada pelo usuário (incluindo espaços em branco), conte:

Quantos espaços em branco existem na frase.
Quantas vezes aparecem as vogais a, e, i, o, u.
"""


def contar_vogais_e_espaço(frase):
    # Conta espaços em branco
    qtd_espacos = frase.count(" ")

    # Conta vogais
    qtd_vogais = 0
    for letra in frase:
        if letra in "aeiouAEIOU":
            letra
            qtd_vogais += 1

    print("A frase digitada é: ", frase)
    print("Quantidade de espaços em branco: ", qtd_espacos)
    print("Quantidade de vogais: ", qtd_vogais)


if __name__ == '__main__':
    contar_vogais_e_espaço('loki o deus da mentira e da discordia')
    print()
    contar_vogais_e_espaço('Hades o deus do submundo')


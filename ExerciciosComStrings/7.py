"""Conta espaços e vogais. Dado uma ‘string’ com uma frase informada pelo usuário (incluindo espaços em branco), conte:

Quantos espaços em branco existem na frase.
Quantas vezes aparecem as vogais a, e, i, o, u.
"""


def contar_vogais_e_espacos(frase):
    # Conta espaços em branco
    qtd_espacos = frase.count(" ")

    # Conta vogais
    qtd_vogais = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for letra in frase:
        if letra in qtd_vogais:
            qtd_vogais[letra] += 1
    print(f'Quantidade de vogais: \n {qtd_vogais}')
    print(f'Quantidade espaços : {qtd_espacos}\n')
    return qtd_espacos, qtd_vogais


if __name__ == '__main__':
    contar_vogais_e_espacos('loki o deus da mentira e da discordia')
    contar_vogais_e_espacos('Hades o deus do submundo')


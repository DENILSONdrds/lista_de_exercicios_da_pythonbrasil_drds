"""Jogo de Craps. Faça um programa de implemente um jogo de Craps.
O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se,
na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado "craps" e você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
O seu objetivo agora é continuar a jogar os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""
import random
import random


def rolar_dado():
    return random.randint(1, 6) + random.randint(1, 6)


def craps():
    print("Bem-vindo ao jogo de Craps!")
    saldo = int(input("Quanto dinheiro você quer jogar? "))
    ponto = None

    while True:
        print(f"\nVocê tem ${saldo}.")
        input("Pressione Enter para jogar os dados...")
        pontos_dados = rolar_dado()
        print(f"Você jogou {pontos_dados}.")
        if ponto is None:
            if pontos_dados in (7, 11):
                print("Você ganhou!")
                saldo += 10
                break
            elif pontos_dados in (2, 3, 12):
                print("Craps! Você perdeu.")
                saldo -= 10
                break
            else:
                ponto = pontos_dados
                print(f"Seu ponto é {ponto}.")
        else:
            if pontos_dados == ponto:
                print("Você ganhou!")
                saldo += 10
                break
            elif pontos_dados == 7:
                print("Você perdeu.")
                saldo -= 10
                break
    print(f"\nFim de jogo. Sua carteira tem ${saldo}.")


craps()

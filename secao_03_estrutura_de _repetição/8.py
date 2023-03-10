"""
Exercício 08 da seção de estrutura de Repetição da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia 5 números e informe a soma e a média dos números.


    >>> soma_media([1, 2, 3, 4, 5])
    A soma dos números é: 15 e a média é: 3.0

    >>> soma_media([10, 20, 30, 40, 50])
    A soma dos números é: 150 e a média é: 30.0

    >>> soma_media([0, 0, 0, 0, 0])
    A soma dos números é: 0 e a média é: 0.0


"""


def soma_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    print(f'A soma dos números é: {soma} e a média é: {media}')


def test_soma_media():
    assert soma_media([1, 2, 3, 4, 5]) == (15, 3.0)
    assert soma_media([10, 20, 30, 40, 50]) == (150, 30.0)
    assert soma_media([0, 0, 0, 0, 0]) == (0, 0.0)
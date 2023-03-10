"""
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda
ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

def palindromo():

    >>> texto = 'OSSO'
    >>> palindromo(texto)
    'OSSO é um palíndromo!'

    >>> texto = 'OVO'
    >>> palindromo(texto)
    'OVO é um palíndromo!'

    >>> texto = 'SUBI NO ONIBUS'
    >>> palindromo(texto)
    'SUBINOONIBUS é um palíndromo!'

    >>> texto = 'A sacada da casa'
    >>> palindromo(texto)
    'ASACADADACASA é um palíndromo!'

    >>> texto = 'Teste de palindromo'
    >>> palindromo(texto)
    'TESTEDEPALINDROMO não é um palíndromo.'

"""


def palindromo(texto):
    # Remover espaços e pontuação do texto
    texto = texto.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").upper()

    # Verificar se o texto invertido é igual ao texto original
    texto_invertido = texto[::-1]
    if texto == texto_invertido:
        print(f"'{texto} é um palíndromo!'")
    else:
        print(f"'{texto} não é um palíndromo.'")

if __name__ == '__main__':
    palindromo('loki o deus da mentira')
    palindromo('arara e arara')
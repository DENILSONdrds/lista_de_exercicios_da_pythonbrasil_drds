"""
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA
e devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

    >>> data = '10/12/2000'
    >>> mes_por_extenso(data)
    10 de dezembro de 2000

    >>> data = '01/01/2010'
    >>> mes_por_extenso(data)
    01 de janeiro de 2010

    >>> data = '30/09/2020'
    >>> mes_por_extenso(data)
    30 de setembro de 2020

    >>> data = '40/02/2020'
    >>> mes_por_extenso(data)
    NULL

"""
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


def mes_por_extenso(data):
    try:
        data = datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        return print('NULL')

    return print(f"{data:%d de %B de %Y}")


if __name__ == '__main__':
    data = '12/01/2023'
    mes_por_extenso(data)
    data = '30/02/2023'
    mes_por_extenso(data)
    data = '12/22/2023'
    mes_por_extenso(data)

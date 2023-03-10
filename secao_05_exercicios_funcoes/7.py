"""Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela.
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso,
cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""


def valor_pagamento(valor_prestaçao: float, dias_atrasado: int):
    if dias_atrasado > 0:
        return valor_prestaçao + (valor_prestaçao * 0.03) + (valor_prestaçao * 0.001 * dias_atrasado)

    else:
        return valor_prestaçao


valor_prestaçao = 1
dias_atraso = 0
prestaçoes_pagas = 0
valor_total = 0

while True:
    valor_prestaçao = float(input('Digite o valor da prestaçao: '))

    if valor_prestaçao == 0:
        break
    else:
        dias_atrasado = int(input('Digite os dias de atraso: '))
        valor_pago = valor_pagamento(valor_prestaçao, dias_atrasado)
        print(f'Valor a ser pago: {valor_pago:.2f}R$')
        valor_total += valor_pago
        prestaçoes_pagas += 1

print()
print('Relatório do dia:')
print(f'Quantidade de prestações pagas: {prestaçoes_pagas}.')
print()
print(f'Valor total das prestações: {valor_total}.')

"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""


def aumento_salarial():
    salario_inicial = float(input('Informe o salario: '))
    if salario_inicial <= 280:
        aumento = 1.2
    elif 280 < salario_inicial <= 700:
        aumento = 1.15
    elif 700 < salario_inicial <= 1500:
        aumento = 1.1
    else:
        aumento = 1.05

    salario_com_aumento = aumento * salario_inicial
    percentual_aumento = (aumento / 1.0 - 1) * 100
    valor_aumento = salario_com_aumento - salario_inicial

    print(f'Salario inicial: {salario_inicial:.2f} R$\n'
          f'Percentual de aumento aplicado: {percentual_aumento:.2f} %\n'
          f'Valor do aumento: {valor_aumento:.2f} R$ \n'
          f'Novo Salário: {salario_com_aumento:.2f} R$ ')


if __name__ == '__main__':
    aumento_salarial()

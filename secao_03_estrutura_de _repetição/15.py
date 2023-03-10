"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
 Faça um programa capaz de gerar a série até o n−ésimo termo."""


n = int(input("Digite o valor de n: "))

fibonacci = [1, 1]

for i in range(2, n):
    proximo = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(proximo)

print("Sequência de Fibonacci até o {}-ésimo termo:".format(n))
for num in fibonacci:
    print(num, end=" ")
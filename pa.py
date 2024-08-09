#Questão 1 da aula 9
numa = int(input("Digite um número: "))
numb = int(input("Digite outro número: "))
soma = 0
if numa < numb:
    for x in range(numa, numb + 1):
         soma += x
    print(soma)
else:
    print("Erro")

#Questão 2 da aula 9
a = int(input("Digite o primeiro termo: "))
b = int (input("Digite a quantidade de termos: "))
r = int(input("Digite a razão: "))
s = 0
for x in range(a, b +1, r):
    s += x
print(s)
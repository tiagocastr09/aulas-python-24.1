#Questão 2 da aula 9
pt = int(input("Digite o primeiro termo: "))
qt = int (input("Digite a quantidade de termos: "))
r = int(input("Digite a razão: "))
ut = pt +(qt - 1) * r
for termo in range(pt, ut +1, r):
    print(termo)
print("Fim")

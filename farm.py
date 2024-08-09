#1. Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria (considere que o usuário informou cinco 
# medicamentos distintos). O programa deve informar o nome e o preço do medicamento mais barato, bem como a média aritmética dos 
# preços informados.

somapreco = 0
for x in range (1, 5):
    pro = input("Digite o medicamento: ")
    preco = float(input("Digite o preço do medicamento: "))
    
    maisbarat = pro
    menorpreco = preco
    somapreco += preco
if preco < menorpreco:
    maisbarat = pro
    menorpreco = preco
    somapreco += preco

media = somapreco / 5

print(f"O medicamento mais barato é {maisbarat}, e custa {menorpreco:.2f}")
print(f"A média de preço é {media:.2f}")




     
err = 0
while err < 3:
    sen = int(input("Digite sua senha: "))
    if sen == 123456:
        print("Oi User. Seja bem-vindo ao banco da phonsy!")
        break
    else: 
        # Errinho de nada veixi
        err += 1
        # Tenta ai mô

    if err <3:
        print(f"Senha incorretíssima veir! Você ainda tem {3- err} tentativas mô.")

    else: 
        print("Sua senha foi bloqueada mô! Por favor, vá a um de nossos caixas.")
        break
# SISTEMA DE AUTENTICAÇÃO

palavra_passe_correta = "1234"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    palavra_passe = input("Introduza a palavra-passe: ")

    if palavra_passe == palavra_passe_correta:
        print("Autenticação bem-sucedida! Acesso permitido.")
        break
    else:
        tentativas += 1
        tentativas_restantes = max_tentativas - tentativas

        if tentativas_restantes > 0:
            print("Palavra-passe incorrecta.")
            print("Tentativas restantes:", tentativas_restantes)
        else:
            print("Número máximo de tentativas atingido.")
            print("Acesso bloqueado!")
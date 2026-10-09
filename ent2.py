# MENU DE OPERAÇOES MATEMATICAS

print("===== MENU DE OPERAÇÕES MATEMÁTICAS =====")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma operação (1-4): "))

numero1 = float(input("Introduza o primeiro número: "))
numero2 = float(input("Introduza o segundo número: "))

match opcao:
    case 1:
        resultado = numero1 + numero2
        print("Resultado da adição:", resultado)

    case 2:
        resultado = numero1 - numero2
        print("Resultado da subtração:", resultado)

    case 3:
        resultado = numero1 * numero2
        print("Resultado da multiplicação:", resultado)

    case 4:
        if numero2 != 0:
            resultado = numero1 / numero2
            print("Resultado da divisão:", resultado)
        else:
            print("Erro: não é possível dividir por zero!")

    case _:
        print("Opção inválida! Escolha uma opção de 1 a 4.")
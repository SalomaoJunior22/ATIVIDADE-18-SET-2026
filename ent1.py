# CALCULADORA DE TROCO

valor_compra = float(input("Digite o valor da compra: R$ "))
valor_pago = float(input("Digite o valor pago: R$ "))

if valor_pago >= valor_compra:
    troco = valor_pago - valor_compra
    print(f"O troco é: R$ {troco:.2f}")
else:
    print("Valor pago insuficiente!")
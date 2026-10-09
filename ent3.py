# ANALIZE DE NUMEROS

numeros = []

for i in range(5):
    numero = float(input(f"Introduza o {i + 1}º número: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma / 5
maior = max(numeros)
menor = min(numeros)

print("\n--- Resultados da Análise ---")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
# CLASSIFICADOR DE CLIENTE

idade = int(input("Introduza a sua idade: "))
rendimento = float(input("Introduza o seu rendimento mensal em euros (€): "))

if idade < 18:
    categoria = "Bronze"
elif rendimento < 1000:
    categoria = "Prata"
elif rendimento < 2500:
    categoria = "Ouro"
else:
    categoria = "Diamante"

print("\n--- Classificação do Cliente ---")
print("Idade:", idade, "anos")
print("Rendimento mensal: €", rendimento)
print("Categoria do cliente:", categoria)
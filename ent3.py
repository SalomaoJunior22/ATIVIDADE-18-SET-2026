# CONVERSOR DE TEMPO

segundos = int(input("Digite o tempo em segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60

print(f"{horas} horas, {minutos} minutos e {segundos} segundos")
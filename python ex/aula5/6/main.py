d1 = int(input("Digite o último digito do RM"))
d2 = int(input("Digite o penúltimo digito do RM"))
campanha_ativa = ""

while campanha_ativa != "sim" and campanha_ativa != "não":
    campanha_ativa = input("Você tem campanha ativa? (sim ou não)")

dias_sem_contato = int(input("Digite a quantidade de dias de contato: "))
valor_estimado = float(input("Digite o valor do estimado: "))

limite_dias = 3 + (d1 % 5)
limite_valor = 500 + 100 * d2

print(f"Limite de dias: {limite_dias}")
print(f"Limite de valor: {limite_valor}")

if campanha_ativa == "sim" and dias_sem_contato >= limite_dias:
    print("URGENTE")
elif valor_estimado >= limite_valor or dias_sem_contato >= limite_dias:
    print("PRIORIZAR")
else:
    print("ACOMPANHAR")
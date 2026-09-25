nivel_interesse = 0

while nivel_interesse < 1 or nivel_interesse > 3:
    nivel_interesse = int(input("Digite o nível de interesse (1 a 3): "))

valor_estimado = float(input("Digite o valor do estimado: "))
dias_sem_contato = int(input("Digite quantos dias sem contato: "))

if (nivel_interesse == 3 and valor_estimado > 1000):
    print("PRIORIDADE MAXIMA")
elif (nivel_interesse == 3 or dias_sem_contato > 7):
    print("PRIORIDADE MÉDIA")
else:
    print("ACOMPANHAMENTO")



nivel_interesse = 0

while nivel_interesse < 1 or nivel_interesse > 3:
    nivel_interesse = int(input("Digite o nível de interesse (1 a 3): "))

dias_sem_contato = int(input("Digite a quantidade de dias sem contato: "))

autorizacao = ""

while autorizacao != "sim" and autorizacao != "não":
    autorizacao = input("Você tem autorização? (sim ou não): ")

# incompleto
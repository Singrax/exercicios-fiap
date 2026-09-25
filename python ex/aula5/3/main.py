dias_sem_contato = int(input("Você está há quantos dias sem contato? "))
nivel_interesse = 0

while nivel_interesse > 3 or nivel_interesse < 1:
    nivel_interesse = (input("Qual o nível de interesse? (1 a 3)"))

if (nivel_interesse == 3 or dias_sem_contato > 7):
    print("Realizar retorno")
else:
    print("Manter acompanhamento")
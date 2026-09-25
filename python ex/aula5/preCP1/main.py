#inicialização e coleta de dados
valor_estimado = float(input("Digite o valor do estimado de apoio: "))
dias_sem_contato = int(input("Digite quantos dias desde o último contato: "))
nivel_interesse = 0
tem_campanha = ""

#uso de while para loopar e perguntar novamente se não for um dos valores esperados
while nivel_interesse < 1 or nivel_interesse > 3:
    nivel_interesse = int(input("Digite o nível de interesse (1 a 3): "))
while tem_campanha != "nao" and tem_campanha != "sim":
    tem_campanha = input("Você tem campanha ativa? (sim/nao): ")

#Exibe os dados informados
print(f"Nível de interesse informado: {nivel_interesse}")
print(f"Dias sem contato: {dias_sem_contato}")
print(f"Valor estimado de apoio: R${valor_estimado:.2f}")
print(f"Campanha ativa: {tem_campanha}")

#Verificação e resultado de prioridade
if nivel_interesse == 3 and tem_campanha == "sim":
    print("Prioridade calculada: RETORNO IMEDIATO")
    print("Ação sugerida: Realizar contato hoje")
elif nivel_interesse == 3 or valor_estimado >= 5000.00:
    print("Prioridade calculada: ALTA")
    print("Ação sugerida: Preparar retorno em até 24h")
elif nivel_interesse == 2 or dias_sem_contato > 5:
    print("Prioridade calculada: MÉDIA")
    print("Ação sugerida: Agendar acompanhamento")
else:
    print("Prioridade calculada: ACOMPANHAMENTO")
    print("Ação sugerida: Manter no fluxo normal de relacionamento")




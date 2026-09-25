erros = int(input("Digite a quantidade de erros encontrados no programa"))

if erros < 0:
    print("Entrada invalida")
elif erros == 0:
    print("Sistema estável")
elif erros <= 5:
    print("Ajustes necessários")
else:
    print("Sistema crítico")

latencia = int(input("Qual o tempo de resposta da API"))

if latencia <= 100:
    print("Excelente")
elif latencia <= 300:
    print("Aceitável")
elif latencia <= 800:
    print("Lento")
else:
    print("Crítico")
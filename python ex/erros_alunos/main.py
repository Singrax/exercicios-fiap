erros = int(input("Quantos erros tem no sistema?"))

if erros == 0:
    print("Sistema estável")
elif erros <= 5:
    print("Ajustes necessários")
else:
    print ("Sistema crítico")
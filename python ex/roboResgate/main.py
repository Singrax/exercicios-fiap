bateria = float(input("Bateria do robô (%): "))
temperatura = float(input("Temperatura do motor (°C): "))
rota = input("Rota bloqueada (sim/não): ")

if bateria < 25:
    print("Missão cancelada: bateria insuficiente")
else:
    if temperatura > 80:
        print("Missão cancelada: superaquecimento")
    else:
        if rota == "sim":
            print("Missão autorizada com atenção: rota bloqueada")
        else:
            print("Missão autorizada")
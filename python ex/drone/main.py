bateria = float(input("Bateria do drone (%): "))
vento = float(input("Velocidade do vento (km/h): "))
peso = float(input("Peso da carga (kg): "))

if bateria < 30:
    print("Missão cancelada: bateria insuficiente")
else:
    if vento > 40:
        print("Missão cancelada: vento forte")
    else:
        if peso > 5:
            print("Missão autorizada com alerta: carga pesada")
        else:
            print("Missão autorizada")
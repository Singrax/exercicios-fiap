totalReg = int(print("Digite o número total de registros:"))
availableServers = int(print("Digite os servidores disponíveis"))

if totalReg == 0 or availableServers == 0:
    print("Operação inválida, quantidade de servidores igual a zero")
else:
    regPerServer = totalReg / availableServers
    print("Cada servidor deverá processar", regPerServer, "registros")





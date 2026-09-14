print("Bem vindo ao sistema LaunchGuard!")

#Entrada de dados
usuariosPrevistos = int(input("Usuários previstos:"))
servidoresDisp = int (input("Quantidade de servidores disponiveis:"))
capacidadeMax = int(input("Capacidade de usuários por servidor:"))
latenciaAtual = float(input("Latência atual do servidor em ms:"))
errosCriticos = int(input("Erros criticos encontrados:"))
usoAtual = int(input("Porcentagem do uso atual do disco do servidor:"))

#Calcular e resultado dos servidores/usuario

if servidoresDisp == 0:
    print("LANÇAMENTO BLOQUEADO: Não existem servidores disponiveis")
else:
    usuariosPorServidor = usuariosPrevistos / servidoresDisp
    print("Capacidade prevista por servidor: " + str(usuariosPorServidor))
    if usuariosPorServidor > capacidadeMax:
        print("LANÇAMENTO BLOQUEADO: Capacidade insuficiente")
    elif errosCriticos >= 1:
        print ("LANÇAMENTO BLOQUEADO: Erro crítico encontrado")
    elif latenciaAtual > 300:
        print("LANÇAMENTO ADIADO: desempenho precisa ser evitado")
    elif usoAtual > 90:
        print("LANÇAMENTO COM ALERTA: pouco espaço disponivel")
    else:
        print("LANÇAMENTO AUTORIZADO")










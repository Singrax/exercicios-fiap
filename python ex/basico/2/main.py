import math

initialUsers = int(input("Digite quantidade de usuários iniciais:"))
months = int(input("Digite quantos meses:"))

print("Crescimento:")

result = initialUsers * int(math.pow(2, months))

print ("Total de usuários após", months, "meses é", result)


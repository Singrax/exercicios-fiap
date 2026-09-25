autorizacao = ""
telefone_cadastrado = ""

while autorizacao != "sim" and autorizacao != "não":
    autorizacao = input("Você tem autorização de contato? (sim ou não)")

while telefone_cadastrado != "sim" and telefone_cadastrado != "não":
    telefone_cadastrado = input("Existe um telefone cadastrado? (sim ou não)")

if telefone_cadastrado == "sim" and autorizacao == "sim":
    print("Contato liberado")
else:
    print("Contato não liberado")

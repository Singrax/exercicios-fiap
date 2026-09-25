autorizacao = ""
tem_email = ""
tem_whatsapp = ""

while tem_email != "sim" and tem_email != "não":
    tem_email = input("Você tem e-mail de contato? (sim ou não)")

while tem_whatsapp != "sim" and tem_whatsapp != "não":
    tem_whatsapp = input("Você tem whatsapp? (sim ou não)")

while autorizacao != "sim" and autorizacao != "não":
    autorizacao = input("Você tem autorização de contato? (sim ou não)")

if (autorizacao == "sim" and (tem_email == "sim" or tem_whatsapp == "sim")):
    print("Cadastro pronto")
else:
    print("Cadastro incompleto")
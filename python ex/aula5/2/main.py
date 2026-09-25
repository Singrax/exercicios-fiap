tem_email = ""
tem_whatsapp = ""

while tem_email != "sim" and tem_email != "não":
    tem_email = input("Você tem e-mail de contato? (sim ou não)")

while tem_whatsapp != "sim" and tem_whatsapp != "não":
    tem_whatsapp = input("Você tem whatsapp? (sim ou não)")

if tem_email == "sim" or tem_whatsapp == "sim":
    print("Contato possível")
else:
    print("Sem canal digital")

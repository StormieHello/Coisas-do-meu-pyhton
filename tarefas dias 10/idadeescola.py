ida=int(input("Me diga o nome do seu filho, pra eu saber em qual série ele irá ficar "))

if ida<6:
    print("Ele vai pra edudação infantil")
if ida>=6 and ida<11:
    if ida<8:
        print("Fundamental I")
    else:
        print("Fundamental I avançado")
if ida>=11:
    print("Fundamental II ou superior!")
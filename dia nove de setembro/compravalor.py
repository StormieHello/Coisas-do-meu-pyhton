val=int(input("Me diga o valor da sua compra, filho! "))

if val>0 and val<=100:
    if val<50:
        print("Gastou pouco, filhão")
    else:
        print("Gastou até que bastante hein.")
elif val>100:
    print("MEU DEUS VOCÊ ESTOUROU O LIMITE DO MEU CARTÃO")
else:
    print("Não entendi filho.")
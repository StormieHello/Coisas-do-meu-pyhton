nota=int(input("Filho, me diga sua nota. "))

if nota>=7:
    print("Tá bom.")
    if nota>9:
        print("Com mérito.")
            
elif nota>4 and nota<7:
    print("Tá de recuperação...")
else:
    print("Filho... você vai reprovar.")
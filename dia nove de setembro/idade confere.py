id=int(input("Hey! Preciso saber sua idade antes de você entrar! "))

if id>17:
    doc=input("Tem documento pra comprovar? ")
    if doc=="s":
        print("Pode entrar!")
    elif doc=="n":
        print("Hoje não!")
else:
    print("Hoje não!")
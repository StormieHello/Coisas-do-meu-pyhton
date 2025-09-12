sen=int(input("Digite sua senha: "))

if sen>8:
    if any(char.isdigit() for char in sen):
        print("A senha está forte!")
    else:
        print("Preciso de números")
else:
    print("Senha fraca")

senh=input("Digite uma senha: ")
qtd=len(senh)

if qtd>=8:
    if any(char.isdigit() for char in senh) & any(char.isalpha() for char in senh):
        print("A senha é forte")
    else:
        print("Senha média")
else:
    print("Senha fraca")
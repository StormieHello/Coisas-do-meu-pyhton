log=input("Me informe o login.")

if log=="admin":
    sen=int(input("Agora me diga a senha."))
    if sen==12345:
        print("Acesso garantido")
    else:
        print("Acesso negado.")
else:
    print("Usúario negado.")
        
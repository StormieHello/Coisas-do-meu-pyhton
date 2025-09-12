idade = int(input("Qual sua idade? "))

if idade<18:
    print("Sai daqui moleque!")
elif idade>17 and idade<65:
    print("Pode entrar, sim senhor.")
elif idade>64:
    print("O senhor tem que entrar pela porta de ídosos!")
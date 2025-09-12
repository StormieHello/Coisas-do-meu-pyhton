ida=int(input("Qual sua idade? "))

if ida>15:
    if ida>17 and ida<71:
        print("Voto obrigatório")
    else:
        print("Voto facultativo")
else:
    print("Você tem que esperar um pouco ainda")
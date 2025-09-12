lim=int(input("Você sabe quantos por hora você estava indo? "))

if lim>60:
    if lim<=80:
        print("Atenção, cidadão, leve multa.")
    elif lim>80:
        print("Vou ter que guinchar seu carro, amigo.")
else:
    print("Ata, tudo bem amigo.")
velo=int(input("Qual a velocidade que você está indo! "))

if velo<=60:
    print("Dentro do limite, cidadão")
if velo>60:
    if velo<=80:
        print("Só uma multa pra você ficar esperto.")
    else:
        print("Vou ter que guinchar seu carro")
        
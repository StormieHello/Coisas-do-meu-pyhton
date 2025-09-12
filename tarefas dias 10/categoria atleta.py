idade = int(input("Qual sua idade, campeão? "))

if idade<12:
    print("Você está na categoria infantil, jovem!")
elif idade>=13 and idade<=17:
    print("Você está na categoria juvenil, jovem!")
elif idade>=18 and idade<=40:
    print("Você está na categoria adulta, campeão!")
else:
    print("Você está na categoria master, senhor!")
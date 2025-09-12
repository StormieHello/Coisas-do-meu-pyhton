n1 = int(float(input("Qual sua primeira nota? ")))
n2 = int(float(input("Qual sua segunda nota? ")))
n3 = int(float(input("Qual sua terceira nota? ")))
media = (n1+n2+n3)/3
print("Sua primeira nota foi: ",n1)
print("Sua segunda nota foi: ",n2)
print("Sua terceira nota foi: ",n3)
print(f"E por fim a sua media final foi: {media:.2f}")

"esse f ai é aquele do float, tem que constatar ele antes da frase se tiver uma, e aquela conta na media é pra formatar ele pra duas casas decimais."

if media>=7:
    print("Você passou de ano, parabéns.")
elif media>=3:
    print("Aluno em recuperação.")
else:
    print("Você está reprovado.")
n1 = int(input("Beep boop, robo calculadora rudimentar, me diga o primeiro número! "))
n2 = int(input("Beep boop, robo calculadora rudimentar, me diga o segundo número! "))
fator = input("Agora me diga que operação devo fazer! div, soma, mult ou sub? ")
div = n1/n2
soma = n1+n2
mult = n1*n2
sub = n1-n2


if fator=="div":
    print(f"ESTE É O RESULTADO DA SUA DIVISÃO! {div}")
elif fator=="soma":
    print(f"ESSE É O VALOR DA SUA SOMA! {soma}")
elif fator=="mult":
    print(f"ESSE É O VALOR DA SUA MULTIPLICAÇÃO! {mult}")
elif fator=="sub":
    print(f"ESSE É O VALOR DA SUBTRAÇÃO! {sub}")
else:
    print("NÃO ENTENDI TENTE DE NOVO!")
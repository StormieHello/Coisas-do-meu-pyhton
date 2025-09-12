temp = int(input("Qual a temperatura de hoje senhor(a)? "))

if temp<10:
    print("Tá muito frio hoje hein?!")
elif temp>=10 and temp<=18:
    print("Tá frio hoje!")
elif temp>=19 and temp<=25:
    print("Está bem agrádavel hoje!")
elif temp>=26 and temp<=35:
    print("Está quente hoje hein!")
else:
    print("Está fervendo hoje!!")
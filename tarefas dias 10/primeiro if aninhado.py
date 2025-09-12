a=int(input("Me diga um número "))

if a>0:
    print(a, "é positivo")
    if a%2==0:
        print(a, "é par")
    else:
        print(a, "é impar")
else:
    print(a, "é negativo")
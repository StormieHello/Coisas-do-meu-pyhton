a=int(input("Digite o valor do primeiro número"))
b=int(input("Digite o valor do segundo número"))
c=int(input("Digite o valor do terceiro número"))

if a<(b+c) and b<(a+c) and c<(a+b):
    if a==b==c:
        print("Forma um equilatero")
    elif a==b or b==c or a==c:
        print("Forma um isosceles")
    else:
        print("Formam um escaleno")
else:
    print("Não formam um triangulo")


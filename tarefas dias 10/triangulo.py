a=int(input("Me informe três números e eu verei se os três conseguem formar um triângulo, que tipo, ou, se não formam, me diga o primeiro número "))
b=int(input("Me diga o segundo número "))
c=int(input("Me diga o terceiro número "))

if a==b==c:
    print("Estes números conseguem formar um triângulo, e eles serão equilátero")
elif a==b or b==c or a==c:
    print("Estes números conseguem formar um triângulo, e eles serão isósceles")
elif a+b>c or b+c>a or a+c>b:
    print("Estes números não conseguem formar um triângulo.")
else:
    print("Estes números conseguem formar um triângulo, e eles serão escaleno")
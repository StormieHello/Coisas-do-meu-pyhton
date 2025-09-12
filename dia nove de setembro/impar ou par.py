n=int(input("Me diga um número! "))

if n>0:
    print("Este número é positivo")
    if n%2==0:
      print("Este número é positivo e par")
    elif n%2!=0:
      print("Este número é impar")
    
elif n==0:
    print("Este número É 0")
else:
    print("Este número é negativo.")
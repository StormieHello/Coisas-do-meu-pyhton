a="aeiouAEIOU"
b=input("Me digite uma palavra e eu direi quantas vogais ela tem! ")
contador=0
for vogais in b:
    if vogais in a:
        contador+=1
print(f"Esta palavra tem: {contador} vogais")

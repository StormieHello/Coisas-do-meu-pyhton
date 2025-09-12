preco=int(input("Qual foi o valor que você pegou de produtos? Para eu avaliar o desconto! "))
desc10=preco*0.10
desc20=preco*0.20

if preco<=100:
    print("Desculpe! Mas sem desconto desta vez!")
elif preco>100 and preco<501:
    print(f"O seu desconto será de 10%! Aqui o está o o total do desconto: {desc10} e seu preço total ficou:  {preco-desc10}")
else:
    print(f"Nossa! Hoje você vai levar um desconto de 20%! O total do desconto foi: {desc20} e seu preço total ficou: {preco-desc20}")
alt=float(input("Qual sua altura em cm? "))
peso=float(input("Qual seu peso? "))
imc=peso/(alt*alt)

if imc<18.5:
    print(f"Tá precisando colocar uns quilinhos! Está abaixo do peso! Seu imc foi de: {imc:.2f} ")
elif imc>=18.5 and imc<=24.9:
    print(f"Parabéns, tá normal. Seu imc foi de: {imc:.2f}")
elif imc>=25 and imc<=29.9:
    print(f"Opa, tá precisando perder uns quilos! Você está sobrepeso! Seu imc está como: {imc:.2f}")
else:
    print(f"Tá precisando se cuidar mais! Você está obeso! Seu imc está constando {imc:.2f}")
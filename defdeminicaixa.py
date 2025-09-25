def menu():
    print("           MINI CAIXA ELETRÔNICO        ")
    print("1. Consultar saldo")
    print("2. Depósito")
    print("3. Saque")
    print("4. Sair")
    
saldo=0.0

def consultar_saldo():
    return saldo

def deposito(valor):
    global saldo
    saldo+=valor
    return saldo

def saque(valor):
    global saldo
    if valor>saldo:
        print("Saldo negativo")
    else:
        saldo-=valor
        print("Saque realizado com sucesso")
        return saldo

def tudo():
    menu()
    opcao=int(input("Escolha a operação: (1) (2) (3) (4):\n"))
        
    if opcao==4:
        print("Consulta encerrada.")
        quit()
    elif opcao==1:
        print(f"Saldo R$:{consultar_saldo():.2f}")
    elif opcao==2:
        dep=float(input("Informe o valor a ser depositado R$:\n"))
        deposito(dep)
        print(f"Depósito de R$:{dep} realizado com sucesso!\n Seu saldo atual é {saldo}")
    elif opcao==3:
        saq=float(input("Informe o valor a ser sacado R$:\n"))
        saque(saq)
    else:
        print("Opção inválida")
    tudo()

tudo()
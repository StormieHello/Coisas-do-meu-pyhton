def menu():
    print("Olá senhor(a), sou o bot de listas versão 1.0. Pronto para o serviço.")
    print("1) Para ADICIONAR algo a lista.")
    print("2) Para EXCLUIR algo da lista.")
    print("3) Para mostrar a LISTA.")
    print("4) Para LIMPAR a lista.")
    print("5) Para Sair.")

compras=[]

def ad_lista(item):
    global compras
    compras.append(item)
    return compras

def sub_lista(item):
    global compras
    compras.remove(item)
    return compras

def lim_lista():
    compras.clear()


def sistema():
    menu()
    pergunta=int(input("Escolha o que deseja fazer! "))
    if pergunta==5:
        print("Serviço encerrado!")
    elif pergunta==1:
        add=input("Informe o item para colocar na lista! ")
        ad_lista(add)
        print(f"Feito! O item {add} foi adicionado a sua lista.")
        print("=====================================================")
    elif pergunta==2:
        sub=input("Informe o item que você quer excluir da lista! ")
        if sub not in compras:
            print("Este item não está na sua lista.")
        else:
            sub_lista(sub)
            print(f"Feito! O item {sub} foi excluído da sua lista.")
        print("=====================================================")
    elif pergunta==3:
        print("Sua lista:")
        for x in compras:
            print(x)
            print("=====================================================")
    elif pergunta==4:
        print("Limpando sua lista!")
        lim_lista()
    sistema()
sistema()

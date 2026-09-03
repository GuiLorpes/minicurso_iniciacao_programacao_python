executar = True
compras = []
while executar:

    print("* - - Lista de compras - - *")
    print("1) Adicionar")
    print("2) Remover")
    print("3) Mostrar")
    print("4) Sair")

    opcao = int(input("Escolha uma opção:"))
    if opcao == 1:
            item = input("Oque você quer comprar?")
            compras.append(item)
    elif opcao == 2:
            item = input("Oque você quer remover?")
            if compras.__contains__(item):
                compras.remove(item)
                print("Você removeu "+item)
            else:
                print("Não tem")
    elif opcao == 3:
            print(compras)
    else:
            executar = False
            print("Você comprou tudo")

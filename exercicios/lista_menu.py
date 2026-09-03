executar: bool = True

while executar:
    #print("-- Lista de Compras --\n1) Add Item\n2) Remover Item\n3) Mostrar Item\n0) Sair")
    print("-- Lista de Compras --")
    print("1) Adicionar item")
    print("2) Remover item")
    print("3) Mostrar lista")
    print("0) Sair")
    comando: int = int(input("Digite o numero da opção: "))
    match comando:
        case 1:
            print('Um item foi adicionado!')
        case 2:r
            print('Um item foi removido!')
        case 3:
            print('A lista foi mostrada!')
        case 0:
            executar = False
            print('Encerrando programa...')
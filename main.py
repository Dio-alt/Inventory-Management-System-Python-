from estoque import Inventory


def show_menu():
    print("
" + "=" * 35)
    print("      SISTEMA DE ESTOQUE")
    print("=" * 35)
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar estoque")
    print("4 - Remover produto")
    print("0 - Sair")


def main():
    inventory = Inventory()

    while True:
        show_menu()
        option = input("Escolha uma opção: ").strip()

        if option == "1":
            name = input("Nome do produto: ")

            try:
                quantity = int(input("Quantidade: "))
                inventory.add_product(name, quantity)
            except ValueError:
                print(" Quantidade inválida.")

        elif option == "2":
            inventory.list_products()

        elif option == "3":
            inventory.list_products()
            try:
                index = int(input("Índice do produto: "))
                quantity = int(input("Nova quantidade: "))
                inventory.update_product(index, quantity)
            except ValueError:
                print(" Entrada inválida.")

        elif option == "4":
            inventory.list_products()
            try:
                index = int(input("Índice do produto para remover: "))
                inventory.remove_product(index)
            except ValueError:
                print(" Entrada inválida.")

        elif option == "0":
            print(" Encerrando sistema...")
            break

        else:
            print(" Opção inválida.")


if __name__ == "__main__":
    main()

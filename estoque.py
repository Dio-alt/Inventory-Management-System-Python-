class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, quantity):
        product = {
            "name": name.strip().title(),
            "quantity": quantity
        }
        self.products.append(product)
        print(f" Produto '{product['name']}' adicionado com sucesso.")

    def list_products(self):
        if not self.products:
            print(" Nenhum produto cadastrado.")
            return

        print("
 Lista de produtos:")
        for index, product in enumerate(self.products):
            print(f"{index} - {product['name']} (Qtd: {product['quantity']})")

    def update_product(self, index, quantity):
        try:
            product = self.products[index]
            product["quantity"] = quantity
            print(f" Estoque de '{product['name']}' atualizado.")
        except IndexError:
            print(" Produto não encontrado.")

    def remove_product(self, index):
        try:
            removed = self.products.pop(index)
            print(f" Produto '{removed['name']}' removido.")
        except IndexError:
            print(" Produto não encontrado.")

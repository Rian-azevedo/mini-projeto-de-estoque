from classes.estoque import Estoque
from banco import cursor

class Comandos:
    def cadastro(self):
        nome = input("Nome do produto: ")
        codigo = int(input("Código: "))
        quantidade = int(input("Quantidade: "))

        produto = Estoque(nome, codigo, quantidade)
        produto.salvar_produtos()
        print("produto cadastrado com sucesso")

    def atualizar(self):
        id_produto = int(input("ID do produto: "))
        nome = input("Novo nome: ")
        codigo = int(input("Novo código: "))
        quantidade = int(input("Nova quantidade: "))

        produto = Estoque(nome, codigo, quantidade, id_produto)
        produto.atualizar_produtos()
        print("produto atualizado com sucesso")

    def deletar(self):
        try:
            id_produto = int(input("ID do produto para deletar: "))
            Estoque.deletar_produto_por_id(id_produto)
        except ValueError:
            print("ID inválido.")

    @staticmethod
    def mostra_produtos():
        Estoque.mostra_produtos()
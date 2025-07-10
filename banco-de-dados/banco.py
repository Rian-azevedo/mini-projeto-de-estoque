import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS estoque(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               codigo INTEGER NOT NULL,
               quantidade INTEGER NOT NULL
               )
               """)
conexao.commit()



class Estoque:
    def __init__(self, nome, codigo, quantidade, id=None):
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
        self.id = id

    def salvar_produtos(self):
        cursor.execute("INSERT INTO estoque(nome, codigo, quantidade) values(?, ?, ?)",
                        (self.nome, self.codigo, self.quantidade))
        conexao.commit()

    @staticmethod
    def mostra_produtos():
        cursor.execute("SELECT * FROM estoque")
        for linha in cursor.fetchall():
            print(linha)

    def atualizar_produtos(self):
        if self.id is None:
            print("precisa ser um id valido")
            return
        cursor.execute("""UPDATE estoque
                           set nome = ?, codigo = ?,
                           quantidade = ? where id = ?""",
                           (self.nome, self.codigo, self.quantidade, self.id))
        conexao.commit()
         
    @staticmethod
    def deletar_produto_por_id(id):
        cursor.execute("DELETE FROM estoque WHERE id = ?", (id,))
        conexao.commit()
        print(f"Produto com o ID {id} deletado com sucesso.")


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
        cursor.execute("SELECT * FROM estoque")
        for linha in cursor.fetchall():
            print(linha)


comandos = Comandos()

print(f"1 cadastrar\n 2 mostrar\n 3 atualizar\n 4 deletar\n 5 sair\n")

while True:
    try:
        valor = int(input("Digite um número: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        continue
    
    if valor == 1:
        comandos.cadastro()
    elif valor == 2:
        comandos.mostra_produtos()
    elif valor == 3:
        comandos.atualizar()
    elif valor == 4:
        comandos.deletar()
    elif valor == 5:
        break
    else:
        print("Opção inválida.")

conexao.close()
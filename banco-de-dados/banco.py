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
    def mostra_produtos(self):
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
         
    def deletar_produto(self):
        if self.id is None:
            print("precisa ser um id valido")
            return
        else:
            cursor.execute("DELETE FROM estoque WHERE id = ?", (self.id,))
            print(f"produto com o id {self.id} deletado com sucesso")
            conexao.commit()


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
        id_produto = int(input("ID do produto para deletar: "))
        produto = Estoque(None, None, None, id_produto)
        produto.deletar_produto()

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
        Comandos.cadastro()
    elif valor == 2:
        Comandos.mostra_produtos()
    elif valor == 3:
        Comandos.atualizar()
    elif valor == 4:
        Comandos.deletar()
    elif valor == 5:
        break

conexao.close()
from banco import conexao, cursor

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
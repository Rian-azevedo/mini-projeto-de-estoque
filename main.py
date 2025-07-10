from classes.comandos import Comandos
from banco import conexao

comandos = Comandos()

while True:
    print(f"\n1 cadastrar\n2 mostrar\n3 atualizar\n4 deletar\n5 sair\n")
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
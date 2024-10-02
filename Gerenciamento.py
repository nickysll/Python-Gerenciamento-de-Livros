# A. Mensagem de boas-vindas
print("Bem-vindo ao Sistema de Gerenciamento de Livros de Nicoly Moreira")

# B. Lista vazia e variável global
lista_livro = []
id_global = 0

# C. Função para cadastrar livro
def cadastrar_livro(id):
    global id_global
    id_global += 1
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    editora = input("Digite o nome da editora do livro: ")
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(livro)

# D. Função para consultar livro
def consultar_livro():
    opcao = int(input("Qual opção deseja?\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Autor\n4. Retornar ao menu\n"))
    if opcao == 1:
        for livro in lista_livro:
            print(livro)
    elif opcao == 2:
        id_consulta = int(input("Digite o Id do livro: "))
        for livro in lista_livro:
            if livro["id"] == id_consulta:
                print(livro)
    elif opcao == 3:
        autor_consulta = input("Digite o nome do autor: ")
        for livro in lista_livro:
            if livro["autor"] == autor_consulta:
                print(livro)
    elif opcao == 4:
        return
    else:
        print("Opção inválida")

# E. Função para remover livro
def remover_livro():
    id_remover = int(input("Digite o Id do livro a ser removido: "))
    for livro in lista_livro:
        if livro["id"] == id_remover:
            lista_livro.remove(livro)
            print("Livro removido com sucesso.")

# F. Estrutura de menu principal
while True:
    print("\nMENU:")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")

    opcao_menu = int(input("Escolha uma opção: "))

    if opcao_menu == 1:
        cadastrar_livro(id_global)
    elif opcao_menu == 2:
        consultar_livro()
    elif opcao_menu == 3:
        remover_livro()
    elif opcao_menu == 4:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida")

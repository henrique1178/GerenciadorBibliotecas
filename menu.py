from biblioteca import *

carregar_biblioteca()

while True:
    print("\n=== MENU ===")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Verificar Disponibilidade")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            copias = int(input("Digite a quantidade de cópias: "))
            print(adicionar_livro(titulo, autor, copias))

        case '2':
            livros = listar_livros()
            if livros:
                print("\n=== LISTAR LIVROS ===")
                for i, livro in enumerate(livros, 1):
                    print(f"{i}. Título: {livro['Titulo']}, Autor: {livro['Autor']}, Cópias: {livro['Quantidade de Copias']}")
            else:
                print("Não há livros disponíveis.")

        case '3':
            livros = listar_livros()
            if livros:
                try:
                    escolha = int(input("Digite o número do livro que deseja emprestar: ")) - 1
                    if 0 <= escolha < len(livros):
                        print(gerenciar_emprestimos(livros[escolha], 'emprestar'))
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há livros disponíveis para emprestar.")

        case '4':
            livros = listar_livros()
            if livros:
                try:
                    escolha = int(input("Digite o número do livro que deseja devolver: ")) - 1
                    if 0 <= escolha < len(livros):
                        print(gerenciar_emprestimos(livros[escolha], 'devolver'))
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            else:
                print("Não há livros disponíveis para devolver.")

        case '5':
            titulo = input("Digite o título do livro que deseja verificar: ")
            livro = verificar_disponibilidade(titulo)
            if livro:
                print(f"O livro '{livro['Titulo']}' de {livro['Autor']} tem {livro['Quantidade de Copias']} cópias disponíveis.")
            else:
                print(f"O livro '{titulo}' não foi encontrado.")

        case '6':
            print("Saindo do sistema. Até logo!")
            break

        case _:
            print("Opção inválida. Tente novamente.")
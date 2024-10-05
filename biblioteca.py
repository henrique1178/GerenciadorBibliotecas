import json
import os

ARQUIVO_BIBLIOTECA = 'biblioteca.json'
biblioteca = []

def carregar_biblioteca():
    global biblioteca
    if os.path.exists(ARQUIVO_BIBLIOTECA):
        with open(ARQUIVO_BIBLIOTECA, 'r') as f:
            biblioteca = json.load(f)

def salvar_biblioteca():
    with open(ARQUIVO_BIBLIOTECA, 'w') as f:
        json.dump(biblioteca, f)

def adicionar_livro(titulo: str, autor: str, copias: int):
    livro = {'Titulo': titulo, 'Autor': autor, 'Quantidade de Copias': copias}
    biblioteca.append(livro)
    salvar_biblioteca()
    return f"Livro '{titulo}' de {autor} adicionado com {copias} cópias."

def listar_livros():
    return biblioteca 

def gerenciar_emprestimos(livro, acao: str):
    if acao == 'emprestar':
        if livro['Quantidade de Copias'] > 0:
            livro['Quantidade de Copias'] -= 1
            salvar_biblioteca()  # Salva a biblioteca após a alteração
            return f"Você emprestou '{livro['Titulo']}'. Cópias restantes: {livro['Quantidade de Copias']}"
        else:
            return f"O livro '{livro['Titulo']}' não tem cópias disponíveis."
    elif acao == 'devolver':
        livro['Quantidade de Copias'] += 1
        salvar_biblioteca()  # Salva a biblioteca após a alteração
        return f"Você devolveu '{livro['Titulo']}'. Cópias disponíveis: {livro['Quantidade de Copias']}"
    
def verificar_disponibilidade(titulo):
    for livro in biblioteca:
        if livro['Titulo'].lower() == titulo.lower():
            return livro
    return None

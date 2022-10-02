"""
Sistema de gerenciamento de informações de filmes
"""

import os
import string
import sys
from unidecode import unidecode

def carregar_arquivo() -> list[list]:
    """
    Abre o arquivo .txt que contém as informações dos filmes
    """
    # Verifica o tamanho do arquivo .txt para saber se está vazio
    tamanho_arquivo = os.path.getsize("filmes.txt")

    if tamanho_arquivo == 0:
        lista_filmes = []
        return lista_filmes

    with open("filmes.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    lista_filmes = [linha.strip().split(',') for linha in linhas]
    return lista_filmes

def salvar_arquivo(lista_filmes: list[list]) -> None:
    """
    Salva as informações dos filmes, adicionados durante a execução do programa, em um arquivo .txt
    """
    with open("filmes.txt", "w", encoding="utf-8") as arquivo:
        for filme in lista_filmes:
            # Escreve no arquivo .txt os elementos da lista separados por virgula
            arquivo.writelines(','.join(filme))

def exibir(filmes: list[list]) -> None:
    """
    Exibe as informações dos filmes cadastrados
    """

    if len(filmes) == 0:
        print('Sem Filmes Cadastrados\n')

    i = 1
    for filme in filmes:
        print(f"{i} - Título: {filme[0]}")
        print(f'    Ano de Lançamento: {filme[1]}')
        print(f'    Gênero: {filme[2]}')
        print('='*100 + '\n')
        i += 1

def adicionar(filmes: list[list]) -> None:
    """
    Cadastra um novo filme
    """

    filme = []
    filme.append(input('Nome: '))
    filme.append(input('Ano: '))
    filme.append(input('Gênero: '))
    filmes.append(filme)

def remover(filmes: list[list]) -> None:
    """
    Remove um filme cadastrado
    """

    if len(filmes) == 0:
        return

    while True:
        indice = input('Digite o índice do filme a ser removido: ')

        if indice.isdigit():
            indice = int(indice) - 1
            if 0 <= indice < len(filmes):
                del filmes[indice]
                os.system('cls')
                print('Filme Deletado com Sucesso!\n')
                break

            os.system('cls')
            print('Não existe filme cadastrado no indice digitado.')
            input('\nPressione Enter para continuar')
            os.system('cls')

        else:
            os.system('cls')
            input('Caractere inválido.\nPressione Enter para continuar')
            os.system('cls')

def pesquisar(lista_filmes: list[list]) -> None:
    """
    Função que procura filmes relacionados a uma palavra-chave digitada pelo usuário
    """

    if len(lista_filmes) == 0:
        print('Sem Filmes Cadastrados\n')

    else:
        resultados = []
        palavra = input('Digite uma palavra chave: ')
        print('\n')

        for filme in lista_filmes:
            if unidecode(palavra.lower()) in unidecode(filme[0].lower()):
                resultados.append(filme[:])

            elif unidecode(palavra.lower()) in unidecode(filme[1].lower()):
                resultados.append(filme[:])

            elif unidecode(palavra.lower()) in unidecode(filme[2].lower()):
                resultados.append(filme[:])

        if len(resultados) == 0:
            print('Não foi possível encontrar o filme.')

        else:
            exibir(resultados)

def opcao_exibir(lista_filmes: list[list]) -> None:
    """
    Primeira opcao do menu
    """

    os.system('cls')
    exibir(lista_filmes)
    input('\nPressione Enter para voltar ao menu principal')

def opcao_pesquisar(lista_filmes: list[list]) -> None:
    """
    Segunda opcao do menu
    """

    controle = 0
    while True:
        os.system('cls')

        if controle == 0:
            pesquisar(lista_filmes)

        subop = validador_de_entrada('pesquisar')
        if subop == 1:
            controle = 0
        elif subop == 2:
            os.system('cls')
            break
        else:
            controle = 1
            opcao_default()

def opcao_adicionar(lista_filmes: list[list]) -> None:
    """
    Terceira opcao do menu
    """

    controle = 0
    while True:
        os.system('cls')

        if controle == 0:
            adicionar(lista_filmes)
            os.system('cls')
            print('Filme Cadastrado com Sucesso!\n')

        subop = validador_de_entrada('cadastrar')
        if subop == 1:
            controle = 0

        elif subop == 2:
            os.system('cls')
            break

        else:
            controle = 1
            opcao_default()

def opcao_remover(lista_filmes: list[list]) -> None:
    """
    Quarta opcao do menu
    """

    controle = 0
    while True:
        os.system('cls')

        if controle == 0:
            exibir(lista_filmes)
            remover(lista_filmes)

        subop = validador_de_entrada('deletar')
        if subop == 1:
            controle = 0

        elif subop == 2:
            os.system('cls')
            break

        else:
            controle = 1
            opcao_default()

def opcao_encerrar(lista_filmes: list[list]) -> None:
    """
    Quinta opcao do menu
    """
    os.system('cls')
    salvar_arquivo(lista_filmes)
    sys.exit()

def opcao_default() -> None:
    """
    Opcao default do menu
    """

    os.system('cls')
    print('Opção inválida')
    input('\nPressione Enter para voltar ao menu anterior')

def menu(menu_tipo: string) -> None:
    """
    Exibe menu principal ou submenus
    """

    if menu_tipo == 'principal':
        titulo = '          PyFilmes          '
        os.system('cls')
        print(f"{'':*^30s}")
        print(f"{titulo:*^30s}")
        print(f"{'':*^30s}")
        print('\n\t1 : Catálogo')
        print('\t2 : Pesquisar')
        print('\t3 : Cadastrar')
        print('\t4 : Deletar')
        print('\t5 : Sair\n')

    elif menu_tipo == 'pesquisar':
        print('\n1 : Pesquisar Novamente')
        print('2 : Menu Inicial\n')

    elif menu_tipo == 'cadastrar':
        print('\n1 : Cadastrar Novo Filme')
        print('2 : Menu Inicial\n')
    elif menu_tipo == 'deletar':
        print('\n1 : Deletar Novo Filme')
        print('2 : Menu Inicial\n')

def validador_de_entrada(menu_tipo: string) -> int:
    """
    Verifica se a opcao digitada pelo usuario é um numeral
    """

    while True:
        menu(menu_tipo)

        opcao = input('Opção: ')
        if opcao.isdigit():
            opcao = int(opcao)
            return opcao

        os.system('cls')
        input('Caractere inválido.\nPressione Enter para voltar ao menu anterior')
        os.system('cls')

def principal() -> None:
    """
    Gerencia o menu principal
    """

    filmes = carregar_arquivo()
    while True:
        opcao = validador_de_entrada('principal')

        if opcao == 1:
            opcao_exibir(filmes)

        elif opcao == 2:
            opcao_pesquisar(filmes)

        elif opcao == 3:
            opcao_adicionar(filmes)

        elif opcao == 4:
            opcao_remover(filmes)

        elif opcao == 5:
            opcao_encerrar(filmes)

        else:
            opcao_default()

if __name__ == "__main__":
    principal()
    
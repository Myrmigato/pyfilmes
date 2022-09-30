"""
Sistema de gerenciamento de informações de filmes
"""

import os
import string
import sys
from unidecode import unidecode

def carrega_arquivo() -> list[list]:
    """
    Abre o arquivo .txt que contém as informações dos filmes
    """
    tamanho_arquivo = os.path.getsize("filmes.txt")

    if tamanho_arquivo == 0:
        lista_filmes = []
        return lista_filmes
    arquivo = open("filmes.txt", "r", encoding="utf-8")
    linhas = arquivo.readlines()
    lista_filmes = [linha.strip().split(',') for linha in linhas]
    return lista_filmes

def salva_arquivo(lista_filmes: list[list]) -> None:
    """
    Salva as informações dos filmes, adicionados durante a execução do programa, em um arquivo .txt
    """
    arquivo = open("filmes.txt", "w", encoding="utf-8")
    for filme in lista_filmes:
        arquivo.writelines(f"{filme[0]},{filme[1]},{filme[2]}\n")
    arquivo.close()

def filmes_cadastrados(filmes: list[list]) -> None:
    """
    Exibe as informações dos filmes que já estão cadastrados
    """
    if len(filmes) == 0:
        print('Sem Filmes Cadastrados\n')
        return
    i = 1
    for filme in filmes:
        print(f"{i} - Título: {filme[0]}")
        print(f'    Ano de Lançamento: {filme[1]}')
        print(f'    Gênero: {filme[2]}')
        print('='*100 + '\n')
        i += 1

def cadastra_filme(filmes: list[list]) -> None:
    """
    Cadastra um novo filme
    """
    filme = []
    filme.append(input('Nome: '))
    filme.append(input('Ano: '))
    filme.append(input('Gênero: '))
    filmes.append(filme)

def deleta_filme(filmes: list[list]) -> None:
    """
    Deleta, através do índice exibido ao usuário, algum filme do catálogo
    """
    if len(filmes) == 0:
        return

    while True:
        indice = input('Digite o número do filme a ser deletado: ')
        if indice.isdigit():
            indice = int(indice)
            indice -= 1
            if indice >= 0 and indice < len(filmes):
                del filmes[indice]
                os.system('cls')
                print('Filme Deletado com Sucesso!\n')
                break
            else:
                os.system('cls')
                print('Não existe filme cadastrado no indice digitado.')
                input('\nPressione Enter para continuar')
                os.system('cls')
                continue
        else:
            os.system('cls')
            input('Caractere inválido.\nPressione Enter para continuar')
            os.system('cls')

def pesquisa_filme(lista_filmes: list[list]) -> None:
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
            filmes_cadastrados(resultados)

def opcao_1(lista_filmes: list[list]) -> None:
    """
    Primeira opcao do menu
    """
    os.system('cls')
    filmes_cadastrados(lista_filmes)
    input('\nPressione Enter para voltar ao menu principal')

def opcao_2(lista_filmes: list[list]) -> None:
    """
    Segunda opcao do menu
    """
    controle = 0
    while True:
        os.system('cls')
        if controle == 0:
            pesquisa_filme(lista_filmes)
        subop = verifica_entrada('pesquisar')
        if subop == 1:
            controle = 0
        elif subop == 2:
            os.system('cls')
            break
        else:
            controle = 1
            opcao_default()

def opcao_3(lista_filmes: list[list]) -> None:
    """
    Terceira opcao do menu
    """
    controle = 0
    while True:
        os.system('cls')
        if controle == 0:
            cadastra_filme(lista_filmes)
            os.system('cls')
            print('Filme Cadastrado com Sucesso!\n')
        subop = verifica_entrada('cadastrar')
        if subop == 1:
            controle = 0
        elif subop == 2:
            os.system('cls')
            break
        else:
            controle = 1
            opcao_default()

def opcao_4(lista_filmes: list[list]) -> None:
    """
    Quarta opcao do menu
    """
    controle = 0
    while True:
        os.system('cls')
        if controle == 0:
            filmes_cadastrados(lista_filmes)
            deleta_filme(lista_filmes)
        subop = verifica_entrada('deletar')
        if subop == 1:
            controle = 0
        elif subop == 2:
            os.system('cls')
            break
        else:
            controle = 1
            opcao_default()

def opcao_5(lista_filmes: list[list]) -> None:
    """
    Quinta opcao do menu
    """
    os.system('cls')
    salva_arquivo(lista_filmes)
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

def verifica_entrada(menu_tipo: string) -> int:
    """
    Verifica se a opcao digitada pelo usuario é um inteiro
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
    filmes = carrega_arquivo()
    while True:
        opcao = verifica_entrada('principal')

        if opcao == 1:
            opcao_1(filmes)

        elif opcao == 2:
            opcao_2(filmes)

        elif opcao == 3:
            opcao_3(filmes)

        elif opcao == 4:
            opcao_4(filmes)

        elif opcao == 5:
            opcao_5(filmes)

        else:
            opcao_default()

if __name__ == "__main__":
    principal()
    
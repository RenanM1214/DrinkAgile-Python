import mysql.connector  # Importa o conector MySQL para Python
from mysql.connector import errorcode  # Importa o módulo de códigos de erro do conector MySQL
import connect  # Importa o arquivo connect.py
from Cadastro import cadastro_funcionario, cadastro_clientes, cadastro_Produto, cadastrar_fornecedor, cadastrar_usuario  # Importa as funções de cadastro de diferentes entidades
from Deletar import deleta_funcionario, deleta_cliente, deleta_produto, deleta_fornecedor, deletar_usuario  # Importa as funções de exclusão de diferentes entidades
from Editar import alterar_funcionario, alterar_clientes, alterar_Produto, alterar_fornecedor  # Importa as funções de edição de diferentes entidades
from Pesquisar import pesquisar_funcionario, consultar_clientes, pesquisar_produto, pesquisar_fornecedor  # Importa as funções de pesquisa de diferentes entidades
from Historico import historioco_func, historioco_cli, historioco_Prod, historioco_forn  # Importa as funções de histórico de diferentes entidades
from venda import realizar_venda, mostrar_estoque
import time

def main():
    texto_progressivo(mensagem)  # Exibe a mensagem progressivamente
    login()  # Após a conclusão da exibição da mensagem, chama a função de login

def texto_progressivo(texto):
    for i in range(len(texto)):
        print(texto[i], end='', flush=True)
        time.sleep(0.05)  # ajuste o tempo de espera conforme desejado
    print()  # para pular para a próxima linha após a mensagem completa

mensagem = "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█"


def login():
    connection = connect.connect_database()  # Estabelece uma conexão com o banco de dados
    if not connection:  # Se a conexão não for estabelecida
        return False

    username = input("Digite seu nome de usuário: ")  # Solicita o nome de usuário
    password = input("Digite sua senha: ")  # Solicita a senha do usuário

    cursor = connection.cursor()  # Cria um cursor para executar comandos SQL
    query = "SELECT * FROM login WHERE username = %s AND password = %s"  # Consulta para verificar o usuário e senha
    cursor.execute(query, (username, password))  # Executa a consulta passando os parâmetros
    result = cursor.fetchone()  # Obtém o resultado da consulta

    # Verifica se algum registro foi retornado
    if result:
        print("Login realizado com sucesso!")  # Imprime mensagem de sucesso
        mainPrincipal()  # Chama a função principal do programa
    else:
        print("Usuário ou senha incorretos.")  # Imprime mensagem de usuário ou senha incorretos
        login()  # Chama novamente a função de login

# Função principal do programa
def mainPrincipal():
    while True:
        print("-" * 59)
        print('-' * 23 + "Menu Principal" + '-' * 22)
        print("-" * 59)
        print("\nSeja bem-vindo!\n1-Funcionarios\n2-Clientes\n3-Produtos\n4-Fornecedores\n5-Usuario\n6-Vender\n7-Fechar")

        escolha = input("Escolha uma opção: ")  # Solicita uma opção ao usuário

        if escolha == "1":
            mainFunc()  # Chama a função para o menu de funcionários

        elif escolha == "2":
            mainCli()  # Chama a função para o menu de clientes

        elif escolha == "3":
            mainProd()  # Chama a função para o menu de produtos

        elif escolha == "4":
            mainForn()  # Chama a função para o menu de fornecedores

        elif escolha == "5":
            mainUsuario()  # Chama a função para o menu de usuários

        elif escolha == "6":
            mainVenda()
def mainFunc():
    while True:
        print("-" * 59)
        print('-' * 23 + "Menu Funcionario" + '-' * 22)
        print("-" * 59)
        print("\nSeja bem-vindo!\n1-Cadastrar\n2-Editar\n3-Pesquisar\n4-Deletar\n5- Historico Funcionarios\n6- Voltar")

        escolha = input("Escolha uma opção: ")  # Solicita uma opção ao usuário

        if escolha == "1":
            # Solicita informações para cadastrar um funcionário e chama a função correspondente
            nomeFunc = input("Digite o nome do Funcionarios: ")
            cargoFunc = input("Digite o cargo do Funcionarios: ")
            salarioFunc = input("Digite o salario do Funcionarios: ")
            cadastro_funcionario(nomeFunc, cargoFunc, salarioFunc)

        elif escolha == "2":
            # Solicita informações para editar um funcionário e chama a função correspondente
            id_funcionario = int(input("Digite o ID do Funcionário: "))
            novo_nome = input("Digite o novo nome do Funcionário: ")
            novo_cargo = input("Digite o novo cargo do Funcionário: ")
            novo_salario = float(input("Digite o novo salário do Funcionário: "))
            alterar_funcionario(id_funcionario, novo_nome, novo_cargo, novo_salario)

        elif escolha == "3":
            # Solicita o ID do funcionário para pesquisa e chama a função correspondente
            id = input("Digite o id do Funcionarios: ")
            pesquisar_funcionario(id)

        elif escolha == "4":
            # Solicita o ID do funcionário para exclusão e chama a função correspondente
            id = input("Digite o id do Funcionarios: ")
            deleta_funcionario(id)

        elif escolha == "5":
            historioco_func()  # Chama a função para exibir o histórico de funcionários

        elif escolha == "6":
            mainPrincipal()  # Volta para o menu principal

        else:
            print("Opção inválida. Tente novamente.")  # Mensagem de opção inválida


# Função para o menu de clientes
def mainCli():
    while True:
        print("-" * 59)
        print('-' * 23 + "Menu Cliente" + '-' * 22)
        print("-" * 59)
        print("\nSeja bem-vindo!\n1-Cadastrar\n2-Editar\n3-Pesquisar\n4-Deletar\n5- Historico Clientes\n6- Voltar")

        escolha = input("Escolha uma opção: ")  # Solicita uma opção ao usuário

        if escolha == "1":
            # Solicita informações para cadastrar um cliente e chama a função correspondente
            nomecli = input("Digite o nome do cliente: ")
            Sociedadecli = input("Digite a sociedade do cliente: ")
            telefonecli = input("Digite o telefone do cliente: ")
            cpfcli = input("Digite o cpf do cliente: ")
            cadastro_clientes(nomecli, Sociedadecli, telefonecli, cpfcli)

        elif escolha == "2":
            # Solicita informações para editar um cliente e chama a função correspondente
            novo_id_cli = input("Digite o id do cliente: ")
            novo_nome_cli = input("Digite o novo nome do cliente: ")
            novo_sociedade_cli = input("Digite a nova sociedade do cliente: ")
            novo_telefone_cli = float(input("Digite o novo telefone do cliente: "))
            novo_cpf_cli = int(input("Digite o novo cpf do cliente: "))
            alterar_clientes(novo_id_cli, novo_nome_cli, novo_sociedade_cli, novo_telefone_cli, novo_cpf_cli)

        elif escolha == "3":
            # Solicita o ID do cliente para pesquisa e chama a função correspondente
            idcli = input("Digite o id do cliente: ")
            consultar_clientes(idcli)

        elif escolha == "4":
            # Solicita o ID do cliente para exclusão e chama a função correspondente
            idcli = input("Digite o id do cliente: ")
            deleta_cliente(idcli)

        elif escolha == "5":
            historioco_cli()  # Chama a função para exibir o histórico de clientes

        elif escolha == "6":
            mainPrincipal()  # Volta para o menu principal

        else:
            print("Opção inválida. Tente novamente.")  # Mensagem de opção inválida

# Função para o menu de produtos
def mainProd():
    while True:
        print("-" * 59)
        print('-' * 23 + "Menu Produtos" + '-' * 22)
        print("-" * 59)
        print("\nSeja bem-vindo!\n1-Cadastrar\n2-Editar\n3-Pesquisar\n4-Deletar\n5- Historico produtos\n6- Voltar")

        escolha = input("Escolha uma opção: ")  # Solicita uma opção ao usuário

        if escolha == "1":
            # Solicita informações para cadastrar um produto e chama a função correspondente
            nomeProd = input("Digite o nome do Produto: ")
            preçoProd = input("Digite o preço do Produto: ")
            descProd = input("Digite a descrição do Produto: ")
            codProd = input("Digite o codigo do Produto: ")
            idFornecedor = input("Digite o ID do fornecedor: ")
            cadastro_Produto(nomeProd, preçoProd, descProd, codProd, idFornecedor)

        elif escolha == "2":
            # Solicita informações para editar um produto e chama a função correspondente
            id_Produtos = int(input("Digite o ID do Produto: "))
            novo_nome = input("Digite o novo nome do Produto: ")
            novo_preço = float(input("Digite o novo preço do produto: "))
            novo_desc = input("Digite a nova descrição do Produto: ")
            novo_cod = float(input("Digite o novo código do Produto: "))
            novo_idForn = float(input("Digite o novo ID do Fornecedor: "))
            alterar_Produto(id_Produtos, novo_nome, novo_preço, novo_desc, novo_cod, novo_idForn)

        elif escolha == "3":
            # Solicita o ID do produto para pesquisa e chama a função correspondente
            idprod = input("Digite o id do Produto: ")
            pesquisar_produto(idprod)

        elif escolha == "4":
            # Solicita o ID do produto para exclusão e chama a função correspondente
            idprod = input("Digite o id do Produto: ")
            deleta_produto(idprod)

        elif escolha == "5":
            historioco_Prod()  # Chama a função para exibir o histórico de produtos

        elif escolha == "6":
            mainPrincipal()  # Volta para o menu principal

        else:
            print("Opção inválida. Tente novamente.")  # Mensagem de opção inválida

# Função para o menu de fornecedores
def mainForn():
    while True:
        print("-" * 59)
        print('-' * 23 + "Menu Fornecedor" + '-' * 22)
        print("-" * 59)
        print("\nSeja bem-vindo!\n1-Cadastrar\n2-Editar\n3-Pesquisar\n4-Deletar\n5- Historico produtos\n6- Voltar")

        escolha = input("Escolha uma opção: ")  # Solicita uma opção ao usuário

        if escolha == "1":
            # Solicita informações para cadastrar um fornecedor e chama a função correspondente
            nomeForn = input("Digite o nome do fornecedor: ")
            produtoForn = input("Digite o produto do fornecedor: ")
            cidadeforn = input("Digite a cidade do fornecedor: ")
            cnpjforn = input("Digite o cnpj do fornecedor: ")
            cadastrar_fornecedor(nomeForn, produtoForn, cidadeforn, cnpjforn)

        elif escolha == "2":
            # Solicita informações para editar um fornecedor e chama a função correspondente
            id_fornecedor = int(input("Digite o ID do fornecedor: "))
            nome_forn = input("Digite o novo nome do fornecedor: ")
            produto_forn = input("Digite o novo produto: ")
            cidade_forn = input("Digite a nova cidade: ")
            cnpj_forn = input("Digite o novo cnpj do Fornecedor: ")
            alterar_fornecedor(id_fornecedor, nome_forn, produto_forn, cidade_forn, cnpj_forn)

        elif escolha == "3":
            # Solicita o ID do fornecedor para pesquisa e chama a função correspondente
            id_fornecedor = int(input("Digite o ID do fornecedor: "))
            pesquisar_fornecedor(id_fornecedor)

        elif escolha == "4":
            # Solicita o ID do fornecedor para exclusão e chama a função correspondente
            id_fornecedor = input("Digite o id do Fornecedor: ")
            deleta_fornecedor(id_fornecedor)

        elif escolha == "5":
            historioco_forn()  # Chama a função para exibir o histórico de fornecedores

        elif escolha == "6":
            mainPrincipal()  # Volta para o menu principal

        else:
            print("Opção inválida. Tente novamente.")  # Mensagem de opção inválida

# Função para o menu de usuários
def mainUsuario():
    while True:
        print("-" * 59)
        print('-' * 23 + "Manipular Usuario" + '-' * 22)
        print("-" * 59)
        print("\nSeja bem-vindo!\n1-Cadastrar\n2-Deletar\n3- Voltar")

        escolha = input("Escolha uma opção: ")  # Solicita uma opção ao usuário

        if escolha == "1":
            # Solicita informações para cadastrar um usuário e chama a função correspondente
            n_username = input("Digite seu nome de usuário: ")
            n_password = input("Digite sua senha: ")
            cadastrar_usuario(n_username, n_password)

        elif escolha == "2":
            # Solicita o ID do usuário para exclusão e chama a função correspondente
            id_login = input("Digite o ID do usuário que deseja deletar: ")
            deletar_usuario(id_login)

        elif escolha == "3":
            mainPrincipal()  # Volta para o menu principal

        else:
            print("Opção inválida. Tente novamente.")  # Mensagem de opção inválida

def mainVenda():
    while True:
        print("-" * 59)
        print('-' * 23 + "Menu de Vendas" + '-' * 22)
        print("-" * 59)
        print("\nSeja bem-vindo!\n1-Fazer Venda\n2-Conferir Estoque\n3-Voltar")

        escolha = input("Escolha uma opção: ")  # Solicita uma opção ao usuário

        if escolha == "1":
            # Solicita informações para  chamar a função correspondente
            id_produto = int(input("Digite o ID do produto: "))
            quantidade = int(input("Digite a quantidade vendida: "))
            realizar_venda(id_produto, quantidade)

        elif escolha == "2":
            mostrar_estoque()

        elif escolha == "3":
            mainPrincipal()  # Volta para o menu principal


        else:
            print("Opção inválida. Tente novamente.")  # Mensagem de opção inválida

# Ponto de entrada do programa, chama a função de login para iniciar o sistema
if __name__ == "__main__":
    main()  # Inicia o programa
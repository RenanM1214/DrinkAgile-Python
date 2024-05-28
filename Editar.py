import mysql.connector
# Importa o código de erro do MySQL e o módulo de conexão personalizado
from mysql.connector import errorcode
import connect

# Função para alterar informações de um funcionário no banco de dados
def alterar_funcionario(novo_id_func, novo_nome_func, novo_cargo_func, novo_salario_func):
    try:
        # Estabelece conexão com o banco de dados
        db_connection = connect.connect_database()
        cursor = db_connection.cursor()

        # Chama a stored procedure para alterar os detalhes do funcionário
        cursor.callproc('procalterarfunc', (novo_id_func, novo_nome_func, novo_cargo_func, novo_salario_func))
        db_connection.commit()

        # Exibe a mensagem retornada pela procedure
        for result in cursor.stored_results():
            print(result.fetchone()[0])

    except mysql.connector.Error as error:
        print("Erro ao alterar o funcionário:", error)

    finally:
        # Fecha a conexão com o banco de dados
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada")

# Função para alterar informações de um cliente no banco de dados
def alterar_clientes(novo_id_cli, novo_nome_cli, novo_sociedade_cli, novo_telefone_cli, novo_cpf_cli):
    try:
        # Estabelece conexão com o banco de dados
        db_connection = connect.connect_database()
        cursor = db_connection.cursor()

        # Chama a stored procedure para alterar os detalhes do cliente
        cursor.callproc('procalterarclientes', (novo_id_cli, novo_nome_cli, novo_sociedade_cli, novo_telefone_cli, novo_cpf_cli))
        db_connection.commit()

        # Exibe a mensagem retornada pela procedure
        for result in cursor.stored_results():
            print(result.fetchone()[0])

    except mysql.connector.Error as error:
        print("Erro ao alterar o cliente:", error)

    finally:
        # Fecha a conexão com o banco de dados
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada")

# Função para alterar informações de um produto no banco de dados
def alterar_Produto(novo_id_Prod, novo_nome_Prod, novo_preco_Prod, novo_desc_Prod, novo_cod_Pord, novo_idForn_Prod):
    try:
        # Estabelece conexão com o banco de dados
        db_connection = connect.connect_database()
        cursor = db_connection.cursor()

        # Chama a stored procedure para alterar os detalhes do produto
        cursor.callproc('procalterarProd', (novo_id_Prod, novo_nome_Prod, novo_preco_Prod, novo_desc_Prod, novo_cod_Pord, novo_idForn_Prod))
        db_connection.commit()

        # Exibe a mensagem retornada pela procedure
        for result in cursor.stored_results():
            print(result.fetchone()[0])

    except mysql.connector.Error as error:
        print("Erro ao alterar o Produto:", error)

    finally:
        # Fecha a conexão com o banco de dados
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada")

# Função para alterar informações de um fornecedor no banco de dados
def alterar_fornecedor(id_fornecedor, nome_forn, produto_forn, cidade_forn, cnpj_forn):
    try:
        # Estabelece conexão com o banco de dados
        db_connection = connect.connect_database()
        cursor = db_connection.cursor()

        # Chama a stored procedure para alterar os detalhes do fornecedor
        cursor.callproc('procalterarfornecedor', (id_fornecedor, nome_forn, produto_forn, cidade_forn, cnpj_forn))
        db_connection.commit()

        # Exibe a mensagem retornada pela procedure
        for result in cursor.stored_results():
            print(result.fetchone()[0])

    except mysql.connector.Error as error:
        print("Erro ao alterar o fornecedor:", error)

    finally:
        # Fecha a conexão com o banco de dados
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada")



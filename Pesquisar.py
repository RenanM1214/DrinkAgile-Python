import mysql.connector  # Importa o conector MySQL
import connect  # Importa o módulo personalizado para conexão com o banco de dados

# Define uma função para pesquisar informações de um funcionário com base em seu ID
def pesquisar_funcionario(id):
    try:
        # Estabelece a conexão com o banco de dados MySQL
        db_connection = connect.connect_database()

        # Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        # Executa a consulta SQL para obter os dados do funcionário com o ID fornecido
        sql = f"SELECT * FROM funcionarios WHERE idFuncionarios = {id}"
        cursor.execute(sql)

        # Exibe os resultados da consulta
        print("ID\tNOME\t\tCARGO\t\t\tSALARIO")
        for row in cursor.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}")

    except mysql.connector.Error as error:
        print("Erro ao consultar funcionario:", error)

    finally:
        # Garante que a conexão seja fechada, independentemente do resultado
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")

# As funções abaixo (consultar_clientes, pesquisar_produto, pesquisar_fornecedor) seguem uma lógica similar,
# permitindo a pesquisa de informações de clientes, produtos e fornecedores com base em seus respectivos IDs.


# Define uma função para consultar informações de um cliente com base em seu ID
def consultar_clientes(idcli):
    try:
        # Estabelece a conexão com o banco de dados MySQL
        db_connection = connect.connect_database()

        # Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        # Executa a consulta SQL para obter os dados do cliente com o ID fornecido
        sql = f"SELECT * FROM clientes WHERE idClientes = {idcli}"
        cursor.execute(sql)

        # Exibe os resultados da consulta
        print("ID\tNOME\t\tSOCIEDADE\t\t\tTELEFONE\t\tCPF")
        for row in cursor.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}\t\t\t{row[4]}")

    except mysql.connector.Error as error:
        print("Erro ao consultar clientes:", error)

    finally:
        # Garante que a conexão seja fechada, independentemente do resultado
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")

# Define uma função para pesquisar informações de um produto com base em seu ID
def pesquisar_produto(idprod):
    try:
        # Estabelece a conexão com o banco de dados MySQL
        db_connection = connect.connect_database()

        # Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        # Executa a consulta SQL para obter os dados do produto com o ID fornecido
        sql = f"SELECT * FROM produtos WHERE idProdutos = {idprod}"
        cursor.execute(sql)

        # Exibe os resultados da consulta
        print("ID\tNome\t\tPreço\t\tDescrição\t\tCodigo\t\tidFornecedor")
        for row in cursor.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}\t{row[4]}\t{row[5]}")

    except mysql.connector.Error as error:
        print("Erro ao consultar produto:", error)

    finally:
        # Garante que a conexão seja fechada, independentemente do resultado
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")

# Define uma função para pesquisar informações de um fornecedor com base em seu ID
def pesquisar_fornecedor(id_fornecedor):
    try:
        # Estabelece a conexão com o banco de dados MySQL
        db_connection = connect.connect_database()

        # Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        # Executa a consulta SQL para obter os dados do fornecedor com o ID fornecido
        sql = f"SELECT * FROM fornecedor WHERE idFornecedor = {id_fornecedor}"
        cursor.execute(sql)

        # Exibe os resultados da consulta
        print("ID\tNome\t\tproduto\t\tcidade\t\tcnpj")
        for row in cursor.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}\t{row[4]}")

    except mysql.connector.Error as error:
        print("Erro ao consultar fornecedor:", error)

    finally:
        # Garante que a conexão seja fechada, independentemente do resultado
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")

import mysql.connector
import connect

def deleta_funcionario(id):
    try:
        # Estabelece a conexão com o banco de dados MySQL
        db_connection = connect.connect_database()

        # Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        # Executa a consulta SQL para deletar o funcionário
        sql = f"DELETE FROM funcionarios WHERE idFuncionarios = {id}"
        cursor.execute(sql)
        db_connection.commit()  # Confirma a transação

    except mysql.connector.Error as error:
        print("Erro ao deletar funcionário:", error)

    finally:
        # Fecha o cursor e a conexão
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")


def deleta_cliente(idcli):
    try:
        # Estabelece a conexão com o banco de dados MySQL
        db_connection = connect.connect_database()

        # Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        # Executa a consulta SQL para deletar o funcionário
        sql = f"DELETE FROM clientes WHERE idClientes = {idcli}"
        cursor.execute(sql)
        db_connection.commit()  # Confirma a transação

    except mysql.connector.Error as error:
        print("Erro ao deletar cliente:", error)

    finally:
        # Fecha o cursor e a conexão
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")

def deleta_produto(idprod):
    try:
        # Estabelece a conexão com o banco de dados MySQL
        db_connection = connect.connect_database()

        # Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        # Executa a consulta SQL para deletar o funcionário
        sql = f"DELETE FROM produtos WHERE idProdutos = {idprod}"
        cursor.execute(sql)
        db_connection.commit()  # Confirma a transação

    except mysql.connector.Error as error:
        print("Erro ao deletar produto:", error)

    finally:
        # Fecha o cursor e a conexão
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")


def deleta_fornecedor(id_fornecedor):
    try:
        # Estabelece a conexão com o banco de dados MySQL
        db_connection = connect.connect_database()

        # Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        # Executa a consulta SQL para deletar o funcionário
        sql = f"DELETE FROM fornecedor WHERE idFornecedor = {id_fornecedor}"
        cursor.execute(sql)
        db_connection.commit()  # Confirma a transação

    except mysql.connector.Error as error:
        print("Erro ao deletar fornecedor:", error)

    finally:
        # Fecha o cursor e a conexão
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")

def deletar_usuario(id_login):
    try:
        # Estabelece a conexão com o banco de dados MySQL
        db_connection = connect.connect_database()

        # Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        # Executa a consulta SQL para deletar o funcionário
        sql = f"DELETE FROM login WHERE idLogin = {id_login}"
        cursor.execute(sql)
        db_connection.commit()  # Confirma a transação

    except mysql.connector.Error as error:
        print("Erro ao cadastrar usuario:", error)

    finally:
        # Fecha o cursor e a conexão
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")
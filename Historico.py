import mysql.connector
import connect

def historioco_func():
    try:
        # Estabelece a conexão com o banco de dados MySQL
        db_connection = connect.connect_database()

        #Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        #Executa a consulta SQL para obter os dados da view
        sql = f"SELECT * FROM historicofuncionarios"
        cursor.execute(sql)

        #Exibe os resultados da consulta
        print("idFuncionario\tnomeAntigo\tcargoAntigo\tsalarioAntigo\tnomeNovo\tcargoNovo\tsalarioNovo\tdataAlteracao")
        for row in cursor.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}\t\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}\t\t{row[7]}")

    except mysql.connector.Error as error:
        print("Erro ao consultar historico:",error)

    finally:
        #Garante que a conexão seja fechada, independentemente do resultado
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")


def historioco_cli():
    try:
        # Estabelece a conexão com o banco de dados MySQL
        db_connection = connect.connect_database()

        #Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        #Executa a consulta SQL para obter os dados da view
        sql = f"select * from historicoclientes"
        cursor.execute(sql)

        #Exibe os resultados da consulta
        print("idHistcli\tidCliente\tnomeAntigo\tSociedadeAntiga\tTelefoneAntigo\tCpfAntigo\t\tnomeNovo\tSociedadeNovo\tTelefoneNovo\tCpfNovo\tdataAlteracao")
        for row in cursor.fetchall():
            print(f"{row[0]}\t\t\t{row[1]}\t\t\t{row[2]}\t\t\t{row[3]}\t\t\t{row[4]}\t\t\t{row[5]}\t\t{row[6]}\t\t{row[7]}\t\t\t{row[8]}")

    except mysql.connector.Error as error:
        print("Erro ao consultar historico:",error)

    finally:
        #Garante que a conexão seja fechada, independentemente do resultado
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")


def historioco_Prod():
    try:
        # Estabelece a conexão com o banco de dados MySQL
        db_connection = connect.connect_database()

        #Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        #Executa a consulta SQL para obter os dados da view
        sql = f"SELECT * FROM historicoProduto"
        cursor.execute(sql)

        #Exibe os resultados da consulta
        print("idProduto\tnomeAntigo\tpreçoAntigo\tdescAntigo\tcodProdAntigo\tidFornAntigo\tnomeNovo\tpreçoNovo\tdescNovo\tcodProdNovo\tidFornNovo\tdataAlteracao")
        for row in cursor.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}\t\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}\t\t{row[7]}\t\t{row[8]}\t\t{row[9]}\t\t{row[10]}\t\t{row[11]}\t\t{row[12]}")

    except mysql.connector.Error as error:
        print("Erro ao consultar historico:",error)

    finally:
        #Garante que a conexão seja fechada, independentemente do resultado
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexão encerrada.")


def historioco_forn():
    try:
        # Estabelece a conexão com o banco de dados MySQL
        db_connection = connect.connect_database()

        #Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        #Executa a consulta SQL para obter os dados da view
        sql = f"SELECT * FROM historicofornecedores"
        cursor.execute(sql)

        #Exibe os resultados da consulta
        print("idFornecedores\tnomeAntigo\tprodutoAntigo\tcidadeAntiga\tcnpjAntigo\tnomeNovo\tprodutoNovo\tcidadenova\tcnpjnovo\tdataAlteracao")
        for row in cursor.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}\t\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}\t\t{row[7]}\t\t{row[8]}\t\t{row[9]}")

    except mysql.connector.Error as error:
        print("Erro ao consultar historico:",error)
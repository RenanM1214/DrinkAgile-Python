import mysql.connector  # Importa o módulo mysql.connector para permitir a conexão com o banco de dados MySQL
import connect  # Importa um módulo personalizado chamado 'connect' que contém a função de conexão com o banco de dados

def cadastro_funcionario(nomeFunc, cargoFunc, salarioFunc):
    try:
        db_connection = connect.connect_database()  # Estabelece a conexão com o banco de dados
        cursor = db_connection.cursor()  # Cria um cursor para executar comandos SQL

        # Chama a procedure para cadastrar o funcionario
        cursor.callproc('proccadastrarFuncionarios', (nomeFunc, cargoFunc, salarioFunc))  # Executa a procedure armazenada 'proccadastrarFuncionarios' com os parâmetros fornecidos
        db_connection.commit()  # Confirma a transação

        print("Funcionarios cadastrado com Sucesso!")  # Mensagem de sucesso

    except mysql.connector.Error as error:
        print("Erro ao cadastrar Funcionarios:", error)  # Mensagem de erro em caso de falha

    finally:
        if 'db_connection' in locals() and db_connection.is_connected():  # Verifica se a conexão está estabelecida
            cursor.close()  # Fecha o cursor
            db_connection.close()  # Fecha a conexão com o banco de dados
            print("Conexão encerrada.")  # Mensagem indicando que a conexão foi encerrada

def cadastro_clientes(nomecli, Sociedadecli, telefonecli, cpfcli):
    try:
        db_connection = connect.connect_database()  # Estabelece a conexão com o banco de dados
        cursor = db_connection.cursor()  # Cria um cursor para executar comandos SQL

        # Chama a procedure para cadastrar o cliente
        cursor.callproc('proccadastrarClientes', (nomecli, Sociedadecli, telefonecli, cpfcli))  # Executa a procedure armazenada 'proccadastrarClientes' com os parâmetros fornecidos
        db_connection.commit()  # Confirma a transação

        print("Cliente cadastrado com Sucesso!")  # Mensagem de sucesso

    except mysql.connector.Error as error:
        print("Erro ao cadastrar cliente:", error)  # Mensagem de erro em caso de falha

    finally:
        if 'db_connection' in locals() and db_connection.is_connected():  # Verifica se a conexão está estabelecida
            cursor.close()  # Fecha o cursor
            db_connection.close()  # Fecha a conexão com o banco de dados
            print("Conexão encerrada.")  # Mensagem indicando que a conexão foi encerrada

def cadastro_Produto(nomeProd, preçoProd, descProd, codProd, idFornecedor):
    try:
        db_connection = connect.connect_database()  # Estabelece a conexão com o banco de dados
        cursor = db_connection.cursor()  # Cria um cursor para executar comandos SQL

        # Chama a procedure para cadastrar o produto
        cursor.callproc('proccadastrarProduto', (nomeProd, preçoProd, descProd, codProd, idFornecedor))  # Executa a procedure armazenada 'proccadastrarProduto' com os parâmetros fornecidos
        db_connection.commit()  # Confirma a transação

        print("Produto cadastrado com Sucesso!")  # Mensagem de sucesso

    except mysql.connector.Error as error:
        print("Erro ao cadastrar Produto:", error)  # Mensagem de erro em caso de falha

    finally:
        if 'db_connection' in locals() and db_connection.is_connected():  # Verifica se a conexão está estabelecida
            cursor.close()  # Fecha o cursor
            db_connection.close()  # Fecha a conexão com o banco de dados
            print("Conexão encerrada.")  # Mensagem indicando que a conexão foi encerrada

def cadastrar_fornecedor(nomeForn, produtoForn, cidadeforn, cnpjforn):
    try:
        db_connection = connect.connect_database()  # Estabelece a conexão com o banco de dados
        cursor = db_connection.cursor()  # Cria um cursor para executar comandos SQL

        cursor.callproc('proccadastrarFornecedor', (nomeForn, produtoForn, cidadeforn, cnpjforn))  # Executa a procedure armazenada 'proccadastrarFornecedor' com os parâmetros fornecidos
        db_connection.commit()  # Confirma a transação

        print("Fornecedor cadastrado com sucesso!")  # Mensagem de sucesso

    except mysql.connector.Error as error:
        print("Erro ao cadastrar fornecedor:", error)  # Mensagem de erro em caso de falha

    finally:
        if 'db_connection' in locals() and db_connection.is_connected():  # Verifica se a conexão está estabelecida
            cursor.close()  # Fecha o cursor
            db_connection.close()  # Fecha a conexão com o banco de dados
            print("Conexão encerrada.")  # Mensagem indicando que a conexão foi encerrada

def cadastrar_usuario(username, password):
    try:
        db_connection = connect.connect_database()  # Estabelece a conexão com o banco de dados
        cursor = db_connection.cursor()  # Cria um cursor para executar comandos SQL

        # Executa a consulta SQL para inserir um novo usuário
        sql = f"INSERT INTO login (username, password) VALUES {(username, password)}"  # Cria a consulta SQL para inserir os valores fornecidos na tabela 'login'
        cursor.execute(sql)  # Executa a consulta SQL
        db_connection.commit()  # Confirma a transação

    except mysql.connector.Error as error:
        print("Erro ao cadastrar usuario:", error)  # Mensagem de erro em caso de falha

    finally:
        if 'db_connection' in locals() and db_connection.is_connected():  # Verifica se a conexão está estabelecida
            cursor.close()  # Fecha o cursor
            db_connection.close()  # Fecha a conexão com o banco de dados
            print("Conexão encerrada.")  # Mensagem indicando que a conexão foi encerrada
import mysql.connector  # Importa o módulo mysql.connector para permitir a conexão com o banco de dados MySQL

def connect_database():
    try:
        # Tenta estabelecer a conexão com o banco de dados
        db_connection = mysql.connector.connect(
            host='localhost',  # Define o host onde o banco de dados está rodando (neste caso, localhost)
            user='tecmysql',  # Nome de usuário do banco de dados
            password='devmysql',  # Senha do usuário do banco de dados
            database='drink_agile'  # Nome do banco de dados que deseja se conectar
        )
        print("Conexão Realizada com Sucesso!")  # Mensagem de sucesso ao conectar
        return db_connection  # Retorna a conexão estabelecida

    except mysql.connector.Error as error:  # Captura os erros relacionados ao MySQL
        if error.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:  # Caso o banco de dados não exista
            print("O Banco de dados não existe")
        elif error.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:  # Caso o nome de usuário ou a senha estejam incorretos
            print("O User name ou o password esta errado!")
        else:  # Para outros erros
            print(error)

if __name__ == '__main__':
    connect_database()  # Executa a função connect_database() caso este arquivo seja executado diretamente
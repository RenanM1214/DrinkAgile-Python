import connect
import mysql.connector


# Função para realizar a venda
def realizar_venda(id_produto, quantidade):
    conexao = connect.connect_database()  # Conecta ao banco de dados
    cursor = conexao.cursor(dictionary=True)

    try:
        # Verifica se há estoque suficiente
        consulta_estoque = "SELECT quantidade FROM estoque WHERE idProdutos = %s"
        cursor.execute(consulta_estoque, (id_produto,))
        estoque_atual = cursor.fetchone()

        if estoque_atual and estoque_atual['quantidade'] >= quantidade:
            # Consulta os detalhes do produto
            consulta_produto = "SELECT nomeProd, preçoProd FROM produtos WHERE idProdutos = %s"
            cursor.execute(consulta_produto, (id_produto,))
            produto = cursor.fetchone()

            if produto:
                nome_produto = produto['nomeProd']
                preco_produto = produto['preçoProd']

                valor_total = preco_produto * quantidade

                # Insere a venda
                inserir_venda = "INSERT INTO vendas (codvendas, idClientes, idFornecedor, valorvendas, totalvendas, datavendas) VALUES (%s, %s, %s, %s, %s, NOW())"
                dados_venda = (id_produto, 1, 1, valor_total, valor_total)
                cursor.execute(inserir_venda, dados_venda)

                # Atualiza o estoque
                novo_estoque = estoque_atual['quantidade'] - quantidade
                atualizar_estoque = "UPDATE estoque SET quantidade = %s WHERE idProdutos = %s"
                cursor.execute(atualizar_estoque, (novo_estoque, id_produto))

                conexao.commit()

                print(
                    f"Venda realizada com sucesso!\nNome do produto: {nome_produto}\nValor total da venda: R${valor_total:.2f}")
            else:
                print("Produto não encontrado.")
        else:
            print("Quantidade insuficiente em estoque.")

    except mysql.connector.Error as erro:
        print("Erro ao realizar a venda:", erro)

    finally:
        cursor.close()
        conexao.close()


# Função para mostrar a tabela de estoque
def mostrar_estoque():
    conexao = connect.connect_database()  # Conecta ao banco de dados
    cursor = conexao.cursor(dictionary=True)

    try:
        consulta = "SELECT produtos.nomeProd, estoque.quantidade FROM estoque INNER JOIN produtos ON estoque.idProdutos = produtos.idProdutos"
        cursor.execute(consulta)
        estoque = cursor.fetchall()

        if estoque:
            print("Tabela de Estoque:")
            for item in estoque:
                print(f"Nome do Produto: {item['nomeProd']} | Quantidade: {item['quantidade']}")
        else:
            print("A tabela de estoque está vazia.")

    except mysql.connector.Error as erro:
        print("Erro ao mostrar o estoque:", erro)

    finally:
        cursor.close()
        conexao.close()

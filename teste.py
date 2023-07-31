import mysql.connector

def access_stored_procedure():
    # Configurações de conexão com o banco de dados
    host = 'localhost'
    user = 'root'
    password = 'admin'
    database = 'partitoteca'

    try:
        # Estabelece a conexão com o banco de dados
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Cria um cursor para executar as consultas
        cursor = connection.cursor()

        # Define o nome da stored procedure
        stored_procedure_name = "spTeste"

        # Parâmetros de entrada para a stored procedure, se houver
        # Exemplo: params = (parametro1, parametro2, ...)
        # Caso não tenha parâmetros, deixe params como uma tupla vazia (params = ())
        params = ()  # Coloque os parâmetros aqui, se necessário

        # Executa a stored procedure
        cursor.callproc(stored_procedure_name, params)

        # Se a stored procedure retornar algum resultado, você pode recuperá-lo assim:
        result = None
        for result_cursor in cursor.stored_results():
            result = result_cursor.fetchall()

        # Exemplo de exibição do resultado
        if result is not None:
            print("Resultado da stored procedure:")
            print(result)

        # Fecha o cursor e a conexão
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print("Erro ao acessar a stored procedure:", error)

if __name__ == "__main__":
    access_stored_procedure()
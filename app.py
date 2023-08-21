from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
    conn = mysql.connector.connect(
      host='127.0.0.1',
      user='root',
      password='admin'

    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

cursor = conn.cursor()

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Conecta o SQLAlchemy com a aplicação. A conexão com o banco de dados é feita pelo app.config acima
db = SQLAlchemy(app)

# Para funcionar, a aplicação deve ser rodada a partir de app.py
from views import *

if __name__ == '__main__':
    app.run(debug=True)

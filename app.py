from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

class Pais:
    def __init__(self, idPais, nome, sigla3, sigla2):
        self.idPais=idPais
        self.nome=nome
        self.sigla3=sigla3
        self.sigla2=sigla2


app = Flask(__name__)

# Instanciando o banco de dados. Conecta a aplicação ao banco de dados
# string de conexão. Permite a migração para outros bancos de dados
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = '127.0.0.1',
        database = 'partitoteca'

    )

db = SQLAlchemy(app)





@app.route('/')
def ola():

    pais1 = Pais('1','Brasil','BRA','BR')
    pais2 = Pais('2','Argentina', 'ARG', 'AR')
    pais3 = Pais('3','Canadá', 'CAN', 'CA')


    lista = [pais1,pais2,pais3]

    #return lista[0].nome

    return render_template('index.html', titulo='Bem-vindo ao Partitoteca', paises=lista)

app.run()



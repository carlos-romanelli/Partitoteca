from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


class Pais:
    def __init__(self, idpais, nome, sigla3, sigla2):
        self.idpais = idpais
        self.nome = nome
        self.sigla3 = sigla3
        self.sigla2 = sigla2

class Acervo:
    def __init__(self, descricao_acervo, telefone_acervo, email_acervo, sigla, localizacao, publico):
        self.descricao_acervo = descricao_acervo
        self.telefone_acervo = telefone_acervo
        self.email_acervo = email_acervo
        self.sigla = sigla
        self.localizacao = localizacao
        self.publico = publico



app = Flask(__name__)

# Instanciando o banco de dados. Conecta a aplicação ao banco de dados
# string de conexão. Permite a migração para outros bancos de dados
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='admin',
        servidor='127.0.0.1',
        database='partitoteca'

    )

db = SQLAlchemy(app)

acervo1 = Acervo('Acervo um', '(32) 99999-1111', 'email_acervo1@gmail.com', 'ACV1', 'Rua A número 100', 'S')
acervo2 = Acervo('Acervo dois', '(32) 99999-2222', 'email_acervo2@gmail.com', 'ACV2', 'Rua A número 200', 'S')
acervo3 = Acervo('Acervo três', '(32) 99999-3333', 'email_acervo3@gmail.com', 'ACV3', 'Rua A número 300', 'S')
lista = [acervo1, acervo2, acervo3]


@app.route('/')
def index():

    return render_template('index.html', titulo='Bem-vindo ao Partitoteca', acervos=lista)


@app.route('/novo_usuario')
def novo_usuario():
    return render_template('novo_usuario.html', titulo1='Dados do Acervo', titulo2='Dados do Usuário')


@app.route('/cria_acervo', methods=['POST',])
def cria_acervo():
    descricao_acervo = request.form['descricao_acervo']
    telefone_acervo = request.form['telefone_acervo']
    email_acervo = request.form['email_acervo']
    sigla = request.form['sigla']
    localizacao = request.form['localizacao']
    publico = request.form['publico']

    acervo = Acervo(descricao_acervo, telefone_acervo, email_acervo, sigla, localizacao, publico)
    acervos = lista.append(acervo)
    return redirect('/')


@app.route('/cria_usuario', methods=['POST',])
def cria_usuario():
    pass

app.run(debug=True)

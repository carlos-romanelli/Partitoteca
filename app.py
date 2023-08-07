from flask import Flask, render_template, request, redirect, session, flash, url_for
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
app.secret_key = 'mozart'

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

# Testando se o usuário está logado
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo_usuario')))

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
    return redirect(url_for('index'))


@app.route('/cria_usuario', methods=['POST',])
def cria_usuario():
    pass

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

# Faz o login do usuário
@app.route('/autenticar', methods=['POST',])
def autenticar():

    if '123456' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado!')
        return redirect(url_for('login'))

# Faz o logout do usuário
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)

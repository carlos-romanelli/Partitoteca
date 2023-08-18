from flask import Flask, render_template, request, redirect, session, flash, url_for
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
app.secret_key = 'mozart'

# Conecta com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='admin',
        servidor='localhost',
        database='partitoteca'
    )

# Conecta o SQLAlchemy com a aplicação. A conexão com o banco de dados é feita pelo app.config acima
db = SQLAlchemy(app)

# Criando as classes de tabelas - Models - de conexão com o banco de dados
class Usuarios(db.Model):
    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    apelido = db.Column(db.String(20), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(8), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    alterarSenha = db.Column(db.String(1), nullable=False)
    contatoPublico = db.Column(db.String(1), nullable=False)
    redesSociais = db.Column(db.String(200), nullable=False)
    dataInclusao = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Pais(db.Model):
    idPais = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    sigla3 = db.Column(db.String(3), nullable=False)
    sigla2 = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Acervo(db.Model):
    idAcervo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    sigla = db.Column(db.String(20), nullable=False)
    localizacao = db.Column(db.String(100), nullable=False)
    publico = db.Column(db.String(1), nullable=False)
    dtInclusao = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome



# FIM DAS CLASSES MODELS

'''class Pais:
    def __init__(self, idPais, nome, sigla3, sigla2):
        self.idPais = iPpais
        self.nome = nome
        self.sigla3 = sigla3
        self.sigla2 = sigla2


class Acervo:
    def __init__(self, idAcervo, descricao_acervo, telefone_acervo, email_acervo, sigla, localizacao, publico, dtInclusao):
        self.idAcervo = idAcervo
        self.descricao_acervo = descricao_acervo
        self.telefone_acervo = telefone_acervo
        self.email_acervo = email_acervo
        self.sigla = sigla
        self.localizacao = localizacao
        self.publico = publico
        self.dtInclusao = dtInclusao

acervo1 = Acervo('1', 'Acervo um', '(32) 99999-1111', 'email_acervo1@gmail.com', 'ACV1', 'Rua A número 100', 'S', '2023-08-18')
acervo2 = Acervo('2', 'Acervo dois', '(32) 99999-2222', 'email_acervo2@gmail.com', 'ACV2', 'Rua A número 200', 'S', '2023-08-18')
acervo3 = Acervo('3', 'Acervo três', '(32) 99999-3333', 'email_acervo3@gmail.com', 'ACV3', 'Rua A número 300', 'S', '2023-08-18')
lista_acervo = [acervo1, acervo2, acervo3]

class Usuario:
    def __init__(self, apelido, nome, senha, email_usuario, telefone_usuario, contato_publico, redes_sociais):
        self.apelido = apelido
        self.nome = nome
        self.senha = senha
        self.email_usuario = email_usuario
        self.telefone_usuario = telefone_usuario
        self.contato_publico = contato_publico
        self.redes_sociais = redes_sociais


usuario1 = Usuario("CA", "Carlos Alberto", "123456", "carlos@gmail.com", "3232-3232", "S", "Instagram & Twitter")
usuario2 = Usuario("CB", "Carla Beatriz",  "123456", "carla@gmail.com", "1111-1111", "S", "Instagram & Twitter")
usuario3 = Usuario("LL", "Luciane Lopes",  "123456", "luciane@gmail.com", "2222-2222", "S", "Instagram & Twitter")

# Dicionário de usuários
usuarios = {usuario1.apelido: usuario1,
            usuario2.apelido: usuario2,
            usuario3.apelido: usuario3}
'''

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

# db = SQLAlchemy(app)




@app.route('/')
def index():
    lista_acervo = Acervo.query.order_by(Acervo.idAcervo)
    return render_template('index.html', titulo='Bem-vindo ao Partitoteca', acervos=lista_acervo)


@app.route('/pais')
def pais():
    lista_pais = Pais.query.order_by(Pais.idPais)
    return render_template('pais.html', titulo='Bem-vindo ao Partitoteca', paises=lista_pais)



@app.route('/usuarios')
def usuarios():

    return render_template('usuarios.html', titulo='Usuários', usuarios='dict_usuario')


@app.route('/novo_usuario')
def novo_usuario():

    # Testando se o usuário está logado
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo_usuario')))

    return render_template('novo_usuario.html', titulo1='Dados do Acervo', titulo2='Dados do Usuário')


@app.route('/cria_acervo', methods=['POST', ])
def cria_acervo():
    descricao_acervo = request.form['descricao_acervo']
    telefone_acervo = request.form['telefone_acervo']
    email_acervo = request.form['email_acervo']
    sigla = request.form['sigla']
    localizacao = request.form['localizacao']
    publico = request.form['publico']

    acervo = Acervo(descricao_acervo, telefone_acervo, email_acervo, sigla, localizacao, publico)
    acervos = lista_acervo.append(acervo)
    return redirect(url_for('index'))


@app.route('/cria_usuario', methods=['POST', ])
def cria_usuario():
    apelido = request.form['apelido']
    nome = request.form['nome']
    email_usuario = request.form['email_usuario']
    senha = request.form['senha']
    telefone_usuario = request.form['telefone_usuario']
    contato_publico = request.form['contato_publico']
    redes_sociais = request.form['redes_sociais']

    usuario = Usuario(apelido, nome, email_usuario, senha, telefone_usuario, contato_publico, redes_sociais)
    # usuarios = dict_usuario.append(usuario)

    return redirect(url_for('usuarios'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


# Faz o login do usuário
@app.route('/autenticar', methods=['POST', ])
def autenticar():

    # Pesquisa dentro do dicionário usuarios
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:

            # Se a senha bater, colocar o usuário dentro da session
            session['usuario_logado'] = usuario.apelido
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

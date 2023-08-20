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

class Andamento(db.Model):
    idAndamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Compositor(db.Model):
    idObra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idPessoa = db.Column(db.Integer, nullable=False)
    idAcervo = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


class Conjunto(db.Model):
    idConjunto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


class Conjunto_pessoa(db.Model):
    idConjunto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idPessoa = db.Column(db.Integer, nullable=False)
    idAcervo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Container(db.Model):
    idContainer = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


class Container_partitura(db.Model):
    idContainer = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idPartitura = db.Column(db.Integer, nullable=False)
    idAcervo = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


class Edicao(db.Model):
    idPartitura = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idEditora = db.Column(db.Integer, nullable=False)
    idAcervo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    anoEdicao = db.Column(db.String(4), nullable=False)
    numEdicao = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Editora(db.Model):
    idEditora = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Forma(db.Model):
    idForma = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Genero(db.Model):
    idGenero = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


class Instrumento(db.Model):
    idInstrumento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Instrumento_pessoa(db.Model):
    idInstrumento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idPessoa = db.Column(db.Integer, nullable=False)
    idAcervo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

# class Letrista

class Obra(db.Model):
    idObra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    idPeriodo = db.Column(db.Integer, nullable=True)
    idTipoCodigoInternacional = db.Column(db.Integer, nullable=True)
    titulo = db.Column(db.String(200), nullable=False)
    dtInclusao = db.Column(db.Date, nullable=False)
    tituloAlternativo = db.Column(db.String(200), nullable=True)
    notas = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<Name %r>' % self.nome


class Pais(db.Model):
    idPais = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    sigla3 = db.Column(db.String(3), nullable=False)
    sigla2 = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Partitura(db.Model):
    idPartitura = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idVersao = db.Column(db.Integer, nullable=False)
    idAcervo = db.Column(db.Integer, nullable=False)
    nivelDificuldade = db.Column(db.String(50), nullable=True)
    codigoLocalizacao = db.Column(db.String(50), nullable=False)
    linkLocalizacao = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Periodo(db.Model):
    idPeriodo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Pessoa(db.Model):
    idPessoa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    idPais = db.Column(db.Integer, nullable=True)
    nome = db.Column(db.String(100), nullable=False)
    dtNascimento = db.Column(db.Date, nullable=True)
    nomeComum = db.Column(db.String(100), nullable=True)
    dtInclusao = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


# class Restauracao

class Tipo_codigo_internacional(db.Model):
    idTipoCodigoInternacional = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Tipo_variacao(db.Model):
    idTipoVariacao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Tonalidade(db.Model):
    idTonalidade = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


class Usuario(db.Model):
    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    apelido = db.Column(db.String(20), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(8), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=True)
    alterarSenha = db.Column(db.String(1), nullable=False)
    contatoPublico = db.Column(db.String(1), nullable=False)
    redesSociais = db.Column(db.String(200), nullable=True)
    dtInclusao = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Usuario_acervo(db.Model):
    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idAcervo = db.Column(db.Integer, nullable=False)
    tpUsuario = db.Column(db.String(1), nullable=False)
    dtInclusao = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

class Versao(db.Model):
    idVersao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idObra = db.Column(db.Integer, nullable=False)
    idAcervo = db.Column(db.Integer, nullable=False)
    idGenero     = db.Column(db.Integer, nullable=False)
    idForma = db.Column(db.Integer, nullable=False)
    idAndamento = db.Column(db.Integer, nullable=False)
    idTonalidade = db.Column(db.Integer, nullable=False)
    idTipoVariacao = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    publica = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome

# class Versionador


# FIM DAS CLASSES MODELS


@app.route('/')
def index():
    lista_acervo = Acervo.query.order_by(Acervo.idAcervo)
    return render_template('index.html', titulo='Bem-vindo ao Partitoteca', acervos=lista_acervo)

@app.route('/acervo')
def acervo():
    lista_acervo = Acervo.query.order_by(Acervo.idAcervo)
    return render_template('acervo.html', titulo='Lista de Acervos', acervos=lista_acervo)

@app.route('/andamento')
def andamento():
    lista_andamento = Andamento.query.order_by(Andamento.descricao)
    return render_template('andamento.html', titulo='Lista de Andamentos', andamentos=lista_andamento)

@app.route('/compositor')
def compositor():
    lista_compositor = Compositor.query.order_by(Compositor.idObra)
    return render_template('compositor.html', titulo='Lista de Compositores', compositores=lista_compositor)

@app.route('/conjunto')
def conjunto():
    lista_conjunto = Conjunto.query.order_by(Conjunto.descricao)
    return render_template('conjunto.html', titulo='Lista de Conjuntos', conjuntos=lista_conjunto)

@app.route('/conjunto_pessoa')
def conjunto_pessoa():
    lista_conjunto_pessoa = Conjunto_pessoa.query.order_by(Conjunto_pessoa.idConjunto)
    return render_template('conjunto_pessoa.html', titulo='Lista de Conjuntos Pessoa', conjuntos_pessoas=lista_conjunto_pessoa)

@app.route('/container')
def container():
    lista_container = Container.query.order_by(Container.descricao)
    return render_template('container.html', titulo='Lista de Containers', containers=lista_container)

@app.route('/container_partitura')
def container_partitura():
    lista_container_partitura = Container_partitura.query.order_by(Container_partitura.idContainer)
    return render_template('container_partitura.html', titulo='Lista de Partituras por Containers ', containers_partituras=lista_container_partitura)

@app.route('/edicao')
def edicao():
    lista_edicao = Edicao.query.order_by(Edicao.descricao)
    return render_template('edicao.html', titulo='Lista de Edições ', edicoes=lista_edicao)

@app.route('/editora')
def editora():
    lista_editora = Editora.query.order_by(Editora.nome)
    return render_template('editora.html', titulo='Lista de Editoras ', editoras=lista_editora)

@app.route('/forma')
def forma():
    lista_forma = Forma.query.order_by(Forma.descricao)
    return render_template('forma.html', titulo='Lista de Formas', formas=lista_forma)

@app.route('/genero')
def genero():
    lista_genero = Genero.query.order_by(Genero.descricao)
    return render_template('genero.html', titulo='Lista de Gêneros', generos=lista_genero)

@app.route('/instrumento')
def instrumento():
    lista_instrumento = Instrumento.query.order_by(Instrumento.descricao)
    return render_template('instrumento.html', titulo='Lista de Instrumentos', instrumentos=lista_instrumento)

@app.route('/instrumento_pessoa')
def instrumento_pessoa():
    lista_instrumento_pessoa = Instrumento_pessoa.query.order_by(Instrumento_pessoa.descricao)
    return render_template('instrumento_pessoa.html', titulo='Lista de Instrumentos da Pessoa', instrumentos_pessoas=lista_instrumento_pessoa)

# @app.route('/letrista')

@app.route('/obra')
def obra():
    lista_obra = Obra.query.order_by(Obra.titulo)
    return render_template('obra.html', titulo='Lista de Obras', obras=lista_obra)

@app.route('/pais')
def pais():
    lista_pais = Pais.query.order_by(Pais.nome)
    return render_template('pais.html', titulo='Lista de países', paises=lista_pais)

@app.route('/partitura')
def partitura():
    lista_partitura = Partitura.query.order_by(Partitura.idPartitura)
    return render_template('partitura.html', titulo='Lista de Partituras', partituras=lista_partitura)

@app.route('/periodo')
def periodo():
    lista_periodo = Periodo.query.order_by(Periodo.descricao)
    return render_template('periodo.html', titulo='Lista de Períodos', periodos=lista_periodo)

@app.route('/pessoa')
def pessoa():
    lista_pessoa = Pessoa.query.order_by(Pessoa.nome)
    return render_template('pessoa.html', titulo='Lista de Pessoas', pessoas=lista_pessoa)

# @app.route('/restauracao')

@app.route('/tipo_codigo_internacional')
def tipo_codigo_internacional():
    lista_tipo_codigo_internacional = Tipo_codigo_internacional.query.order_by(Tipo_codigo_internacional.descricao)
    return render_template('tipo_codigo_internacional.html', titulo='Lista de Tipos de Códigos Internacionais', tipos_codigos_internacionais=lista_tipo_codigo_internacional)


@app.route('/tipo_variacao')
def tipo_variacao():
    lista_tipo_variacao = Tipo_variacao.query.order_by(Tipo_variacao.descricao)
    return render_template('tipo_variacao.html', titulo='Lista de Tipos de Variações', tipos_variacoes=lista_tipo_variacao)

@app.route('/tonalidade')
def tonalidade():
    lista_tonalidade = Tonalidade.query.order_by(Tonalidade.descricao)
    return render_template('tonalidade.html', titulo='Lista de Tonalidades', tonalidades=lista_tonalidade)

@app.route('/usuario')
def usuario():
    lista_usuario = Usuario.query.order_by(Usuario.nome)
    return render_template('usuario.html', titulo='Lista de Usuários', usuarios=lista_usuario)

@app.route('/usuario_acervo')
def usuario_acervo():
    lista_usuario_acervo = Usuario_acervo.query.order_by(Usuario_acervo.idAcervo)
    return render_template('usuario_acervo.html', titulo='Lista de Usuários por Acervo', usuarios_acervos=lista_usuario_acervo)

@app.route('/versao')
def versao():
    lista_versao = Versao.query.order_by(Versao.descricao)
    return render_template('versao.html', titulo='Lista de Versões', versões=lista_versao)

# @app.route('/versionador')

##################
# ROTAS DE CRIAÇÃO
##################

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
    if request.form['usuario'] in lista_usuario:
        usuario = lista_usuario[request.form['usuario']]
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

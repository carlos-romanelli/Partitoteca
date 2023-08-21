import datetime
from flask import render_template, request, redirect, session, flash, url_for
from app import app, db
from models import Acervo, Andamento, Compositor, Conjunto, Conjunto_pessoa, Container, Container_partitura, Edicao, \
    Editora, Forma, Genero, Instrumento, Instrumento_pessoa, Obra, Pais, Partitura, Periodo, Pessoa, \
    Tipo_codigo_internacional, Tipo_variacao, Tonalidade, Usuario, Usuario_acervo, Versao


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
    return render_template('conjunto_pessoa.html', titulo='Lista de Conjuntos Pessoa',
                           conjuntos_pessoas=lista_conjunto_pessoa)


@app.route('/container')
def container():
    lista_container = Container.query.order_by(Container.descricao)
    return render_template('container.html', titulo='Lista de Containers',
                           containers=lista_container)


@app.route('/container_partitura')
def container_partitura():
    lista_container_partitura = Container_partitura.query.order_by(Container_partitura.idContainer)
    return render_template('container_partitura.html', titulo='Lista de Partituras por Containers ',
                           containers_partituras=lista_container_partitura)


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
    return render_template('instrumento_pessoa.html', titulo='Lista de Instrumentos da Pessoa',
                           instrumentos_pessoas=lista_instrumento_pessoa)

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
    return render_template('tipo_codigo_internacional.html', titulo='Lista de Tipos de Códigos Internacionais',
                           tipos_codigos_internacionais=lista_tipo_codigo_internacional)


@app.route('/tipo_variacao')
def tipo_variacao():
    lista_tipo_variacao = Tipo_variacao.query.order_by(Tipo_variacao.descricao)
    return render_template('tipo_variacao.html', titulo='Lista de Tipos de Variações',
                           tipos_variacoes=lista_tipo_variacao)


@app.route('/tonalidade')
def tonalidade():
    lista_tonalidade = Tonalidade.query.order_by(Tonalidade.descricao)
    return render_template('tonalidade.html', titulo='Lista de Tonalidades',
                           tonalidades=lista_tonalidade)


@app.route('/usuario')
def usuario():
    lista_usuario = Usuario.query.order_by(Usuario.nome)
    return render_template('usuario.html', titulo='Lista de Usuários', usuarios=lista_usuario)


@app.route('/usuario_acervo')
def usuario_acervo():
    lista_usuario_acervo = Usuario_acervo.query.order_by(Usuario_acervo.idAcervo)
    return render_template('usuario_acervo.html', titulo='Lista de Usuários por Acervo',
                           usuarios_acervos=lista_usuario_acervo)


@app.route('/versao')
def versao():
    lista_versao = Versao.query.order_by(Versao.descricao)
    return render_template('versao.html', titulo='Lista de Versões', versoes=lista_versao)

# @app.route('/versionador')

##################
# ROTAS DE CRIAÇÃO
##################


@app.route('/novo_usuario')
def novo_usuario():

    # Testando se o usuário está logado
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo_usuario')))

    return render_template('novo_usuario.html', titulo='Novo Usuário')


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
    senha = request.form['senha']
    email = request.form['email_usuario']
    telefone = request.form['telefone_usuario']
    contatoPublico = request.form['contato_publico']
    alterarSenha = request.form['alterar_senha']
    redesSociais = request.form['redes_sociais']
    #dtInclusao = request.form['data_inclusao']
    dtInclusao = datetime.date.today()


    usuario_criar = Usuario.query.filter_by(apelido=apelido).first()
    if usuario_criar:
        flash('Usuário já existe')
        return redirect(url_for('index'))

    novo_usuario = Usuario(apelido=apelido,
                           nome=nome,
                           senha=senha,
                           email=email,
                           telefone=telefone,
                           contatoPublico=contatoPublico,
                           alterarSenha=alterarSenha,
                           redesSociais=redesSociais,
                           dtInclusao=dtInclusao)

    db.session.add(novo_usuario)
    db.session.commit()

    return redirect(url_for('usuario'))


@app.route('/atualiza_usuario', methods=['POST', ])
def atualiza_usuario():
    usuario = Usuario.query.filter_by(idUsuario=request.form['idUsuario']).first()
    usuario.apelido = request.form['apelido']
    usuario.nome = request.form['nome']
    usuario.senha = request.form['senha']
    usuario.email = request.form['email_usuario']
    usuario.telefone = request.form['telefone_usuario']
    usuario.contatoPublico = request.form['contato_publico']
    usuario.alterarSenha = request.form['alterar_senha']
    usuario.redesSociais = request.form['redes_sociais']
    #usuario.dtInclusao = request.form['dtInclusao']

    db.session.add(usuario)
    db.session.commit()

    return redirect(url_for('usuario'))

@app.route('/edita_usuario/<int:id>')
def edita_usuario(id):

    # Testando se o usuário está logado
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('edita_usuario')))

    usuario = Usuario.query.filter_by(idUsuario=id).first()

    return render_template('edita_usuario.html', titulo='Edição de Usuário', usuario=usuario)



@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


# Faz o login do usuário
@app.route('/autenticar', methods=['POST', ])
def autenticar():

    usuario = Usuario.query.filter_by(apelido=request.form['usuario']).first()
    if usuario:
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

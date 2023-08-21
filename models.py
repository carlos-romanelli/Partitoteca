from app import db

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

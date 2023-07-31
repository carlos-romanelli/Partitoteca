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

# PERIGO!!! Apaga o banco se ele existe - PERIGOSO!!!
cursor.execute("DROP DATABASE IF EXISTS `partitoteca`;")

# cria o banco
cursor.execute("CREATE DATABASE `partitoteca`;")

cursor.execute("USE `partitoteca`;")

# cria um dicionário com os INSERTs para criar as tabelas do banco
# Nem todas serão preenchidas

TABLES = {}

# 1 - pais
TABLES['pais'] = ('''
      CREATE TABLE `pais` (
      `idPais` int NOT NULL AUTO_INCREMENT,
      `nome` varchar(150) NOT NULL,
      `sigla3` char(3) NOT NULL,
      `sigla2` char(2) NOT NULL,
      PRIMARY KEY (`idPais`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')

# 2 - tipo_variacao
TABLES['tipo_variacao'] = ('''
      CREATE TABLE `tipo_variacao` (
      `idTipoVariacao` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `descricao` varchar(50) NOT NULL,
      PRIMARY KEY (`idTipoVariacao`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')

# 3 - periodo
TABLES['periodo'] = ('''
      CREATE TABLE `periodo` (
      `idPeriodo` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `descricao` varchar(50) NOT NULL,
      PRIMARY KEY (`idPeriodo`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')


# 4 - tipo_codigo_internacional
TABLES['tipo_codigo_internacional'] = ('''
      CREATE TABLE `tipo_codigo_internacional` (
      `idTipoCodigoInternacional` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `descricao` varchar(20) NOT NULL,
      PRIMARY KEY (`idTipoCodigoInternacional`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')


# 5 - genero
TABLES['genero'] = ('''
      CREATE TABLE `genero` (
      `idGenero` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `descricao` varchar(50) NOT NULL,
      PRIMARY KEY (`idGenero`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')


# 6 - forma
TABLES['forma'] = ('''
      CREATE TABLE `forma` (
      `idForma` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `descricao` varchar(50) NOT NULL,
      PRIMARY KEY (`idForma`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')

# 7 - andamento
TABLES['andamento'] = ('''
      CREATE TABLE `andamento` (
      `idAndamento` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `descricao` varchar(50) NOT NULL,
      PRIMARY KEY (`idAndamento`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')

# 8 - tonalidade
TABLES['tonalidade'] = ('''
      CREATE TABLE `tonalidade` (
      `idTonalidade` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `descricao` varchar(50) NOT NULL,
      PRIMARY KEY (`idTonalidade`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')

# 9 - pessoa
TABLES['pessoa'] = ('''
      CREATE TABLE `pessoa` (
      `idPessoa` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `nome` varchar(100) NOT NULL,
      `dtNascimento` date,
      `idPais` int,
      `nomeComum` varchar(100),
      `dtInclusao` date NOT NULL,
      PRIMARY KEY (`idPessoa`)      
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')


# 10 - container
TABLES['container'] = ('''
      CREATE TABLE `container` (
      `idContainer` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `descricao` varchar(50) NOT NULL,
      PRIMARY KEY (`idContainer`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')

# 11 - instrumento
TABLES['instrumento'] = ('''
      CREATE TABLE `instrumento` (
      `idInstrumento` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `descricao` varchar(50) NOT NULL,
      PRIMARY KEY (`idInstrumento`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')


# 12 - conjunto
TABLES['conjunto'] = ('''
      CREATE TABLE `conjunto` (
      `idConjunto` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `descricao` varchar(100) NOT NULL,
      PRIMARY KEY (`idConjunto`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')

# Tabelas que serão só criadas e não preenchidas

# 13 - Usuario
TABLES['usuario'] = ('''
      CREATE TABLE `usuario` (
      `idUsuario` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `apelido` varchar(20) NOT NULL,
      `nome` varchar(100) NOT NULL,
      `senha` varchar(8) NOT NULL,
      `tpUsuario` char(1) NOT NULL,
      `email` varchar(100) NOT NULL,
      `telefone` varchar(100),
      `contatoPublico` char(1) NOT NULL,
      `alterarSenha` char(1) NOT NULL,
      `redesSociais` varchar(200),
      `dtInclusao` date NOT NULL,
      PRIMARY KEY (`idUsuario`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')


# 14 - Acervo
TABLES['acervo'] = ('''
      CREATE TABLE `acervo` (
      `idAcervo` int NOT NULL AUTO_INCREMENT,
      `descricao` varchar(100) NOT NULL,
      `telefone` varchar(20),
      `email` varchar(100) NOT NULL,
      `sigla` varchar(20) NOT NULL,
      `localizacao` varchar(100) NOT NULL,
      `publico` char(1) NOT NULL,
      `dtInclusao` date NOT NULL,
      PRIMARY KEY (`idAcervo`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')


# 15 - Obra
TABLES['obra'] = ('''
      CREATE TABLE `obra` (
      `idObra` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `idPeriodo` int NOT NULL,
      `idTipoCodigoInternacional` int NOT NULL,
      `titulo` varchar(200) NOT NULL,
      `dtInclusao` date NOT NULL,
      `tituloAlternativo` varchar(200),
      `notas` varchar (200),
      PRIMARY KEY (`idObra`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')

# 16 - Compositor
TABLES['compositor'] = ('''
      CREATE TABLE `compositor` (
      `idObra` int NOT NULL,
      `idPessoa` int NOT NULL,
      `idAcervo` int NOT NULL,
      PRIMARY KEY (`idObra`, `idPessoa`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')


# 17 - Instrumento_Pessoa

TABLES['instrumento_pessoa'] = ('''
      CREATE TABLE `instrumento_pessoa` (
      `idInstrumento` int NOT NULL,
      `idPessoa` int NOT NULL,
      `idAcervo` int NOT NULL,
      `descricao` varchar(100) NOT NULL,
      PRIMARY KEY (`idInstrumento`, `idPessoa`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')


# 18 - Conjunto_Pessoa
TABLES['conjunto_pessoa'] = ('''
      CREATE TABLE `conjunto_pessoa` (
      `idConjunto` int NOT NULL,
      `idPessoa` int NOT NULL,
      `idAcervo` int NOT NULL,
      `descricao` varchar(100) NOT NULL,
      PRIMARY KEY (`idConjunto`, `idPessoa`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')


# 19 - Letrista
TABLES['letrista'] = ('''
      CREATE TABLE `letrista` (
      `idVersao` int NOT NULL,
      `idPessoa` int NOT NULL,
      `idAcervo` int NOT NULL,
      PRIMARY KEY (`idVersao`, `idPessoa`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')

# 20 - Editora
TABLES['editora'] = ('''
      CREATE TABLE `editora` (
      `idEditora` int NOT NULL AUTO_INCREMENT,
      `idAcervo` int NOT NULL,
      `nome` varchar(100) NOT NULL,
      PRIMARY KEY (`idEditora`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')

# 21  - Partitura
TABLES['partitura'] = ('''
      CREATE TABLE `partitura` (
      `idPartitura` int NOT NULL AUTO_INCREMENT,
      `idVersao` int NOT NULL,
      `idAcervo` int NOT NULL,
      `nivelDificuldade` varchar(50),
      `codigoLocalizacao` varchar(50) NOT NULL,
      `linkLocalizacao` varchar(300)  NOT NULL,
      PRIMARY KEY (`idPartitura`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')


# 22  - Container_partitura
TABLES['container_partitura'] = ('''
      CREATE TABLE `container_partitura` (
      `idContainer` int NOT NULL,
      `idPartitura` int NOT NULL,
      `idAcervo` int NOT NULL,
      PRIMARY KEY (`idContainer`, `idPartitura`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')

# 23  - Edicao
TABLES['edicao'] = ('''
      CREATE TABLE `edicao` (
      `idPartitura` int NOT NULL,
      `idEditora` int NOT NULL,
      `idAcervo` int NOT NULL,
      `descricao` varchar(100) NOT NULL,
      `anoEdicao` char(4) NOT NULL,
      `numEdicao` varchar(10)  NOT NULL,
      PRIMARY KEY (`idPartitura`, `idEditora`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')


# 24  - Restauracao
TABLES['restauracao'] = ('''
      CREATE TABLE `restauracao` (
      `idRestauracao` int NOT NULL AUTO_INCREMENT,
      `idPartitura` int NOT NULL,
      `idPessoa` int NOT NULL,
      `idAcervo` int NOT NULL,
      `descricao` varchar(100) NOT NULL,
      `dataInicio` date NOT NULL,
      `dataFim` date,
      `motivo` varchar(200),
      `tecnica` varchar(200),
      `resultado` varchar(200),
      `notas` varchar (200),
      PRIMARY KEY (`idRestauracao`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')

# 25  - Versao
TABLES['versao'] = ('''
      CREATE TABLE `versao` (
      `idVersao` int NOT NULL AUTO_INCREMENT,
      `idObra` int NOT NULL,
      `idAcervo` int NOT NULL,
      `idGenero` int NOT NULL,
      `idForma` int NOT NULL,
      `idAndamento` int NOT NULL,
      `idTonalidade` int NOT NULL,
      `idTipoVariacao` int NOT NULL,
      `descricao` varchar(100) NOT NULL,
      `publica` char(1),
      PRIMARY KEY (`idVersao`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')


# 26  - Versionador
TABLES['versionador'] = ('''
      CREATE TABLE `versionador` (
      `idVersao` int NOT NULL,
      `idPessoa` int NOT NULL,
      `idAcervo` int NOT NULL,
      PRIMARY KEY (`idVersao`, `idPessoa`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;''')

# Aproveita o for da criação das tabelas para criar as chaves estrangeiras

# 1 pais - Não tem

# 2 tipo_variacao
TABLES['fkTipoVariacao_Acervo'] = ('''
      ALTER TABLE `tipo_variacao` ADD CONSTRAINT `fkTipoVariacao_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 3 periodo
TABLES['fkPeriodo_Acervo'] = ('''
      ALTER TABLE `periodo` ADD CONSTRAINT `fkPeriodo_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 4 tipo_codigo_internacional
TABLES['fkTipoCodigoInternacional_Acervo'] = ('''
      ALTER TABLE `tipo_codigo_internacional` ADD CONSTRAINT `fkTipoCodigoInternacional_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 5 genero
TABLES['fkGenero_Acervo'] = ('''
      ALTER TABLE `genero` ADD CONSTRAINT `fkGenero_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 6 forma
TABLES['fkForma_Acervo'] = ('''
      ALTER TABLE `forma` ADD CONSTRAINT `fkForma_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 7 andamento
TABLES['fkAndamento_Acervo'] = ('''
      ALTER TABLE `andamento` ADD CONSTRAINT `fkAndamento_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 8 tonalidade
TABLES['fkTonalidade_Acervo'] = ('''
      ALTER TABLE `tonalidade` ADD CONSTRAINT `fkTonalidade_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 9 pessoa
TABLES['fkPessoa_Acervo'] = ('''
      ALTER TABLE `pessoa` ADD CONSTRAINT `fkPessoa_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 10 container
TABLES['fkContainer_Acervo'] = ('''
      ALTER TABLE `container` ADD CONSTRAINT `fkContainer_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 11 instrumento
TABLES['fkInstrumento_Acervo'] = ('''
      ALTER TABLE `instrumento` ADD CONSTRAINT `fkInstrumento_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 12 conjunto
TABLES['fkConjunto_Acervo'] = ('''
      ALTER TABLE `conjunto` ADD CONSTRAINT `fkConjunto_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 13 usuario
TABLES['fkUsuario_Acervo'] = ('''
      ALTER TABLE `usuario` ADD CONSTRAINT `fkUsuario_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 14 acervo - Não possui

# 15 obra
TABLES['fkObra_Acervo'] = ('''
      ALTER TABLE `obra` ADD CONSTRAINT `fkObra_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

TABLES['fkObra_Periodo'] = ('''
      ALTER TABLE `obra` ADD CONSTRAINT `fkObra_Periodo` FOREIGN KEY (`idPeriodo`) 
      REFERENCES `periodo` (`idPeriodo`);''')

TABLES['fkObra_TipoCodigoInternacional'] = ('''
      ALTER TABLE `obra` ADD CONSTRAINT `fkObra_TipoCodigoInternacional` FOREIGN KEY (`idTipoCodigoInternacional`) 
      REFERENCES `tipo_codigo_internacional` (`idTipoCodigoInternacional`);''')


# 16 compositor
TABLES['fkCompositor_Obra'] = ('''
      ALTER TABLE `compositor` ADD CONSTRAINT `fkCompositor_Obra` FOREIGN KEY (`idObra`) 
      REFERENCES `obra` (`idObra`);''')

TABLES['fkCompositor_Pessoa'] = ('''
      ALTER TABLE `compositor` ADD CONSTRAINT `fkCompositor_Pessoa` FOREIGN KEY (`idPessoa`) 
      REFERENCES `pessoa` (`idPessoa`);''')

TABLES['fkCompositor_Acervo'] = ('''
      ALTER TABLE `compositor` ADD CONSTRAINT `fkCompositor_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')


# 17 instrumento_pessoa
TABLES['fkInstrumentoPessoa_Pessoa'] = ('''
      ALTER TABLE `instrumento_pessoa` ADD CONSTRAINT `fkInstrumentoPessoa_Pessoa` FOREIGN KEY (`idPessoa`) 
      REFERENCES `pessoa` (`idPessoa`);''')

TABLES['fkInstrumentoPessoa_Instrumento'] = ('''
      ALTER TABLE `instrumento_pessoa` ADD CONSTRAINT `fkInstrumentoPessoa_Instrumento` FOREIGN KEY (`idInstrumento`) 
      REFERENCES `instrumento` (`idInstrumento`);''')

TABLES['fkInstrumentoPessoa_Acervo'] = ('''
      ALTER TABLE `instrumento_pessoa` ADD CONSTRAINT `fkInstrumentoPessoa_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')


# 18 conjunto_pessoa
TABLES['fkConjuntoPessoa_Pessoa'] = ('''
      ALTER TABLE `conjunto_pessoa` ADD CONSTRAINT `fkConjuntoPessoa_Pessoa` FOREIGN KEY (`idPessoa`) 
      REFERENCES `pessoa` (`idPessoa`);''')

TABLES['fkConjuntoPessoa_Conjunto'] = ('''
      ALTER TABLE `conjunto_pessoa` ADD CONSTRAINT `fkConjuntoPessoa_Conjunto` FOREIGN KEY (`idConjunto`) 
      REFERENCES `conjunto` (`idConjunto`);''')

TABLES['fkConjuntoPessoa_Acervo'] = ('''
      ALTER TABLE `conjunto_pessoa` ADD CONSTRAINT `fkConjuntoPessoa_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 19 letrista
TABLES['fkLetrista_Versao'] = ('''
      ALTER TABLE `letrista` ADD CONSTRAINT `fkLetrista_Versao` FOREIGN KEY (`idVersao`) 
      REFERENCES `versao` (`idVersao`);''')

TABLES['fkLetrista_Pessoa'] = ('''
      ALTER TABLE `letrista` ADD CONSTRAINT `fkLetrista_Pessoa` FOREIGN KEY (`idPessoa`) 
      REFERENCES `pessoa` (`idPessoa`);''')

TABLES['fkLetrista_Acervo'] = ('''
      ALTER TABLE `letrista` ADD CONSTRAINT `fkLetrista_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')


# 20 editora
TABLES['fkEditora_Acervo'] = ('''
      ALTER TABLE `editora` ADD CONSTRAINT `fkEditora_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')


# 21 container_partitura
TABLES['fkContainerPartitura_Partitura'] = ('''
      ALTER TABLE `container_partitura` ADD CONSTRAINT `fkContainerPartitura_Partitura` FOREIGN KEY (`idPartitura`) 
      REFERENCES `partitura` (`idPartitura`);''')

TABLES['fkContainerPartitura_Container'] = ('''
      ALTER TABLE `container_partitura` ADD CONSTRAINT `fkContainerPartitura_Container` FOREIGN KEY (`idContainer`) 
      REFERENCES `container` (`idContainer`);''')

TABLES['fkContainerPartitura_Acervo'] = ('''
      ALTER TABLE `container_partitura` ADD CONSTRAINT `fkContainerPartitura_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 22 edicao
TABLES['fkEdicao_Editora'] = ('''
      ALTER TABLE `edicao` ADD CONSTRAINT `fkEdicao_Editora` FOREIGN KEY (`idEditora`) 
      REFERENCES `editora` (`idEditora`);''')

TABLES['fkEdicao_Partitura'] = ('''
      ALTER TABLE `edicao` ADD CONSTRAINT `fkEdicao_Partitura` FOREIGN KEY (`idPartitura`) 
      REFERENCES `partitura` (`idPartitura`);''')

TABLES['fkEdicao_Acervo'] = ('''
      ALTER TABLE `edicao` ADD CONSTRAINT `fkEdicao_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')


# 23 partitura
TABLES['fkPartitura_versao'] = ('''
      ALTER TABLE `partitura` ADD CONSTRAINT `fkPartitura_Versao` FOREIGN KEY (`idVersao`) 
      REFERENCES `versao` (`idVersao`);''')
TABLES['fkPartitura_Acervo'] = ('''
      ALTER TABLE `partitura` ADD CONSTRAINT `fkPartitura_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')


# 24 restauracao
TABLES['fkRestauracao_Pessoa'] = ('''
      ALTER TABLE `restauracao` ADD CONSTRAINT `fkVRestauracao_Pessoa` FOREIGN KEY (`idPessoa`) 
      REFERENCES `pessoa` (`idPessoa`);''')

TABLES['fkRestauracao_Partitura'] = ('''
      ALTER TABLE `restauracao` ADD CONSTRAINT `fkVRestauracao_Partitura` FOREIGN KEY (`idPartitura`) 
      REFERENCES `partitura` (`idPartitura`);''')

TABLES['fkRestauracao_Acervo'] = ('''
      ALTER TABLE `restauracao` ADD CONSTRAINT `fkVRestauracao_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

# 25 versao
TABLES['fkVersao_Obra'] = ('''
      ALTER TABLE `versao` ADD CONSTRAINT `fkVersao_Obra` FOREIGN KEY (`idObra`) 
      REFERENCES `obra` (`idObra`);''')

TABLES['fkVersao_Acervo'] = ('''
      ALTER TABLE `versao` ADD CONSTRAINT `fkVersao_Acervo` FOREIGN KEY (`idAcervo`) 
      REFERENCES `acervo` (`idAcervo`);''')

TABLES['fkVersao_Genero'] = ('''
      ALTER TABLE `versao` ADD CONSTRAINT `fkVersao_Genero` FOREIGN KEY (`idGenero`) 
      REFERENCES `genero` (`idGenero`);''')

TABLES['fkVersao_Forma'] = ('''
      ALTER TABLE `versao` ADD CONSTRAINT `fkVersao_Forma` FOREIGN KEY (`idForma`) 
      REFERENCES `forma` (`idForma`);''')

TABLES['fkVersao_Andamento'] = ('''
      ALTER TABLE `versao` ADD CONSTRAINT `fkVersao_Andamento` FOREIGN KEY (`idAndamento`) 
      REFERENCES `andamento` (`idAndamento`);''')


TABLES['fkVersao_Tonalidade'] = ('''
      ALTER TABLE `versao` ADD CONSTRAINT `fkVersao_Tonalidade` FOREIGN KEY (`idTonalidade`) 
      REFERENCES `tonalidade` (`idTonalidade`);''')

TABLES['fkVersao_TipoVariacao'] = ('''
      ALTER TABLE `versao` ADD CONSTRAINT `fkVersao_TipoVariacao` FOREIGN KEY (`idTipoVariacao`) 
      REFERENCES `tipo_variacao` (`idTipoVariacao`);''')


# 26 versionador
TABLES['fkVersionadorVersao'] = ('''
      ALTER TABLE `versionador` ADD CONSTRAINT `fkVersionadorVersao` FOREIGN KEY (`idVersao`) 
      REFERENCES `versao` (`idVersao`);''')

TABLES['fkVersionadorPessoa'] = ('''
      ALTER TABLE `versionador` ADD CONSTRAINT `fkVersionadorPessoa` FOREIGN KEY (`idPessoa`)  
      REFERENCES `pessoa` (`idPessoa`);''')

TABLES['fkVersionador_Acervo'] = ('''
      ALTER TABLE `versionador` ADD CONSTRAINT `fkVersionador_Acervo` FOREIGN KEY (`idAcervo`)  
      REFERENCES `acervo` (`idAcervo`);''')

#####################################################################
# Cria as tabelas do banco com base no dicionário TABLES criado acima
#####################################################################

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print('Criando tabela {}:'.format(tabela_nome), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err.msg)
    else:
        print('OK')


# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()

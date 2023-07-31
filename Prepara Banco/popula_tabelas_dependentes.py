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

cursor.execute("USE `partitoteca`;")

###############################
# POPULANDO TABELAS SECUNDÁRIAS
###############################

####################
# inserindo usuarios
####################
'''
usuario_sql = 'INSERT INTO usuario (idUsuario, idAcervo, apelido, nome, senha, tpUsuario, email, telefone, ' \
              'contatoPublico, alterarSenha, redesSociais, dtInclusao) ' \
              'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
usuario = [
      (1, 1, 'casoba', 'Carlos Alberto Romanelli', '12345678', 'M', 'emaildoroma@gmail.com', '(32)98857-2905',
       'N', 'N', 'Instagram: @romanelli.carlos', '2023-07-24')
]

cursor.executemany(usuario_sql, usuario)


cursor.execute('select * from partitoteca.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[2])

##############################
# inserindo Tipos de Variações
##############################

tipo_sql = 'INSERT INTO tipo_variacao (idAcervo, descricao) VALUES (%s, %s)'
tipos = [
      (1, 'Original'),
      (1, 'Arranjo'),
      (1, 'Transcrição'),
      (1, 'Redução'),
      (1, 'Variação'),
      (1, 'Revisão')
]
cursor.executemany(tipo_sql, tipos)

cursor.execute('select * from partitoteca.tipo_variacao')
print(' -------------  Tipo Variacão:  -------------')
for tipo_variacao in cursor.fetchall():
    print(tipo_variacao[2])

##############################
# inserindo andamentos
##############################

andamento_sql = 'INSERT INTO andamento (idAcervo, descricao) VALUES (%s, %s)'
andamento = [

        (1, 'Larghissimo'),
        (1, 'Grave'),
        (1, 'Lento'),
        (1, 'Largo'),
        (1, 'Adagio'),
        (1, 'Andante'),
        (1, 'Moderato'),
        (1, 'Allegretto'),
        (1, 'Allegro'),
        (1, 'Vivace'),
        (1, 'Presto'),
        (1, 'Prestissimo')
]
cursor.executemany(andamento_sql, andamento)

cursor.execute('select * from partitoteca.andamento')
print(' -------------  Andamentos:  -------------')
for andamento in cursor.fetchall():
    print(andamento[2])

##############################
# inserindo conjuntos
##############################

comando_sql = 'INSERT INTO conjunto (idAcervo,descricao) VALUES (%s, %s)'
comando = [

    (1, 'Orquestra Sinfônica'),
    (1, 'Coral SATB'),
    (1, 'Trio de Cordas'),
    (1, 'Quarteto de Cordas'),
    (1, 'Piano Solo'),
    (1, 'Voz e Violão'),
    (1, 'Voz e Piano'),
    (1, 'Soprano Solo'),
    (1, 'Contralto Solo'),
    (1, 'Tenor Solo'),
    (1, 'Baixo Solo'),
    (1, 'Barítono Solo'),
    (1, 'Contratenor Solo'),
    (1, 'Ópera'),
    (1, 'Banda Sinfônica'),
    (1, 'Grupo de Música Antiga'),
    (1, 'Quinteto de Metais'),
    (1, 'Orquestra de Câmara'),
    (1, 'Duo de Violino e Piano'),
    (1, 'Duo de Flauta e Piano'),
    (1, 'Conjunto de Música Barroca'),
    (1, 'Orquestra de Cordas'),
    (1, 'Quarteto de Sopros'),
    (1, 'Trio de Piano, Violino e Violoncelo'),
    (1, 'Quinteto de Sopros de Madeira'),
    (1, 'Quarteto de Sopros de Metais')


]
cursor.executemany(comando_sql, comando)

cursor.execute('select * from partitoteca.conjunto')
print(' -------------  Conjuntos:  -------------')
for conjunto in cursor.fetchall():
    print(conjunto[2])


##############################
# inserindo pessoa
##############################



comando_sql = 'INSERT INTO pessoa (idAcervo, nome, dtInclusao) VALUES (%s, %s, %s)'
comando = [

(1,'Johann Sebastian Bach','2023-07-23'),
(1,'Ludwig van Beethoven','2023-07-23'),
(1,'Wolfgang Amadeus Mozart','2023-07-23'),
(1,'Franz Schubert','2023-07-23'),
(1,'Richard Wagner','2023-07-23'),
(1,'Johannes Brahms','2023-07-23'),
(1,'Antonio Vivaldi','2023-07-23'),
(1,'George Frideric Handel','2023-07-23'),
(1,'Pyotr Ilyich Tchaikovsky','2023-07-23'),
(1,'Gustav Mahler','2023-07-23'),
(1,'Claude Debussy','2023-07-23'),
(1,'Igor Stravinsky','2023-07-23'),
(1,'Johann Strauss II','2023-07-23'),
(1,'Franz Joseph Haydn','2023-07-23'),
(1,'Frédéric Chopin','2023-07-23'),
(1,'Sergei Rachmaninoff','2023-07-23'),
(1,'Giuseppe Verdi','2023-07-23'),
(1,'Richard Strauss','2023-07-23'),
(1,'Arnold Schoenberg','2023-07-23'),
(1,'Maurice Ravel','2023-07-23'),
(1,'Franz Liszt','2023-07-23'),
(1,'Béla Bartók','2023-07-23'),
(1,'Benjamin Britten','2023-07-23'),
(1,'Dmitri Shostakovich','2023-07-23'),
(1,'Hector Berlioz','2023-07-23'),
(1,'Jean Sibelius','2023-07-23'),
(1,'Carl Orff','2023-07-23'),
(1,'Ralph Vaughan Williams','2023-07-23'),
(1,'Jean-Philippe Rameau','2023-07-23'),
(1,'Claudio Monteverdi','2023-07-23'),
(1,'Giacomo Puccini','2023-07-23'),
(1,'Modest Mussorgsky','2023-07-23'),
(1,'Giuseppe Tartini','2023-07-23'),
(1,'Antonio Salieri','2023-07-23'),
(1,'Edward Elgar','2023-07-23'),
(1,'Camille Saint-Saëns','2023-07-23'),
(1,'Henry Purcell','2023-07-23'),
(1,'John Cage','2023-07-23'),
(1,'Samuel Barber','2023-07-23'),
(1,'Georg Philipp Telemann','2023-07-23'),
(1,'Leonard Bernstein','2023-07-23'),
(1,'Arvo Pärt','2023-07-23'),
(1,'Carl Maria von Weber','2023-07-23'),
(1,'William Byrd','2023-07-23'),
(1,'Sergei Prokofiev','2023-07-23'),
(1,'Charles Ives','2023-07-23'),
(1,'Jean-Baptiste Lully','2023-07-23'),
(1,'Antonín Dvorák','2023-07-23'),
(1,'Hildegard von Bingen','2023-07-23'),
(1,'Henryk Górecki','2023-07-23'),
(1,'Domenico Scarlatti','2023-07-23'),
(1,'Francis Poulenc','2023-07-23'),
(1,'Erik Satie','2023-07-23'),
(1,'Karlheinz Stockhausen','2023-07-23'),
(1,'Aaron Copland','2023-07-23'),
(1,'Georg Friedrich Händel','2023-07-23'),
(1,'Olivier Messiaen','2023-07-23'),
(1,'Luciano Berio','2023-07-23'),
(1,'György Ligeti','2023-07-23'),
(1,'Krzysztof Penderecki','2023-07-23'),
(1,'John Adams','2023-07-23'),
(1,'John Williams','2023-07-23'),
(1,'Carl Nielsen','2023-07-23'),
(1,'François Couperin','2023-07-23'),
(1,'Tomaso Albinoni','2023-07-23'),
(1,'Gioachino Rossini','2023-07-23'),
(1,'Alberto Nepomuceno','2023-07-23'),
(1,'Alexandre Levy','2023-07-23'),
(1,'Almeida Prado','2023-07-23'),
(1,'André da Silva Gomes','2023-07-23'),
(1,'André Filho','2023-07-23'),
(1,'Antonio Ribeiro','2023-07-23'),
(1,'Arnaldo Rebello','2023-07-23'),
(1,'Camargo Guarnieri','2023-07-23'),
(1,'Carlos Gomes','2023-07-23'),
(1,'Celso Mojola','2023-07-23'),
(1,'César Guerra-Peixe','2023-07-23'),
(1,'Cláudio Santoro','2023-07-23'),
(1,'Dimitri Cervo','2023-07-23'),
(1,'Dinorá de Carvalho','2023-07-23'),
(1,'Domingos Caldas Barbosa','2023-07-23'),
(1,'Edmundo Villani-Côrtes','2023-07-23'),
(1,'Edson Zampronha','2023-07-23'),
(1,'Egberto Gismonti','2023-07-23'),
(1,'Elias Álvares Lôbo','2023-07-23'),
(1,'Ernesto Nazareth','2023-07-23'),
(1,'Ernst Mahle','2023-07-23'),
(1,'Estércio Marquez Cunha','2023-07-23'),
(1,'Esther Scliar','2023-07-23'),
(1,'Eunice Katunda','2023-07-23'),
(1,'Flo Menezes','2023-07-23'),
(1,'Francisco Braga','2023-07-23'),
(1,'Francisco Mignone','2023-07-23'),
(1,'Géza Szilvay','2023-07-23'),
(1,'Gilberto Mendes','2023-07-23'),
(1,'H. J. Koellreutter','2023-07-23'),
(1,'Heitor Villa-Lobos','2023-07-23'),
(1,'Henrique Oswald','2023-07-23'),
(1,'João Guilherme Ripper','2023-07-23'),
(1,'Jorge Antunes','2023-07-23'),
(1,'José Albano','2023-07-23'),
(1,'José Augusto Mannis','2023-07-23'),
(1,'José Maurício Nunes Garcia','2023-07-23'),
(1,'José Orlando Alves','2023-07-23'),
(1,'José Penalva','2023-07-23'),
(1,'José Siqueira','2023-07-23'),
(1,'Leo Brouwer','2023-07-23'),
(1,'Liduino Pitombeira','2023-07-23'),
(1,'Lindembergue Cardoso','2023-07-23'),
(1,'Lorenzo Fernândez','2023-07-23'),
(1,'Marcos Lucas','2023-07-23'),
(1,'Mário Ficarelli','2023-07-23'),
(1,'Marlos Nobre','2023-07-23'),
(1,'Maurício Ribeiro','2023-07-23'),
(1,'Osvaldo Lacerda','2023-07-23'),
(1,'Radamés Gnattali','2023-07-23'),
(1,'Ricardo Tacuchian','2023-07-23'),
(1,'Roberto Victorio','2023-07-23'),
(1,'Rodolfo Caesar','2023-07-23'),
(1,'Rodolfo Coelho de Souza','2023-07-23'),
(1,'Ronaldo Miranda','2023-07-23'),
(1,'Rui Coelho','2023-07-23'),
(1,'Silvio Ferraz','2023-07-23'),
(1,'Sônia Ray','2023-07-23'),
(1,'Turi Collura','2023-07-23'),
(1,'Villa-Lobos','2023-07-23'),
(1,'Willy Corrêa de Oliveira','2023-07-23'),
(1,'Wilson Sukorski','2023-07-23'),
(1,'Chiquinha Gonzaga','2023-07-23')

]
cursor.executemany(comando_sql, comando)

cursor.execute('select * from partitoteca.pessoa')

print(' -------------  Pessoas:  -------------')
for pessoa in cursor.fetchall():
    print(pessoa[2])


##############################
# inserindo containers
##############################

comando_sql = 'INSERT INTO container (idAcervo, descricao) VALUES (%s, %s)'
comando = [
      (1, 'Álbum'),
      (1, 'Colatânea'),
      (1, 'coleção'),
      (1, 'Excertos'),
      (1, 'Estudos'),
      (1, 'Encadernação')
]
cursor.executemany(comando_sql, comando)

cursor.execute('select * from partitoteca.container')
print(' -------------  Container:  -------------')
for container in cursor.fetchall():
    print(container[2])


##############################
# inserindo formas
##############################

comando_sql = 'INSERT INTO forma (idAcervo, descricao) VALUES (%s, %s)'
comando = [

(1,'MÚSICA INSTRUMENTAL'),
(1,'MÚSICA VOCAL'),
(1,'CONCERTO'),
(1,'CANTATA'),
(1,'SONATA'),
(1,'VARIAÇÃO'),
(1,'VALSA'),
(1,'ESTUDO'),
(1,'FUGA'),
(1,'PRELÚDIO'),
(1,'SUITE'),
(1,'MÚSICA POPULAR'),
(1,'ABERTURA'),
(1,'FANTASIA'),
(1,'MISSA'),
(1,'ÁRIA'),
(1,'MÚSICA FOLCLÓRICA'),
(1,'LIED'),
(1,'SERENATA'),
(1,'MINUETO'),
(1,'RONDÓ'),
(1,'HINO'),
(1,'MOTETO'),
(1,'DIVERTIMENTO'),
(1,'MARCHA'),
(1,'ÓPERA'),
(1,'VILANCICO'),
(1,'SALMO'),
(1,'NOTURNO'),
(1,'POLONAISE'),
(1,'CÂNONE'),
(1,'RECITATIVO'),
(1,'SINFONIA'),
(1,'POEMA SINFÔNICO'),
(1,'SCHERZO'),
(1,'IMPROVISO'),
(1,'MADRIGAL'),
(1,'RAPSÓDIA'),
(1,'REQUIEM'),
(1,'INTERMEZZO'),
(1,'SONATINA'),
(1,'ANTÍFONA'),
(1,'PRELÚDIO CORAL'),
(1,'BALADA'),
(1,'CANÇÃO'),
(1,'PARTITA'),
(1,'MÚSICA NATALINA'),
(1,'TANGO'),
(1,'MAZURCA'),
(1,'POLCA'),
(1,'BERCEUSE'),
(1,'SAMBA'),
(1,'TE DEUM'),
(1,'TOCATA'),
(1,'BAGATELA'),
(1,'CHACONNE'),
(1,'INTERLÚDIO'),
(1,'MÚSICA ELETROACÚSTICA'),
(1,'MÚSICA ELETRÔNICA'),
(1,'ORATÓRIO'),
(1,'PASSACAGLIA'),
(1,'PASTORAL'),
(1,'STABAT MATER'),
(1,'JAZZ'),
(1,'MODINHA'),
(1,'BARCAROLA'),
(1,'CANTIGA'),
(1,'CANÇÃO TROVADORESCA'),
(1,'MOMENTO MUSICAL'),
(1,'RESPONSÓRIO'),
(1,'CANTO GREGORIANO'),
(1,'CONTRAPONTO'),
(1,'DANÇA'),
(1,'PAVANA'),
(1,'ARRANJO MUSICAL'),
(1,'BALÉ'),
(1,'ELEGIA'),
(1,'HABANERA'),
(1,'ROCK')

]
cursor.executemany(comando_sql, comando)

cursor.execute('select * from partitoteca.forma')
print(' -------------  Formas:  -------------')
for forma in cursor.fetchall():
    print(forma[2])
'''

##############################
# inserindo GÊNEROS
##############################

comando_sql = 'INSERT INTO genero (idAcervo, descricao) VALUES (%s, %s)'
comando = [

(1,'Erudito'),
(1,'Clássico'),
(1,'Pop'),
(1,'Pop Rock'),
(1,'Dance Pop'),
(1,'Electropop'),
(1,'Synthpop'),
(1,'Rock n Roll'),
(1,'Rock Clássico'),
(1,'Rock Alternativo'),
(1,'Rock Progressivo'),
(1,'Indie Rock'),
(1,'Punk Rock'),
(1,'Heavy Metal'),
(1,'Grunge'),
(1,'Hip Hop'),
(1,'Rap'),
(1,'Trap'),
(1,'Gangsta Rap'),
(1,'West Coast Rap'),
(1,'East Coast Rap'),
(1,'Rhythm and Blues (R&B)'),
(1,'Soul'),
(1,'Funk'),
(1,'Motown'),
(1,'Eletrônica'),
(1,'House'),
(1,'Techno'),
(1,'Trance'),
(1,'Dubstep'),
(1,'Country'),
(1,'Country Pop'),
(1,'Bluegrass'),
(1,'Jazz'),
(1,'Swing'),
(1,'Bebop'),
(1,'Smooth Jazz'),
(1,'Reggae'),
(1,'Ska'),
(1,'Dancehall'),
(1,'Latino'),
(1,'Salsa'),
(1,'Merengue'),
(1,'Reggaeton'),
(1,'Bachata'),
(1,'Blues'),
(1,'Delta Blues'),
(1,'Chicago Blues'),
(1,'Folk'),
(1,'Folk Rock'),
(1,'Funk'),
(1,'Gospel'),
(1,'Black Metal'),
(1,'Death Metal'),
(1,'Power Metal'),
(1,'Trash Metal'),
(1,'Progressive Metal'),
(1,'Música Étnica'),
(1,'Música Tradicional')


]
cursor.executemany(comando_sql, comando)

cursor.execute('select * from partitoteca.genero')
print(' -------------  Formas:  -------------')
for genero in cursor.fetchall():
    print(genero[2])



# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()

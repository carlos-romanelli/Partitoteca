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


###########################
# POPULANDO TABELAS BÁSICAS
###########################

########################################################################
# Inserindo o acervo 1 que serve de base para popular as outras tabelas
########################################################################
'''
acervo_sql = 'INSERT INTO acervo (descricao, telefone, email, sigla, localizacao, publico, dtInclusao)' \
             ' VALUES (%s, %s, %s, %s, %s, %s, %s)'
acervo = [
      ('Acervo Mestre', '(DD)NNNNN-NNNN', 'email_do_usuario@provedor.com', 'ACV-MAS', 'Endereço do acervo', 'N', '2023-07-28')
]

cursor.executemany(acervo_sql, acervo)

cursor.execute('select * from partitoteca.acervo')
print(' -------------  Acervos:  -------------')
for user in cursor.fetchall():
    print(user[1])
'''
########################################################################
# Inserindo os países
########################################################################

comando_sql = 'INSERT INTO pais (nome, sigla3, sigla2)' \
             ' VALUES (%s, %s, %s)'
comando = [

('África do Sul','AFS','ZA'),
('Alemanha','ALE','DE'),
('Angola','ANG','AO'),
('Arábia Saudita','ASA','SA'),
('Argélia','ARG','DZ'),
('Argentina','ARG','AR'),
('Austrália','AUS','AU'),
('Áustria','AUT','AT'),
('Bangladesh','BAN','BD'),
('Bélgica','BEL','BE'),
('Brasil','BRA','BR'),
('Burkina Faso','BKF','BF'),
('Cabo Verde','CAB','CV'),
('Canadá','CAN','CA'),
('Cazaquistão','CAZ','KZ'),
('Chade','CHA','TD'),
('Chile','CHI','CL'),
('China','CHN','CN'),
('Cingapura','CIN','SG'),
('Colômbia','COL','CO'),
('Coreia do Sul','COR','KR'),
('Costa do Marfim','CMA','CI'),
('Dinamarca','DIN','DK'),
('Egito','EGI','EG'),
('Emirados Árabes Unidos','EAU','AE'),
('Espanha','ESP','ES'),
('Estados Unidos da América','EUA','US'),
('Etiópia','ETI','ET'),
('Filipinas','FIL','PH'),
('Finlândia','FIN','FI'),
('França','FRA','FR'),
('Gâmbia','GAM','GM'),
('Gana','GAN','GH'),
('Grécia','GRE','GR'),
('Guiné-Bissau','GBS','GW'),
('Holanda','HOL','NL'),
('Índia','IND','IN'),
('Indonésia','IDN','ID'),
('Irã','IRA','IR'),
('Iraque','IRQ','IQ'),
('Israel','ISR','IL'),
('Itália','ITA','IT'),
('Japão','JPN','JP'),
('Líbia','LIB','LY'),
('Malásia','MAL','MY'),
('Mali','MAL','ML'),
('Marrocos','MAR','MA'),
('Mauritânia','MAT','MR'),
('México','MEX','MX'),
('Moçambique','MOC','MZ'),
('Mongólia','MON','MN'),
('Níger','NIG','NE'),
('Nigéria','NIG','NG'),
('Noruega','NOR','NO'),
('Paquistão','PAQ','PK'),
('Peru','PER','PE'),
('Polônia','POL','PL'),
('Portugal','POR','PT'),
('Quênia','QUE','KE'),
('Reino Unido','RU','GB'),
('República Democrática do Congo','RDC','CD'),
('Rússia','RUS','RU'),
('Saara Ocidental','SO','EH'),
('Senegal','SEN','SN'),
('Seychelles','SEY','SC'),
('Somália','SOM','SO'),
('Sri Lanka','SRI','LK'),
('Sudão','SUD','SD'),
('Suécia','SUE','SE'),
('Suíça','SUI','CH'),
('Tailândia','TAI','TH'),
('Tanzânia','TAN','TZ'),
('Turquia','TUR','TR'),
('Uganda','UGA','UG'),
('Uzbequistão','UZB','UZ'),
('Vietnã','VIE','VN'),
('Zâmbia','ZAM','ZM'),
('Zimbábue','ZIM','ZW'),

]

cursor.executemany(comando_sql, comando)

cursor.execute('select * from partitoteca.pais')
print(' -------------  Países:  -------------')
for user in cursor.fetchall():
    print(user[1])







# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()

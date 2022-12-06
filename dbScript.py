import sqlite3
from datetime import timezone, datetime, timedelta
from random import randint

lista_de_dias = []
for i in range(0,26):
  lista_de_dias.append(datetime.now() + timedelta(days = randint(-60,-5)))


def openDB():
  connection = sqlite3.connect('database.db')
  cur = connection.cursor()  
  return cur,connection


def createSchemaDB(): 
  connection = sqlite3.connect('database.db')
  
  connection.execute('''DROP TABLE IF EXISTS layout;''')
  connection.execute('''CREATE TABLE layout(
  laboratorio_id INTEGER PRIMARY KEY AUTOINCREMENT,
  laboratorio_nome TEXT NOT NULL,
  layout_nome TEXT NOT NULL
);''')
  connection.execute('''DROP TABLE IF EXISTS chamados;''')
  connection.execute('''CREATE TABLE chamados(
  chamado_id INTEGER PRIMARY KEY AUTOINCREMENT,
  micro INTEGER NOT NULL,
  laboratorio TEXT NOT NULL,
  problema TEXT NOT NULL,
  done BOOL,
  created_at DATE
);''')

  connection.execute(''' DROP TABLE IF EXISTS alunos;''')
  connection.execute('''CREATE TABLE alunos(
    aluno_id INTEGER PRIMARY KEY,
    nome text,
    email text,
    chamado_id INTEGER,
    FOREIGN KEY (chamado_id) REFERENCES chamados(chamado_id)

  );''')

def layout():
  cur,conn = openDB()
  cur.execute("INSERT INTO layout(laboratorio_nome,layout_nome) VALUES (?,?)", ('Laboratório 301','4x3')) 
  cur.execute("INSERT INTO layout(laboratorio_nome,layout_nome) VALUES (?,?)", ('Laboratório 302','4x3')) 
  cur.execute("INSERT INTO layout(laboratorio_nome,layout_nome) VALUES (?,?)", ('Laboratório 303','3x3')) 
  cur.execute("INSERT INTO layout(laboratorio_nome,layout_nome) VALUES (?,?)", ('Laboratório 401','4x3')) 
  cur.execute("INSERT INTO layout(laboratorio_nome,layout_nome) VALUES (?,?)", ('Laboratório 402','4x4')) 
  cur.execute("INSERT INTO layout(laboratorio_nome,layout_nome) VALUES (?,?)", ('Laboratório 404','3x3')) 
  cur.execute("INSERT INTO layout(laboratorio_nome,layout_nome) VALUES (?,?)", ('Laboratório 405','3x3')) 
  cur.execute("INSERT INTO layout(laboratorio_nome,layout_nome) VALUES (?,?)", ('Laboratório 406','3x3')) 
  cur.execute("INSERT INTO layout(laboratorio_nome,layout_nome) VALUES (?,?)", ('Laboratório 407','3x3')) 
  cur.execute("INSERT INTO layout(laboratorio_nome,layout_nome) VALUES (?,?)", ('Laboratório 408','3x3')) 
  cur.execute("INSERT INTO layout(laboratorio_nome,layout_nome) VALUES (?,?)", ('Laboratório 409','3x3')) 
  cur.execute("INSERT INTO layout(laboratorio_nome,layout_nome) VALUES (?,?)", ('Laboratório 411','3x3')) 
  cur.execute("INSERT INTO layout(laboratorio_nome,layout_nome) VALUES (?,?)", ('Laboratório 412','3x3')) 
  conn.commit()


def fillDb():
  cur,conn = openDB()
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Michael Morais', 'moraisdpm@outlook.com',1))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Joaquim Portella dos santos', 'joaquim@hotmail.com',2))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Isabella Danes Silva', 'bella@hotmail.com',3))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Barbara junqueira', 'babi@hotmail.com',4))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Samuel santos', 'sam@outlook.com',5))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Sandra Danes', 'sandradpm@outlook.com',6))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Gustavo Silva', 'gugu@gmail.com',7))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Andréia Oliveira', 'andreia30@gmail.com',8))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Marcos Morais', 'marcoan@gmail.com',9))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Ian Porto', 'ianporto@gmail.com',10))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Gabriel Santana', 'gabsads@outlook.com',11))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Jean Marques', 'jean@outlook.com',12))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Caique Alberto', 'caique@hotmail.com',13))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Ana Flavia', 'aninha@hotmail.com',14))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Joaquim Souza', 'jo_souza@hotmail.com',15))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Barbara Mariane', 'babi_mari@hotmail.com',16))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Samuel Rosa', 'sam__rosa22@outlook.com',17))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Elon Musk', 'elon@space.com',18))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Gabriel silva', 'silvagabs@gmail.com',19))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Amanda romana', 'romana_manda@gmail.com',20))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Flavia santos', 'santos_Flavia@gmail.com',21))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Bruna carvalho', 'bruna@gmail.com',22))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Paulo Nunes', 'nunespaulo@outlook.com',23))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Marcelino', 'marcel@hotmail.com.com',24))

  
    
  conn.commit()

  # Inserindo Atributos na entidade CHAMADOS
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 402','5','Cabo de rede danificado',datetime.now().strftime('%Y-%m-%d'),))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 401','5','Mouse não funciona',lista_de_dias[0].strftime('%Y-%m-%d'),))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 409','8','Cabo de rede danificado',lista_de_dias[5].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 303','8','Sem internet',lista_de_dias[6].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 401','12','reiniciou sozinho',lista_de_dias[7].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 408','12','monitor não liga',lista_de_dias[8].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 412','2','Sem internet',lista_de_dias[9].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 303','2','PC muito lento',lista_de_dias[10].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 412','5','Sem internet',lista_de_dias[11].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 303','4','PC muito lento',lista_de_dias[12].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 411','1','sem vnc instalado',lista_de_dias[13].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 401','8','monitor não liga',lista_de_dias[14].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 401','12','Mouse não funciona',lista_de_dias[15].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 302','10','Cabo de rede danificado',lista_de_dias[15].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 401','3','monitor não liga',lista_de_dias[16].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 302','1','Mouse não funciona',lista_de_dias[17].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 301','10','Cabo de rede danificado',lista_de_dias[18].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 401','12','mouse com mau contato',lista_de_dias[19].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 301','12','internet não funciona',lista_de_dias[20].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 301','1','sem espaço na memória',lista_de_dias[21].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 302','4','Mouse não funciona',lista_de_dias[22].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 303','10','Cabo de rede danificado',lista_de_dias[23].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 301','12','sem espaço na memória',lista_de_dias[24].strftime('%Y-%m-%d')))
  cur.execute("""INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,?)""", ('Laboratório 303','10','Cabo de rede danificado',lista_de_dias[25].strftime('%Y-%m-%d')))
    
  conn.commit()

  conn.close()

 

createSchemaDB()
layout()
fillDb()

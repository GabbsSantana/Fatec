import sqlite3


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
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Michael', 'moraisdpm@outlook.com',1))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Joaquim', 'joaquim@hotmail.com',2))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Isabella', 'bella@hotmail.com',3))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Barbara', 'babi@hotmail.com',4))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Samuel', 'sam@outlook.com',5))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Sandra', 'sandradpm@outlook.com',6))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Gustavo', 'gugu@gmail.com',7))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Andréia', 'andreia30@gmail.com',8))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Marcos', 'marcoan@gmail.com',9))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Ian', 'ianporto@gmail.com',10))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Gabriel', 'gabsads@outlook.com',11))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Jean', 'jean@outlook.com',12))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Michael', 'moraisdpm@outlook.com',13))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Joaquim', 'joaquim@hotmail.com',14))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Isabella', 'bella@hotmail.com',15))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Barbara', 'babi@hotmail.com',16))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Samuel', 'sam@outlook.com',17))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Sandra', 'sandradpm@outlook.com',18))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Gustavo', 'gugu@gmail.com',19))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Andréia', 'andreia30@gmail.com',20))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Marcos', 'marcoan@gmail.com',21))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Ian', 'ianporto@gmail.com',22))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Gabriel', 'gabsads@outlook.com',23))
  cur.execute("INSERT INTO alunos (nome,email,chamado_id) VALUES(?,?,?)",('Jean', 'jean@outlook.com',24))

  
    
  conn.commit()

  # Inserindo Atributos na entidade CHAMADOS
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 402','5','Cabo de rede danificado',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 401','5','Mouse não funciona',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 409','8','Cabo de rede danificado',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 301','8','Sem internet',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 401','12','reiniciou sozinho',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 408','12','monitor não liga',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 412','2','Sem internet',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 301','2','Cabo de rede danificado',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 412','5','Sem internet',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 301','4','Cabo de rede danificado',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 411','1','sem vnc instalado',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 401','8','monitor não liga',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 401','12','Mouse não funciona',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 301','10','Cabo de rede danificado',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 401','3','monitor não liga',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 301','1','Mouse não funciona',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 301','10','Cabo de rede danificado',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 401','12','mouse com mau contato',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 301','12','internet não funciona',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 301','1','sem espaço na memória',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 302','4','Mouse não funciona',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 303','10','Cabo de rede danificado',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 301','12','sem espaço na memória',))
  cur.execute("INSERT INTO chamados(laboratorio,micro,problema,created_at) VALUES (?,?,?,DATE())", ('Laboratório 303','10','Cabo de rede danificado',))
    
  conn.commit()

  conn.close()

 

createSchemaDB()
layout()
fillDb()

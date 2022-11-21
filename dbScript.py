import sqlite3

def openDB():
  connection = sqlite3.connect('database.db')
  cur = connection.cursor()  
  return cur,connection


def createSchemaDB(): 
  connection = sqlite3.connect('database.db')
  connection.execute(''' DROP TABLE IF EXISTS alunos;''')
  connection.execute('''CREATE TABLE alunos (
  aluno_id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  email TEXT NOT NULL);''')
  connection.execute('''DROP TABLE IF EXISTS layout;''')
  connection.execute('''CREATE TABLE layout(
  laboratorio_id INTEGER PRIMARY KEY AUTOINCREMENT,
  laboratorio_nome TEXT NOT NULL,
  layout_nome TEXT NOT NULL
);''')
  connection.execute('''DROP TABLE IF EXISTS chamados;''')
  connection.execute('''CREATE TABLE chamados(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  micro INTEGER NOT NULL,
  laboratorio TEXT NOT NULL,
  problema TEXT NOT NULL
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




createSchemaDB()
layout()

from flask import Flask,render_template,request,flash,redirect,url_for
import sqlite3

connection = sqlite3.connect('database.db',check_same_thread=False)

with open('schema.sql') as f:
  connection.executescript(f.read())

def openDB():
  connection = sqlite3.connect('database.db')
  cur = connection.cursor()
  return cur,connection


# Inicializando o app FLASK
app = Flask(__name__)

# Criando classe para captura de dados do usuário e criação do chamad
# Número do laboratório, número do micro, Problema relatado
class Chamados: 
    def __init__(self, laboratorio='', micro='', problema=''):
        self.laboratorio = laboratorio
        self.micro = micro
        self.problema = problema

# Classe responsável pela captura de dados do usuário (nome e email)
class alunos:
    def __init__(self, nome='', email=''):
        self.nome = nome
        self.email = email
       
# Inicializando objetos
chamado = Chamados
aluno = alunos
# Inicializando lista 
chamados_abertos = []

# Rota para página home
@app.route('/')
def home():
  return render_template('home.html')

# Rota para página SELECT
# Rota responsável por receber do usuário dados referente ao laboratório
@app.route('/select/',methods=(['GET','POST']))
def select():
  if request.method == 'POST':
    lab = request.form['laboratorios']
    
      
    if not lab:
      flash('Escolha um laboratório')
    else:
      chamado.laboratorio = lab
      cur,conn = openDB()
      cur.execute("INSERT INTO chamados (laboratorio) VALUES(?)",
              (lab,))
      conn.commit()
      cur.execute('SELECT * FROM chamados')
      data = cur.fetchall()
      print(data)
      conn.close()

      return redirect(url_for('layout'))

  return render_template('select.html')
  

# Rota para para página Layout
# Rota responsável por apresentar o layout do laboratório escolhido
# Rota responsável por receber dados referente ao micro e o problema reportado
# Rota responsável por receber nome e email do usuário
@app.route('/layout/',methods=(['GET','POST']))
def layout():
  ## Chamando informação Laboratório xxx do SQLITE
  cur,conn = openDB()
  cur.execute("SELECT laboratorio FROM chamados")
  lab = cur.fetchall()
  if len(lab) > 0:
    lab = lab[-1]
  else:
    lab = lab[0]
    
    

  if request.method == 'POST':
    nome = request.form['nome']
    email = request.form['e-mail']
    micro = request.form['micro']
    problem = request.form['problem']
   
    if not chamado.laboratorio and micro == '':
      flash('Primeiro escolha um laboratório')
      return redirect(url_for('select'))
    else:
      chamado.micro = micro
      chamado.problema = problem
      aluno.nome = nome
      aluno.email = email

      cur,conn = openDB()
      cur.execute("INSERT INTO alunos (nome,email) VALUES(?,?)",
              (nome,email,))
      conn.commit()
      cur.execute('SELECT * FROM alunos')
      data = cur.fetchall()
      print(data)
      conn.close()

      

     

      return redirect(url_for('done'))

  return render_template('layout.html',chamado=chamado,aluno=aluno,chamados_abertos=chamados_abertos,laboratorio=lab)

# Rota para página Done
# Rota responsável por apresentar ao usuário a conclusão do chamado e os dados sobre
@app.route('/done/')
def done(): 
  cur,conn = openDB()
  cur.execute('select nome,email from alunos')
  alunoDB = cur.fetchall()
  if len(alunoDB) > 0:
    alunoDB = alunoDB[-1]
  else:
    alunoDB = alunoDB[0]

   # Pegando dados sobre laboratório  
  cur.execute("SELECT laboratorio FROM chamados")
  lab = cur.fetchall()
  if len(lab) > 0:
    lab = lab[-1]
  else:
    lab = lab[0]
  
  


  return render_template('done.html',chamado=chamado,aluno=alunoDB,
  data=alunoDB,laboratorio=lab)

# Rota para página all
# Rota responsável por apresentar ao usuário todos os chamados abertos no sistema
@app.route('/all/')
def all():
  return render_template('all.html',chamados=chamados_abertos)

app.run(debug=True)

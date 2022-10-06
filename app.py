from flask import Flask,render_template,request,flash,redirect,url_for
import sqlite3

connection = sqlite3.connect('database.db',check_same_thread=False)

with open('schema.sql') as f:
  connection.executescript(f.read())

def openDB():
  connection = sqlite3.connect('database.db')
  cur = connection.cursor()
  return cur,connection

def lab_atual(lab):
  if lab != '':
    laboratorio = lab
    return laboratorio
  else:
    return laboratorio

# Inicializando o app FLASK
app = Flask(__name__)

# Criando classe para captura de dados do usuário e criação do chamad
# Número do laboratório, número do micro, Problema relatado



# Rota para página home
@app.route('/')
def home():
  openDB()
  return render_template('home.html')

# Rota para página SELECT
# Rota responsável por receber do usuário dados referente ao laboratório
@app.route('/select/',methods=(['GET','POST']))
def select():
  openDB()
  if request.method == 'POST':
    lab = request.form['laboratorios']
    lab_atual(lab)

    if not lab:
      flash('Escolha um laboratório')
    else:
      lab_atual(lab)
      return redirect(url_for('layout'))

  return render_template('select.html')
  

# Rota para para página Layout
# Rota responsável por apresentar o layout do laboratório escolhido
# Rota responsável por receber dados referente ao micro e o problema reportado
# Rota responsável por receber nome e email do usuário
@app.route('/layout/',methods=(['GET','POST']))
def layout():  
  if request.method == 'POST':
    nome = request.form['nome']
    email = request.form['e-mail']
    micro = request.form['micro']
    problem = request.form['problem']

    # Inserindo Atributos na entidade ALUNOS
    cur,conn = openDB()
    cur.execute("INSERT INTO alunos (nome,email) VALUES(?,?)",
            (nome,email,))
    conn.commit()
    # Inserindo Atributos na entidade CHAMADOS
    laboratorio = lab_atual('')
    cur.execute("INSERT INTO chamados(laboratorio,micro,problema) VALUES (?,?,?)", (laboratorio,micro,problem,))
    conn.commit()
    return redirect(url_for('done'))

  return render_template('layout.html',laboratorio=laboratorio)

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
  cur.execute("SELECT laboratorio,micro,problema FROM chamados")
  lab = cur.fetchall()
  if len(lab) > 0:
    lab = lab[-1]
  else:
    lab = lab[0]
  
  


  return render_template('done.html', data=alunoDB,laboratorio=lab)

# Rota para página all
# Rota responsável por apresentar ao usuário todos os chamados abertos no sistema
@app.route('/all/')
def all():
  return render_template('all.html')

app.run(debug=True)

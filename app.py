from flask import Flask,render_template,request,flash,redirect,url_for
import sqlite3

connection = sqlite3.connect('database.db')

class LaboratorioAtual:
    def __init__(self, laboratorio=''):
        self.laboratorio = laboratorio

laboratorio_atual = LaboratorioAtual()

# Função responsável por retornar o Cursos e Conector do banco de dados
def openDB():
  connection = sqlite3.connect('database.db')
  cur = connection.cursor()  
  return cur,connection 

# Inicializando variável com os layouts vinculados aos Laboratórios
def layouts():
  cur,conn = openDB()
  cur.execute('select laboratorio_nome,layout_nome from layout')
  layoutLab = cur.fetchall()
  conn.close()
  return layoutLab


# Inicializando o app FLASK
app = Flask(__name__)


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
    if not lab:
      flash('Escolha um laboratório')
    else:
      laboratorio_atual.laboratorio = lab
      return redirect(url_for('layout'))

  return render_template('select.html')
  

# Rota para para página Layout
# Rota responsável por apresentar o layout do laboratório escolhido
# Rota responsável por receber dados referente ao micro e o problema reportado
# Rota responsável por receber nome e email do usuário
@app.route('/layout/',methods=(['GET','POST']))
def layout():  
  layoutLab = layouts()
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
    cur.execute("INSERT INTO chamados(laboratorio,micro,problema) VALUES (?,?,?)", (laboratorio_atual.laboratorio,micro,problem,))
    conn.commit()

    conn.close()
    
    # Redirecionando para página DONE
    return redirect(url_for('done'))

  return render_template('layout.html',laboratorio=laboratorio_atual.laboratorio,layout=layoutLab)

# Rota para página Done
# Rota responsável por apresentar ao usuário a conclusão do chamado e os dados sobre
@app.route('/done/')
def done(): 
  cur,conn = openDB()

  # Pegando dados da Entidade Alunos  
  cur.execute('select nome,email from alunos')
  alunoDB = cur.fetchall()
  if len(alunoDB) > 0:
    alunoDB = alunoDB[-1]
  else:
    alunoDB = alunoDB[0]

   # Pegando dados da Entidade CHAMADOS  
  cur.execute("SELECT laboratorio,micro,problema FROM chamados")
  lab = cur.fetchall()
  if len(lab) > 0:
    lab = lab[-1]
  else:
    lab = lab[0]
  
  conn.close()
  return render_template('done.html', data=alunoDB,laboratorio=lab)

# Rota para Login do administrador
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['login'] != 'admin' or request.form['senha'] != 'admin':
            error = 'Credencial invalida'
        else:
            return redirect(url_for('admin'))
    return render_template('login.html', error=error)



# Rota para página all
# Rota responsável por apresentar ao administrador todos os chamados abertos no sistema
@app.route('/all/')
def all():
  cur,conn = openDB()
  cur.execute('select nome,email from alunos')
  alunoDB = cur.fetchall()
  
   #Pegando dados sobre laboratório  
  cur.execute("SELECT laboratorio,micro,problema FROM chamados")
  lab = cur.fetchall()
  
  conn.close()
  return render_template('all.html',alunos=alunoDB,chamado=lab)


# Rota responsável por editar layout de uma Laboratório
# Disponível apenas para o administrador
@app.route('/update',methods=['GET','POST'])
def update():
  layoutLab = layouts()
  cur,con = openDB()
  if request.method == 'POST':
    lab = request.form['laboratorios']
    imagem = request.form['imagem']
    print(lab,imagem)
    cur.execute('UPDATE layout SET layout_nome = ? WHERE laboratorio_nome == ?',(imagem,lab))
    con.commit()
    con.close()
    return redirect(url_for('admin'))
  
  return render_template('update.html',layout=layoutLab)

# Rota que apresenta o Painel de controle do Administrador
@app.route('/admin')
def admin():
  return render_template('admin.html')
app.run(debug=True)

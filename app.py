from flask import Flask,render_template,request,flash,redirect,url_for

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
    if not chamado.laboratorio and micro == '':
      flash('Primeiro escolha um laboratório')
      return redirect(url_for('select'))
    else:
      chamado.micro = micro
      chamado.problema = problem
      aluno.nome = nome
      aluno.email = email
      chamados_abertos.append(Chamados(laboratorio=chamado.laboratorio,micro=micro,problema=problem))
      return redirect(url_for('done'))

  return render_template('layout.html',chamado=chamado,aluno=aluno,chamados_abertos=chamados_abertos)

# Rota para página Done
# Rota responsável por apresentar ao usuário a conclusão do chamado e os dados sobre
@app.route('/done/')
def done(): 
  chamado.registrado = True
  return render_template('done.html',chamado=chamado,aluno=aluno)

# Rota para página all
# Rota responsável por apresentar ao usuário todos os chamados abertos no sistema
@app.route('/all/')
def all():
  return render_template('all.html',chamados=chamados_abertos)

app.run(debug=True)

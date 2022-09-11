from flask import Flask,render_template,request,flash,redirect,url_for

app = Flask(__name__)


class Chamados:
    def __init__(self, laboratorio, micro='', problema='', registado=False):
        self.laboratorio = laboratorio
        self.micro = micro
        self.problema = problema
        self.registrado = registado

class alunos:
    def __init__(self, nome='', email=''):
        self.nome = nome
        self.email = email
       

chamado = Chamados
aluno = alunos
chamados_abertos = []

@app.route('/')
def home():
  return render_template('home.html')

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
  

@app.route('/layout/',methods=(['GET','POST']))
def layout():
  if request.method == 'POST':
    nome = request.form['nome']
    email = request.form['e-mail']
    micro = request.form['micro']
    problem = request.form['problem']
    if not micro or not problem:
      flash('Escolha um laboratório')
    else:
      chamado.micro = micro
      chamado.problema = problem
      aluno.nome = nome
      aluno.email = email
      return redirect(url_for('done'))

  return render_template('layout.html',chamado=chamado,aluno=aluno,chamados_abertos=chamados_abertos)


@app.route('/done/')
def done(): 
  chamado.registrado = True
  chamados_abertos.append(chamado)
  return render_template('done.html',chamado=chamado,aluno=aluno)


app.run(debug=True)

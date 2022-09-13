from flask import Flask,render_template,request,flash,redirect,url_for

app = Flask(__name__)
  

class Chamados:
    def __init__(self, laboratorio='', micro='', problema=''):
        self.laboratorio = laboratorio
        self.micro = micro
        self.problema = problema

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


@app.route('/done/')
def done(): 
  chamado.registrado = True
  return render_template('done.html',chamado=chamado,aluno=aluno)

@app.route('/all/')
def all():
  return render_template('all.html',chamados=chamados_abertos)

app.run(debug=True)

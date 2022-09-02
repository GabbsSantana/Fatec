from flask import Flask,render_template,request,flash,redirect,url_for

app = Flask(__name__)

chamados = [{'lab':'',
            'micro':'',
            'problem':''}]

chamados_abertos = [{'lab': 0,
            'micro':0,
            'problem':0}]

aluno = [{'Nome':'aluno'},
          {'e-mail':'aluno@fatec.sp.gov.br'}]

chamado = []
micro = []


@app.route('/')
def home():
  return render_template('home.html',chamados=chamados)

@app.route('/select/',methods=(['GET','POST']))
def select():
  if request.method == 'POST':
    lab = request.form['laboratorios']
    if not lab:
      flash('Escolha um laboratório')
    else:
      chamados.append({'lab':lab})
      chamado.append(lab)
      

      return redirect(url_for('layout'))

  return render_template('select.html')
  

@app.route('/layout')
def layout():
  return render_template('layout.html',chamados=chamados,chamado=chamado)

@app.route('/form')
def form():
  return render_template('form.html',chamados=chamados,chamado=chamado,micro=micro)


app.run(debug=True)

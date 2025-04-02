from flask import Flask, render_template, request

app = Flask(__name__)

conteudos = []
diario = []
@app.route('/', methods = ["GET", "POST"])
def principal(): 
    if request.method == 'POST':
        if request.form.get('conteudo'):
            conteudos.append(request.form.get("conteudo"))

    return render_template(
        'index.html',
        conteudos = conteudos
    )

@app.route('/diário')
def diario():
    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get('nota'):
            aluno = request.form.get('aluno')
            nota = request.form.get('nota')
            diario.append(
                {
                    "aluno":aluno,
                    "nota":nota
                }
            )
    return render_template(
        'sobre.html', 
        diario=diario
    )
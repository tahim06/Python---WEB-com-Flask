from flask import Flask, render_template, request

app = Flask(__name__)

conteudos = []
@app.route('/')
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
    diario = {
        "Fulano":5.0,
        "Beltrano":6.0,
        "Teste":7.0,
        "Ciclano":8.5,
        "Rodrigo":9.0,
        "Fernanda":10.0   
    }
    return render_template(
        'sobre.html', 
        diario=diario
    )
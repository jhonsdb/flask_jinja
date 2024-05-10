from  flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def principal():
    return render_template('index.html')

@app.route("/miembros")
def verMimebros():
    equipo=('Jhon','Lourdes','Jesus')
    return render_template('miembros.html', personas=equipo)

@app.route("/actividadJS")
def verejEmplo():
    return render_template('actividad_js.html')

@app.route("/formulario")
def formulario():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)
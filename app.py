from  flask import Flask,render_template 
from flask_sqlalchemy import SQLAlchemy
import sqlite3 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database/tasks.db'
db = SQLAlchemy(app)
#modelo para la tarea
""" class Task(db.model):
    id = db.column(db.integer, primary_key=True)
    content= db.column(db.string(200))
    done = db.column(db.boolean) """


@app.route("/")
def principal():
    return render_template('tasks.html')

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

""" #ruta para recibir los datos, se tiene que acoplar a la que esta??
@app.route('/create-task', methods=['POST'])
def create():
    Task() """

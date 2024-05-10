from  flask import Flask,render_template 
from flask_sqlalchemy import SQLAlchemy
import sqlite3 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database/tasks.db'
db = SQLAlchemy(app)

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



if __name__ == '__main__':
    app.run(debug=True,port=5000)



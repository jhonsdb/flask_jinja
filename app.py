from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS

# inicializar flask
app = Flask(__name__)
CORS(app) #habilitamos cors para todas las rutas.

# asegurarse que exista database
db_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database')
os.makedirs(db_dir, exist_ok=True)

# actualizar la uri de la base de datos a una ruta absoluta.
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(db_dir, "tasks.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicializamos el objeto sqlalchemy
db = SQLAlchemy(app)

# declaramos nuestro modelo task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)

# creamos todas las tablas.
with app.app_context():
    db.create_all()

@app.route("/")
def principal():
    tasks= Task.query.all()
    return render_template('tasks.html', tasks= tasks)

@app.route("/miembros")
def verMimebros():
    equipo = ('Jhon', 'Lourdes', 'Jesus')
    return render_template('miembros.html', personas=equipo)

@app.route("/actividadJS")
def verejEmplo():
    return render_template('actividad_js.html')

@app.route("/formulario")
def formulario():
    return render_template('form.html')

@app.route('/create-task', methods=['POST'])
def create():
    task = Task(content=request.form['content'], done=False)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('principal'))

@app.route('/done/<id>')
def done(id):
    task= Task.query.filter_by(id=int(id)).first()
    task.done= not(task.done)
    db.session.commit()
    return redirect(url_for('principal'))

@app.route('/delete/<id>')
def delete(id):
    task=Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('principal'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
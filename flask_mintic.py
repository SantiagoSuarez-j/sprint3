from flask import Flask
from flask import render_template, url_for,redirect,request

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect(url_for('home'))

# HOME

@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('index.html')
# REGISTRO

@app.route('/registro',methods=['GET','POST'])
def registro():
    return render_template('registro.html')

# MENU

@app.route('/menu',methods=['GET'])
def menu():
    return render_template('menu.html')

@app.route('/menu/busqueda',methods=['GET','POST'])
def busqueda():
    return render_template('busqueda.html')

@app.route('/menu/lista_deseos',methods=['GET','POST','PUT'])
def lista_deseos():
    return 'lista_deseos'

@app.route('/menu/platos',methods=['GET','POST'])
def platos():
    return 'platos'

@app.route('/menu/pedidos',methods=['GET','POST','PUT'])
def pedidos():
    return 'pedidos'

@app.route('/menu/busqueda/resultados',methods=['GET'])
def resultados():
    return 'resultados'

@app.route('/menu/busqueda/detalle_platos',methods=['GET'])
def detalle_platos():
    return 'detalle_platos'

# LOGIN

@app.route('/login',methods=['GET','POST'])
def login():

    return render_template('login.html')

# NOSOTROS

@app.route('/nosotros',methods=['GET'])
def nosotros():
    return 'Nosotros'




if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "llave super duper secreta" #Establecemos una llave secreta para dar más seguridad a los datos almacenados en sesión

#Ruta para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')

#Necesitamos una ruta que vincule con action
@app.route('/proceso', methods=['POST']) #La accion del formulario, aquí vamos a procesar lo que recibamos del form
def proceso():
    print(request.form)

    #Guardamos en sesión
    session['nombre'] = request.form['nombre']
    session['apellido'] = request.form['apellido']
    session['email'] = request.form['email']
    session['tipo_usuario'] = request.form['tipo_usuario']

    return redirect('/exito') #Redirección nos lleva a la nueva URL

@app.route('/exito')
def exito():
    return render_template('exito.html')

if __name__== "__main__":
    app.run(debug=True)
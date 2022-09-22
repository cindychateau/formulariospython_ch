from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#Ruta para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')

#Necesitamos una ruta que vincule con action
@app.route('/proceso', methods=['POST']) #La accion del formulario, aquí vamos a procesar lo que recibamos del form
def proceso():
    print(request.form)
    return redirect('/exito') #Redirección nos lleva a la nueva URL

@app.route('/exito')
def exito():
    return render_template('exito.html')

if __name__== "__main__":
    app.run(debug=True)
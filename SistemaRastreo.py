# Nombre: Jhostyn Javier Gavilanez Suarez

# importar la libreria flask
# En este apartado se añade la libreria de flask, entre otras para hacer el llamado y otras funcionalidades de la pagina del sistema de control.
from flask import Flask, render_template, redirect, request, url_for

# ---------------------------------------------------------------------------
# Se inicializa y se llama a la carpeta 
app = Flask(__name__, template_folder='templates')

# ---------------------------------------------------------------------------
# Este es el arreglo para almacenar las tareas en forma de lista.
RegistrosCliente = []  # arreglo de la lista
# ---------------------------------------------------------------------------
# Password para tener acceso a dicha aplicacion mediante el uso del secret key
app.secret_key = 'jhostyn2022'

# ---------------------------------------------------------------------------
# Este es el primer paso ver las listas de las tareas pendientes
# Esta es la ruta raiz donde esta nuestro html controlador  raiz
# este es el controlador donde me permite ingresar los registros del cliente 
@app.route('/')
# llamar a index.html en la ruta principal
def panelPrincipal():
    return render_template('/Principal', RegistrosCliente=RegistrosCliente)

# ---------------------------------------------------------------------------
# Este es el segundo paso para enviar datos a nuestra lista mediante el formulario dado.
# Controlador de envio.


@app.route('/enviar', methods=['POST'])
# metodo de guardar los datos
def enviar():  # Aqui realiza el envio de datos para ser guardados en la lista.
    if request.method == 'POST':
        # el mensaje de añadir un registro de un nuevo dato se muestra por codigo javascript en el html
        Registro_Nombre = request.form['Registro_Nombre']
        Registro_Telefono = request.form['Registro_Telefono']
        Registro_Estado = request.form['Registro_Estado']

        # El mensaje esta por codigo javascript dentro del HTML
        if Registro_Nombre == '' or Registro_Telefono == '' or Registro_Estado == '':
            return redirect(url_for('panelPrincipal'))
        else:
            RegistrosCliente.append(
                {'Registro_Nombre': Registro_Nombre,
                 'Registro_Telefono': Registro_Telefono,
                 'Registro_Estado': Registro_Estado})

            return redirect(url_for('panelPrincipal'))


# ---------------------------------------------------------------------------
# Controlador de la ruta para borrar todos los datos encontrados del registro 
# Controlador de borrar registros
@app.route('/borrar', methods=['POST'])
def borrar():              # La funcion de envio de mensaje borrado se hace mediante codigo Javascript
    RegistrosCliente.clear()
    return redirect(url_for('panelPrincipal'))


# ---------------------------------------------------------------------------
# Controlador de registrar los de la tienda 


# ejecutar del main principal de la pagina To DO local host
if __name__ == '__main__':

    app.run(debug=True)
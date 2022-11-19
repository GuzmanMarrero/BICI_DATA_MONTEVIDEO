from flask import Flask, request, redirect, url_for
from flask import render_template

from PROYECTO_BICI_DATA_MONTEVIDEO.web.servicios import autenticacion

app = Flask(__name__)

###################################[X]
#01_ingresar_al_index:
@app.route('/')
def index():
    return redirect(url_for('login'))

#####################################[XO]  { tiene el error de : no restringir el acceso de los usuarios no registrados y no dar mensajes de error }
#02_ingresar_identificandose_al_login:
@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        if not autenticacion.validar_credenciales(request.form['usu_nombre'], request.form['usu_contra']):
            error = ['Credenciales inválidas']
        else:
            return redirect( url_for( 'inicio' ) )
    return render_template( 'login.html' , error=error )

####################################[XO]     { tiene el error de : poder crear un usuarios sin  completar el formulario y no avisar lo que falta completar en el formulario }
#03_registrarse_como_usuario:
@app.route('/registro', methods=['GET', 'POST'])
def registro_usuario():
    error = None
    if request.method == 'POST':
        if not  autenticacion.crear_usuario(request.form['usu_fecha'],request.form['usu_correo'],request.form['usu_nombre'], request.form['usu_contra']):
            error = ['No se pudo crear el usuario']
        else:
            return redirect(url_for('inicio'))
    return render_template('registro.html', error=error)

###################################[X]
#04_ ruta de inicio (opcion: se_puede_mostrar_todos_los_usuarios_registrados_en_una_lista_en_el_inicio):
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

#def mostrar_usuarios():

#    usuarios = autenticacion.obtener_usuarios()
#    return render_template( 'inicio.html' , usuarios=usuarios )


####################################################################################################
####################################[XO]{registra la sugerencia pero no registra el sug_usu_id_pk}
#05_registrar_sugerencia:

@app.route('/sugerencia', methods=['POST'])
def registro_sugerencia():
    error=None
    if request.method == 'POST':
        if not autenticacion.crear_sugerencia(request.form['sug_fecha'],request.form['sug_texto'],request.form['sug_link']):
            error=['No se pudo crear la sugerencia']
        else:
            return redirect(url_for('registro_sugerencia'))
    return render_template('sugerencias.html', error=error)



######################################[X] {...}
#06_mostrar_la_lista_de_las_sugerencias_en_el_sitio_sugerencias:
@app.route('/sugerencia',methods=['GET'])
def mostrar_sugerencia_():
    request.method=='GET'
    headings=["__Fecha__","_________________Texto__________________","__Link__"]
    data=autenticacion.obtener_sugerencias_()
    return render_template('sugerencias.html',headings=headings,data=data)


#################################################################
if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)

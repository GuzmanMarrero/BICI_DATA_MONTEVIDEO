from flask import Flask , request , jsonify
from PROYECTO_BICI_DATA_MONTEVIDEO.servicios.autenticacion import autenticacion
from flask import render_template

app= Flask(__name__)
################################################################################
############################################### [X]
#01_crear_usuario:

@app.route('/usuario',methods=['POST'])
def crear_usuario():
    datos_usuario = request.get_json()
    if 'usu_fecha'not  in datos_usuario:
        return 'El usu_fecha es requerido',412
    if 'usu_correo'not  in datos_usuario:
        return 'El usu_correo es requerido',412
    if 'usu_nombre'not  in datos_usuario:
        return 'El usu_nombre es requerido',412
    if 'usu_contra'not  in datos_usuario:
        return 'El usu_contra es requerido',412
    autenticacion.crear_usuario(datos_usuario['usu_fecha'],datos_usuario['usu_correo'],datos_usuario['usu_nombre'], datos_usuario['usu_contra'])
    return 'OK', 200

############################################### [X]
#02_modificar_usuario:
@app.route('/usuario/<usu_id_pk>',methods=['PUT'])
def modificar_usuario(usu_id_pk):
    datos_usuario = request.get_json()
    if'usu_fecha' not in datos_usuario:
        return 'La fecha es requerida', 412
    if 'usu_correo' not in datos_usuario:
        return ' El correo es requerido', 412
    if 'usu_nombre' not in datos_usuario:
        return 'El nombre es requerido',412
    if 'usu_contra' not in datos_usuario:
        return 'La clave es requerida',412
    autenticacion.modificar_usuario(usu_id_pk, datos_usuario)
    return'Ok',200
##########################[X]
#03_borrar_usuario:
@app.route('/usuario/<usu_id_pk>', methods=['DELETE'])
def borrar_usuario(usu_id_pk):
    autenticacion.borrar_usuario(usu_id_pk)
    return "Usuario Borrado", 200

##########################[X]
#04_obtener_usuario:
@app.route('/usuario/<usu_id_pk>', methods=['GET'])
def obtener_usuario(usu_id_pk):
    try:
        usuario = autenticacion.obtener_usuario(usu_id_pk)
        return jsonify(usuario)
    except Exception:
        return 'Usuario no encontrado',404


############################[X]
#05_obtener_usuarios:
@app.route('/usuario/all', methods=['GET'])
def obtener_usuarios():
    return jsonify(autenticacion.obtener_usuarios())

###############################[X]
#06_login():
@app.route('/login', methods=['POST'])
def login():
    datos_usuario =request.get_json()
    if'usu_nombre'not in datos_usuario:
        return'El nombre de usuario es requerido',412
    if'usu_contra' not in datos_usuario:
        return 'La clave es requerida', 412
    id_sesion=autenticacion.login( datos_usuario['usu_nombre'] , datos_usuario['usu_contra'] )
    return jsonify({"id_sesion":id_sesion})

###############################[ ]
#06.5_consulta de validar sesion():

###############################[X]
#07_index():
@app.route('/')
def get_index():
    titulo_bici_data_montevideo = ' Bici Data Montevideo'
    return render_template('index.html', titulo=titulo_bici_data_montevideo)

################################################################################
############################################### [X]
#08_crear_sugerencia:

@app.route('/sugerencia',methods=['POST'])
def crear_sugerencia():
    datos_sugerencia = request.get_json()
    if 'sug_fecha'not  in datos_sugerencia:
        return 'El sug_fecha es requerido',412
    if 'sug_texto'not  in datos_sugerencia:
        return 'El texto es requerido',412
    if 'sug_link'not  in datos_sugerencia:
        return 'El link es requerido',412
    autenticacion.crear_sugerencia(datos_sugerencia['sug_fecha'],datos_sugerencia['sug_texto'], datos_sugerencia['sug_link'])
    return 'OK', 200

############################################### [X]
#09_modificar_sugerencia:
@app.route('/sugerencia/<sug_id_pk>',methods=['PUT'])
def modificar_sugerencia(sug_id_pk):
    datos_sugerencia = request.get_json()
    if'sug_texto' not in datos_sugerencia:
        return 'El texto es requerida', 412
    if 'sug_link' not in datos_sugerencia:
        return ' El Link es requerido', 412
    autenticacion.modificar_sugerencia(sug_id_pk, datos_sugerencia)
    return'Ok',200
##########################[X]
#10_borrar_sugerencia:
@app.route('/sugerencia/<sug_id_pk>', methods=['DELETE'])
def borrar_sugerencia(sug_id_pk):
    autenticacion.borrar_sugerencia(sug_id_pk)
    return "Sugerencia Borrada", 200

##########################[X]
#11_obtener_sugerencia_por_id:
@app.route('/sugerencia/<sug_id_pk>', methods=['GET'])
def obtener_sugerencia(sug_id_pk):
    sugerencia = autenticacion.obtener_sugerencia( sug_id_pk )
    return jsonify(sugerencia)
#    try:
#        sugerencia = autenticacion.obtener_sugerencia(sug_id_pk)
#        return jsonify(sugerencia)
#    except Exception:
#        return 'sugerencia no encontrada',404


############################[X]
#12_obtener_sugerencias:
@app.route('/sugerencia/all', methods=['GET'])
def obtener_sugerencias():
    return jsonify(autenticacion.obtener_sugerencias())

##########################[X] { me manda un error de sugerencia no encontrada aunque no aplique un try }
#13_obtener_sugerencia_por_fecha:
@app.route('/sugerencia/fecha/<sug_fecha>', methods=['GET'])
def obtener_sugerencia_fecha(sug_fecha):
        sugerencia_fecha = autenticacion.obtener_sugerencia_fecha(sug_fecha)
        return jsonify(sugerencia_fecha)

############################[X]
#14_obtener_sugerencias_sin_mostrar_ID:
@app.route('/sugerencia/all_', methods=['GET'])
def obtener_sugerencias_():
    return jsonify(autenticacion.obtener_sugerencias_())

###############################################################
if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
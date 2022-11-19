from PROYECTO_BICI_DATA_MONTEVIDEO.datos.modelos import usuario as modelo_usuario
from PROYECTO_BICI_DATA_MONTEVIDEO.datos.modelos import sugerencia as modelo_sugerencia
from datetime import datetime

############################[X]
#01_autenticacion_crear_usuario:
def crear_usuario(usu_fecha , usu_correo , usu_nombre , usu_contra):
    modelo_usuario.crear_usuario(usu_fecha , usu_correo , usu_nombre , usu_contra)


############################[X]
#02_autenticacion_modificar_usuario:
def modificar_usuario(usu_id_pk,datos_usuario):
    modelo_usuario.modificar_usuario(usu_id_pk, datos_usuario)

############################[X]
#03_autenticacion_borrar_usuario:
def borrar_usuario(usu_id_pk):
    modelo_usuario.borrar_usuario(usu_id_pk)

############################[X]
#04_autenticacion_obtener_usuario:
def obtener_usuario(usu_id_pk):
    usuarios = modelo_usuario.obtener_usuario(usu_id_pk)
    if len (usuarios) == 0:
        raise Exception ("El usuario no existe")
    return usuarios[0]


###########################[X]
#05_autenticacion_obtener_usuarios:
def obtener_usuarios():
    return modelo_usuario.obtener_usuarios()

#######################################
############################[X]
#Autenticaciones_para_el_login:

############################[X]
#A)06_Autenticacion_login:
def login(usu_nombre,usu_contra):
    if _existe_usuario(usu_nombre,usu_contra):
        usuario =modelo_usuario.obtener_usuario_por_nombre_clave(usu_nombre,usu_contra)[0]
        return _crear_sesion(usuario['usu_id_pk'])

############################[X]
#B)07_Autenticacion__existe_usuario:
def _existe_usuario(usu_nombre,usu_contra):
    usuario=modelo_usuario.obtener_usuario_por_nombre_clave(usu_nombre,usu_contra)
    return not len (usuario)==0

############################[X]
#C)08_Autenticacion__crear_sesion:
def _crear_sesion(ses_usuario):
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return modelo_usuario.crear_sesion(ses_usuario, dt_string)

############################[ ]
#09_Autenticacion_validar_sesion:
def validar_sesion(ses_id_pk):
    sesiones = modelo_usuario.obtener_sesion(ses_id_pk)
    if len(sesiones) == 0:
        return False
    elif (datetime.now() - datetime.strptime(sesiones[0]['ses_fecha'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 60:
        # Sesion expirada
        return False
    else:
        return True
###############################################################



############################[X]
#10_autenticacion_crear_sugerencia:
def crear_sugerencia(sug_fecha , sug_texto , sug_link ):
    modelo_sugerencia.crear_sugerencia(sug_fecha , sug_texto , sug_link )


############################[X]
#11_autenticacion_modificar_sugerencia:
def modificar_sugerencia(sug_id_pk,datos_sugerencia):
    modelo_sugerencia.modificar_sugerencia(sug_id_pk, datos_sugerencia)

############################[X]
#12_autenticacion_borrar_sugerencia:
def borrar_sugerencia(sug_id_pk):
    modelo_sugerencia.borrar_sugerencia(sug_id_pk)

############################[X]
#13_autenticacion_obtener_sugerencia:
def obtener_sugerencia(sug_id_pk):
    sugerencias = modelo_sugerencia.obtener_sugerencia(sug_id_pk)
    return sugerencias[0]

###########################[X]
#14_autenticacion_obtener_sugerencias:
def obtener_sugerencias():
    return modelo_sugerencia.obtener_sugerencias()

###########################[ ]
#15_autenticacion_obtener_sugerencias_fecha:
def obtener_sugerencia_fecha(sug_fecha):
    sugerencias_fecha = modelo_sugerencia.obtener_sugerencia_fecha(sug_fecha)
    return sugerencias_fecha[0]

###########################[X]
#16_autenticacion_obtener_sugerencias:
def obtener_sugerencias_():
    return modelo_sugerencia.obtener_sugerencias_()

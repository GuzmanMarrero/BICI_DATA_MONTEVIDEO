import requests

from PROYECTO_BICI_DATA_MONTEVIDEO.web.servicios import rest_api

###########################################[X]
#01_autenticacion_validar_credenciales:
def validar_credenciales(usu_nombre, usu_contra):
    body = {"usu_nombre": usu_nombre,
            "usu_contra": usu_contra}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    # Solo verificamos el codigo de la respuesta en este caso
    return respuesta.status_code==200

###########################################[X]
#02_autenticacion_crear_usuario:
def crear_usuario(usu_fecha,usu_correo,usu_nombre, usu_contra):
    body = {"usu_fecha":usu_fecha,
            "usu_correo":usu_correo,
            "usu_nombre": usu_nombre,
            "usu_contra": usu_contra}
    respuesta = requests.post(f'{rest_api.API_URL}/usuario', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200

###########################################[X]
#03_autenticacion_obtener_usuarios:
def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/usuario/all')
    return respuesta.json()


#########################################################################
#################################################### [XO]
#04_autenticacion_crear_sugerencia
def crear_sugerencia(sug_fecha,sug_texto,sug_link):
    body = {"sug_fecha":sug_fecha,
            "sug_texto":sug_texto,
            "sug_link": sug_link}
    respuesta = requests.post(f'{rest_api.API_URL}/sugerencia', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    return respuesta.status_code == 200

####################################################### [X]
#05_autenticacion_obtener_sugerencias
def obtener_sugerencias():
    respuesta_suregerencias = requests.get(f'{rest_api.API_URL}/sugerencia/all')
    return respuesta_suregerencias.json()

####################################################### [ ]
#06_autenticacion_obtener_sugerencias
def obtener_sugerencias_():
    respuesta_suregerencias_ = requests.get(f'{rest_api.API_URL}/sugerencia/all_')
    return respuesta_suregerencias_.json()

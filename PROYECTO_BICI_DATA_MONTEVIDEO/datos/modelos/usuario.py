from PROYECTO_BICI_DATA_MONTEVIDEO.datos.base_de_datos import BaseDeDatos


###########################[X]
# 01_funcion_crear_usuario:

def crear_usuario(usu_fecha , usu_correo , usu_nombre , usu_contra):
    crear_usuario_sql = f"""
        INSERT INTO USUARIO(USU_FECHA,USU_CORREO,USU_NOMBRE, USU_CONTRA)  
        VALUES('{usu_fecha}','{usu_correo}','{usu_nombre}','{usu_contra}')"""

    bd = BaseDeDatos()
    bd.ejecutar_sql( crear_usuario_sql )


######################### [X]
# 02_funcion_modificar_usuario:

def modificar_usuario(usu_id_pk , datos_usuario):
    modificar_usuario_sql = f"""
    UPDATE USUARIO
    SET USU_FECHA='{datos_usuario["usu_fecha"]}',USU_CORREO='{datos_usuario["usu_correo"]}',
    USU_NOMBRE='{datos_usuario["usu_nombre"]}',USU_CONTRA='{datos_usuario["usu_contra"]}'
    WHERE USU_ID_PK='{usu_id_pk}'"""

    bd = BaseDeDatos()
    bd.ejecutar_sql( modificar_usuario_sql )


########################[X]
# 03_funcion_borrar_usuario:

def borrar_usuario(usu_id_pk):
    obtener_usuario_sql = f"""
    DELETE
    FROM USUARIO
    WHERE USU_ID_PK ='{usu_id_pk}'"""

    bd = BaseDeDatos()
    bd.ejecutar_sql( obtener_usuario_sql )

#######################[X]
# 04_funcion_obtener_usuario:
def obtener_usuario(usu_id_pk):
    obtener_usuarios_sql = f"""
    SELECT usu_id_pk,usu_fecha,usu_correo,usu_nombre,usu_contra
    FROM USUARIO
    WHERE USU_ID_PK= '{usu_id_pk}'"""

    bd = BaseDeDatos()
    return [{"usu_id_pk": registro[0] ,
             "usu_fecha": registro[1] ,
             "usu_correo": registro[2] ,
             "usu_nombre": registro[3] ,
             "usu_contra": registro[4]}
            for registro in bd.ejecutar_sql( obtener_usuarios_sql )]

##########################################[X]
#funcion_05_obtener_usuarios:

def obtener_usuarios():
    obtener_usuarios_sql = f"""
    SELECT usu_id_pk,usu_fecha,usu_correo,usu_nombre,usu_contra
    FROM USUARIO
    """
    bd=BaseDeDatos()
    return [{"usu_id_pk":registro[0],
             "usu_fecha":registro[1],
             "usu_correo":registro[2],
             "usu_nombre":registro[3],
             "usu_contra":registro[4]}
            for registro in bd.ejecutar_sql(obtener_usuarios_sql)]



################################[X]
#funciones_para el login:

################################[X]
#A)Funcion_07_obtener_usuario_por_nombre_clave:
def obtener_usuario_por_nombre_clave(usu_nombre , usu_contra):
    obtener_usuario_sql = f"""
            SELECT usu_id_pk, usu_nombre
            FROM USUARIO 
            WHERE USU_NOMBRE='{usu_nombre}' and USU_CONTRA='{usu_contra}'"""
    bd = BaseDeDatos()
    return [{"usu_id_pk": registro[0],"usu_nombre":registro[1]}
            for registro in bd.ejecutar_sql( obtener_usuario_sql )]


################################[X]
#B)Funcion_08_Crear_sesion:
def crear_sesion(ses_usuario,dt_string):
    crear_sesion_sql = f"""
    INSERT INTO SESIONES(SES_USUARIO,SES_FECHA) 
    VALUES('{ses_usuario}','{dt_string}')"""
    bd=BaseDeDatos()
    return bd.ejecutar_sql(crear_sesion_sql , True)

################################[X]
#Funcion_09_obtener_sesion:
def obtener_sesion(ses_usuario):
    obtener_sesion_sql=f"""
    SELECT SES_USUARIO,SES_FECHA 
    FROM SESIONES 
    WHERE SES_ID_PK={ses_usuario}"""
    bd =BaseDeDatos()
    return[{"ses_id_pk":registro[0],
            "ses_usuario":registro[1],
            "ses_fecha":registro[2]}
           for registro in bd.ejecutar_sql(obtener_sesion_sql)]
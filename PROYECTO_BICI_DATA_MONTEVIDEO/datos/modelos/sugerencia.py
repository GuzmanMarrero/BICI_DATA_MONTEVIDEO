from PROYECTO_BICI_DATA_MONTEVIDEO.datos.base_de_datos import BaseDeDatos


###########################[X]  { falta encontrar el modo de que el usuario que este creando la sugerencia registre automaticamente su sug_usu_id_pk }
# 01_funcion_crear_sugerencia:

def crear_sugerencia(sug_fecha , sug_texto , sug_link ):
    crear_sugerencia_sql = f"""
        INSERT INTO SUGERENCIAS(SUG_FECHA,SUG_TEXTO ,SUG_LINK)  
        VALUES('{sug_fecha}','{sug_texto}','{sug_link}')"""

    bd = BaseDeDatos()
    bd.ejecutar_sql( crear_sugerencia_sql )


######################### [X]
# 02_funcion_modificar_sugerencia:

def modificar_sugerencia(sug_id_pk , datos_sugerencia):
    modificar_sugerencia_sql = f"""
    UPDATE SUGERENCIAS
    SET SUG_TEXTO ='{datos_sugerencia["sug_texto"]}',SUG_LINK='{datos_sugerencia["sug_link"]}'
    WHERE SUG_ID_PK='{sug_id_pk}'"""

    bd = BaseDeDatos()
    bd.ejecutar_sql( modificar_sugerencia_sql )


########################[X]
# 03_funcion_borrar_sugerencia:

def borrar_sugerencia(sug_id_pk):
    obtener_sugerencia_sql = f"""
    DELETE
    FROM SUGERENCIAS
    WHERE SUG_ID_PK ='{sug_id_pk}'"""

    bd = BaseDeDatos()
    bd.ejecutar_sql( obtener_sugerencia_sql )

#######################[X]
# 04_funcion_obtener_sugerencia:
def obtener_sugerencia(sug_id_pk):
    obtener_sugerencia_sql = f"""
    SELECT sug_id_pk,sug_fecha,sug_texto,sug_link
    FROM SUGERENCIAS
    WHERE SUG_ID_PK='{sug_id_pk}'"""

    bd = BaseDeDatos()
    return [{"sug_id_pk": registro[0] ,
             "sug_fecha": registro[1] ,
             "sug_texto": registro[2] ,
             "sug_link": registro[3]}
            for registro in bd.ejecutar_sql( obtener_sugerencia_sql )]

##########################################[X]
#05_obtener_sugerencias:

def obtener_sugerencias():
    obtener_sugerencias_sql = f"""
    SELECT sug_id_pk,sug_fecha,sug_texto,sug_link
    FROM SUGERENCIAS
    """
    bd=BaseDeDatos()
    return [{"1ID":registro[0],
             "2Fecha":registro[1],
             "3Texto":registro[2],
             "4Link":registro[3]}
            for registro in bd.ejecutar_sql(obtener_sugerencias_sql)]

#######################[X]
# 06_funcion_obtener_sugerencia:
def obtener_sugerencia_fecha(sug_fecha):
    obtener_sugerencia_fecha_sql = f"""
    SELECT sug_fecha,sug_texto,sug_link
    FROM SUGERENCIAS
    WHERE SUG_FECHA='{sug_fecha}'"""

    bd = BaseDeDatos()
    return [{"sug_fecha": registro[0] ,
             "sug_texto": registro[1] ,
             "sug_link": registro[2]}
            for registro in bd.ejecutar_sql( obtener_sugerencia_fecha_sql )]

#######################[X]
# 07_funcion_obtener_sugerencia_sin_mostrar_el_ID:
def obtener_sugerencias_():
    obtener_sugerencias_sql_ = f"""
    SELECT sug_fecha,sug_texto,sug_link
    FROM SUGERENCIAS
    """
    bd=BaseDeDatos()
    return [{"_":registro[0],
             "__":registro[1],
             "___":registro[2]}
            for registro in bd.ejecutar_sql(obtener_sugerencias_sql_)]

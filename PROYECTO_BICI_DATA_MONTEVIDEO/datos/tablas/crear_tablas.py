import sqlite3

# 1.1 tabla : usuario

sqlite_tabla_usuario = '''
CREATE TABLE  USUARIO(
USU_ID_PK INTEGER PRIMARY KEY,
USU_FECHA INTEGER,
USU_CORREO STRING, 
USU_NOMBRE STRING, 
USU_CONTRA STRING
)
'''

# 1.2 tabla : rutas

sqlite_tabla_rutas = '''
CREATE TABLE  RUTAS(
RUTA_ID_PK INTEGER PRIMARY KEY,
RUTA_FECHA INTEGER,
RUTA_COOR TEXT,
RUTA_ID_USU_FK INTEGER, 
FOREIGN KEY(RUTA_ID_USU_FK) REFERENCES USUARIO(USU_ID_PK)
)
'''

# 1.3 tabla : comentarios

sqlite_tabla_comentarios = '''
CREATE TABLE  COMENTARIOS(
COM_ID_PK INTEGER PRIMARY KEY,
COM_FECHA INTEGER,
COM_COOR TEXT, 
COM_TEXTO TEXT,
COM_ID_USU_FK INTEGER,
FOREIGN KEY(COM_ID_USU_FK) REFERENCES USUARIO(USU_ID_PK)
)
'''

# 1.4 tabla : carteles

sqlite_tabla_carteles = '''
CREATE TABLE  CARTELES(
CAR_ID_PK INTEGER PRIMARY KEY, 
CAR_FECHA INTEGER,
CAR_COOR TEXT,
CAR_TEXTO TEXT, 
CAR_BLOB BLOB, 
CAR_ID_USU_FK INTEGER,
FOREIGN KEY(CAR_ID_USU_FK) REFERENCES USUARIO(USU_ID_PK)
)
'''

# 1.5 tabla : sugerencias

sqlite_tabla_sugerencias = '''
CREATE TABLE  SUGERENCIAS(
SUG_ID_PK INTEGER PRIMARY KEY, 
SUG_FECHA INTEGER, 
SUG_TEXTO TEXT, 
SUG_LINK STRING,
SUG_ID_USU_FK INTEGER, 
FOREIGN KEY(SUG_ID_USU_FK) REFERENCES USUARIO(USU_ID_PK)
)
'''
#1.6 tabla_sesion:
sqlite_tabla_sesiones = '''
CREATE TABLE SESIONES(
SES_ID_PK INTEGER PRIMARY KEY,
SES_USUARIO TEXT,
SES_FECHA TEXT,
FOREIGN KEY (SES_USUARIO) REFERENCES USUARIO(USU_ID_PK)
)'''


if __name__ == '__main__':
    try:
        print( 'Creando Base de datos...' )
        conexion = sqlite3.connect( '../../BICI_DATA_MONTEVIDEO.db' )

        print( 'Creando Tablas...' )
        conexion.execute( sqlite_tabla_usuario )
        #conexion.execute( sqlite_tabla_rutas )
        #conexion.execute( sqlite_tabla_comentarios )
        #conexion.execute( sqlite_tabla_carteles )
        conexion.execute( sqlite_tabla_sugerencias )
        conexion.execute( sqlite_tabla_sesiones)

        conexion.close()
        print( 'Creacion Finalizada.' )
    except Exception as e:
        print( f'Error Creando base de datos: {e}' , e )

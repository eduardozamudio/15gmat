# # Conexión a base de datos PostgreSQL

# Esta libreta establece un ejemplo de conexión a una base de datos PostgreSQL utilizando variables de ambiente

# La correcta ejecución de esta libreta incluye los siguientes elementos:
# * existe un archivo `.env` con las variables de ambiente de la conexión en la misma ubicación que la libreta
# * se dispone de una instancia de servicio PostgreSQL con la base de datos `universidad`



# 1. Conexión a la base de datos

# Inicialmente se requiere establecer la conexión con la base de datos. 
# Primero se realizan los imports de los módulos requeridos para la tarea

from dotenv import load_dotenv
import sys, os
import numpy as np
import pandas as pd
import pandas.io.sql as psql

# Importa el conector de la base de datos PostgreSQL
from psycopg2 import connect

# Importa la gestión de errores del conector
from psycopg2 import OperationalError


# Carga las variables de ambiente del archivo .env
print("Cargando variables de entorno")
load_dotenv()

PGHOST = os.getenv('PGHOST')
PGPORT = os.getenv('PGPORT')
PGDATABASE= os.getenv('PGDATABASE')
PGUSER = os.getenv('PGUSER') 
PGPASSWORD = os.getenv('PGPASSWORD')


print("1. Estableciendo conexión con la base de datos")
# Establece la conexión con la base de datos
try:
    conn = connect(
                    host = PGHOST,
                    user = PGUSER,
                    dbname = PGDATABASE,
                    password = PGPASSWORD,
                    port = PGPORT)
    
    print('Conectado!')
except OperationalError as err:
    print('Error en la conexión: '+ err)
    
    conn = None



# 2. Obtiene las filas de la tabla estudiante

# Crea el cursor de la conexión y establece la consulta a la tabla estudiantes
print("\n2. Generando la consulta con la base de datos")

cur = conn.cursor()

cur.execute("SELECT id_estudiante, nombre, numero_telefono \
            FROM estudiante;")


# Obtiene las filas resultantes de la consulta
print(cur.fetchmany(size=10))


# Obtiene la cantidad de filas afectadas
print("Cantidad de filas: {0}".format(cur.rowcount))



# 3. Inserta un registro en la tabla estudiante y vuelve a consultar las filas de la tabla estudiante

#Crea el cursor
curInsert = conn.cursor() 

# Establece los valores de los datos a insertar
idEstudiante = "123456"
nombreEstudiante = "María"
numeroTelefono = "+549 9876 123456"

# Ejecuta la acción de inserción con los datos como parámetros de la consulta
print("\n3. Insertando registro en la base de datos: ({0}, {1}, {2})".format(idEstudiante, nombreEstudiante, numeroTelefono))

curInsert.execute("INSERT INTO estudiante (id_estudiante, nombre, numero_telefono) \
                    VALUES (%s, %s, %s)", (idEstudiante, nombreEstudiante, numeroTelefono))


# Crea el cursor de la conexión y establece la consulta
cur = conn.cursor()

cur.execute("SELECT id_estudiante, nombre, numero_telefono \
            FROM estudiante;")

# Obtiene las filas resultantes de la consulta
print(cur.fetchmany(size=10))
# Obtiene la cantidad de filas afectadas
print("Cantidad de filas: {0}".format(cur.rowcount))



# 4. Deshace las modificaciones (insert) a la base de datos y cierra la conexión

# Deshace las modificaciones a la base de datos
print("\n4. Deshaciendo los cambios en la base de datos")

conn.rollback()


# Libera los cursores
print("Liberando recursos y cerrando conexión")
cur.close()
curInsert.close()

# Cierra la conexión a la base de datos
conn.close()

print("Fin del script")
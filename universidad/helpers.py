import psycopg2
from psycopg2 import OperationalError
import dotenv
import os




def get_connection():

    # Obtiene las variables de ambiente
    dotenv.load_dotenv()

    PGHOST = os.getenv('PGHOST')
    PGPORT = os.getenv('PGPORT')
    PGDATABASE= os.getenv('PGDATABASE')
    PGUSER = os.getenv('PGUSER') 
    PGPASSWORD = os.getenv('PGPASSWORD')

    # Establece la conexión con la base de datos
    try:
        conn = psycopg2.connect(
                        host = PGHOST,
                        user = PGUSER,
                        dbname = PGDATABASE,
                        password = PGPASSWORD,
                        port = PGPORT)
        
        print('Conectado!')
    except OperationalError as err:
        print('Error en la conexión: ')
        
        conn = None

    return conn


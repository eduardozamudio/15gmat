import psycopg2
from psycopg2 import OperationalError
from psycopg2.extras import DictCursor
import dotenv
import os

def get_connection():
    """
    Obtiene una conexión a la base de datos

    :returns:   La conexión a la base de datos
    :rtype:     { connection }
    """

    # Obtiene las variables de ambiente
    #dotenv.load_dotenv()

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
                        port = PGPORT,
                        cursor_factory=DictCursor)
        
        print('Conectado!')
    except OperationalError as err:
        print('Error en la conexión: ')
        
        conn = None

    return conn
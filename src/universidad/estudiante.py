import psycopg2

ESTUDIANTE_QUERY = "SELECT * FROM estudiante;"
ESTUDIANTE_INSERT = "INSERT INTO estudiante (id_estudiante, nombre, numero_telefono) VALUES (%s, %s, %s);"


def getAll(conn):
    """ Obtiene todos los registros de estudiantes 

    conn -- La conexión a la base de datos
    """
    cur = conn.cursor()
    cur.execute(ESTUDIANTE_QUERY)

    return cur.fetchall()


def add(conn, id_estudiante, nombre, numero_telefono):
    """ Agrega un registro de estudiante 

    conn -- La conexión a la base de datos
    id_estudiante -- Identificadore del estudiante
    nombre -- Nombre del estudiante
    numero_telefono -- Número de teléfono del estudiante

    """
    cur = conn.cursor()
    cur.execute(ESTUDIANTE_INSERT, (id_estudiante, nombre, numero_telefono))
    
    return True

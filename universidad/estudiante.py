import psycopg2

ESTUDIANTE_QUERY = "SELECT * FROM estudiante;"
ESTUDIANTE_QUERY_ID = "SELECT * FROM estudiante WHERE id_estudiante = %s;"
ESTUDIANTE_INSERT = "INSERT INTO estudiante (id_estudiante, nombre, numero_telefono, direccion) VALUES (%s, %s, %s, %s);"
ESTUDIANTE_DELETE = "DELETE FROM estudiante WHERE id_estudiante = %s;"
ESTUDIANTE_UPDATE = "UPDATE estudiante SET {nombre = %s, numero_telefono = %s, direccion = %s} WHERE id_estudiante = %s;"


def add(conn, id_estudiante, nombre, numero_telefono, direccion):
    """
    Agrega una tupla en la relación Estudiante.

    Keyword arguments:     
    :param      conn:             La conexión a la base de datos
    :type       conn:             Instancia de pyscopg2.connection
    :param      id_estudiante:    El identificador del estudiante
    :type       id_estudiante:    str
    :param      nombre:           El nombre del estudiante
    :type       nombre:           str
    :param      numero_telefono:  El numero de telefono del estudiante
    :type       numero_telefono:  str
    :param      direccion:        La direccion del estudiante
    :type       direccion:        str

    :returns:   La tupla del estudiante
    :rtype:     tuple
    """

    try:
        cur = conn.cursor()
        cur.execute(ESTUDIANTE_INSERT,
                    (id_estudiante, nombre, numero_telefono, direccion))

        cur2 = conn.cursor()
        cur2.execute(ESTUDIANTE_QUERY_ID, (id_estudiante,))
        return cur2.fetchone()

    except Exception as e:
        raise e


def get(conn):
    """
    Obtiene todos las tuplas de la relación Estudiantes

    :param      conn:  La conexión a la base de datos
    :type       conn:  Instancia de pyscopg2.connection 

    :returns:   Todas las tuplas de la relación.
    :rtype:     list 
    """
    try:
        cur = conn.cursor()
        cur.execute(ESTUDIANTE_QUERY)
        return cur.fetchall()
    except Exception as e:
        raise e


def update(conn, id_estudiante, nombre, numero_telefono, direccion):
    """
    Actualiza la tupla de la relación Estudiante con id_estudiante

    :param      conn:             La conexión a la base de datos
    :type       conn:             Instancia de pyscopg2.connection
    :param      id_estudiante:    El identificador actual del estudiante
    :type       id_estudiante:    str
    :param      nombre:           El nombre nuevo del estudiante
    :type       nombre:           str
    :param      numero_telefono:  El numero nuevo de telefono del estudiante
    :type       numero_telefono:  str
    :param      direccion:        La direccion del estudiante
    :type       direccion:        str

    :returns:   La tupla actualizada en la relación
    :rtype:     tuple
    """
    try:
        cur = conn.cursor()
        cur.execute(ESTUDIANTE_UPDATE, (nombre, numero_telefono, direccion))

        cur2 = conn.cursor()
        cur2.execute(ESTUDIANTE_QUERY_ID, (id_estudiante,))
        return cur2.fetchone()
    except Exception as e:
        raise e


def delete(conn, id_estudiante):
    """
    Elimina una tupla de la relación

    :param      conn:           The connection
    :type       conn:           { type_description }
    :param      id_estudiante:  The identifier estudiante
    :type       id_estudiante:  { type_description }

    :returns:   La tupla eliminada de la relación.
    :rtype:     tuple 
    """

    try:
        cur = conn.cursor()
        cur.execute(ESTUDIANTE_DELETE, (id_estudiante,))

        cur2 = conn.cursor()
        cur2.execute(ESTUDIANTE_QUERY_ID, (id_estudiante,))
        return cur2.fetchone()
    except Exception as e:
        raise e

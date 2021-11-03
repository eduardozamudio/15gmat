from universidad import helpers

ESTUDIANTE_QUERY = "SELECT * FROM estudiante WHERE id_estudiante ILIKE %s OR nombre ILIKE %s OR numero_telefono ILIKE %s OR direccion ILIKE %s ESCAPE '';"
ESTUDIANTE_QUERY_ALL = "SELECT * FROM estudiante;" 
ESTUDIANTE_QUERY_ID = "SELECT * FROM estudiante WHERE id_estudiante = %s;"
ESTUDIANTE_INSERT = "INSERT INTO estudiante (id_estudiante, nombre, numero_telefono, direccion) VALUES (%s, %s, %s, %s);"
ESTUDIANTE_DELETE = "DELETE FROM estudiante WHERE id_estudiante = %s;"
ESTUDIANTE_UPDATE = "UPDATE estudiante SET nombre = %s, numero_telefono = %s, direccion = %s WHERE id_estudiante = %s;"


def add(id_estudiante, nombre, numero_telefono, direccion):
    """
    Agrega una tupla en la relación Estudiante.

    Keyword arguments:     
    :param      id_estudiante:    El identificador del estudiante
    :type       id_estudiante:    str
    :param      nombre:           El nombre del estudiante
    :type       nombre:           str
    :param      numero_telefono:  El numero de telefono del estudiante
    :type       numero_telefono:  str
    :param      direccion:        La direccion del estudiante
    :type       direccion:        str

    :returns:   La tupla del estudiante
    :rtype:     dict
    """

    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(ESTUDIANTE_INSERT,
                    (id_estudiante, nombre, numero_telefono, direccion))

        cur2 = conn.cursor()
        cur2.execute(ESTUDIANTE_QUERY_ID, (id_estudiante,))
        result = cur2.fetchone()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        cur2.close()
        conn.close()

        return result 

    except Exception as e:
        raise e


def get_all():
    """
    Obtiene todas las tuplas de la relación Estudiantes
    
    
    :returns:   Todas las tuplas de la relación.
    :rtype:     list
    """
    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(ESTUDIANTE_QUERY_ALL)
        result = cur.fetchall()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        conn.close()

        return result 
    except Exception as e:
        raise e


def get_by_id(id_estudiante):
    """
    Obtiene la tupla de la relación Estudiantes con el identificador
    
    :param      id_estudiante:  El identificador del estudiante
    :type       id_estudiante:  str
    
    :returns:   La tupla de la relación
    :rtype:     dict
    """
    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(ESTUDIANTE_QUERY_ID, (id_estudiante,))
        result = cur.fetchone()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        conn.close()

        return result 
    except Exception as e:
        raise e


def get(id_estudiante, nombre, numero_telefono, direccion):
    """
    Obtiene todos las tuplas de la relación Estudiantes
    
    :param      id_estudiante:    El identificador del estudiante
    :type       id_estudiante:    str
    :param      nombre:           El nombre del estudiante
    :type       nombre:           str
    :param      numero_telefono:  El numero de telefono del estudiante
    :type       numero_telefono:  str
    :param      direccion:        La direccion del estudiante
    :type       direccion:        str
    
    :returns:   Todas las tuplas de la relación
    :rtype:     list
    """

    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(ESTUDIANTE_QUERY, (id_estudiante,
                                       nombre, numero_telefono, direccion))
        result = cur.fetchall()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        conn.close()

        return result 
    except Exception as e:
        raise e


def update(id_estudiante, nombre, numero_telefono, direccion):
    """
    Actualiza la tupla de la relación Estudiante con id_estudiante

    :param      id_estudiante:    El identificador actual del estudiante
    :type       id_estudiante:    str
    :param      nombre:           El nombre nuevo del estudiante
    :type       nombre:           str
    :param      numero_telefono:  El numero nuevo de telefono del estudiante
    :type       numero_telefono:  str
    :param      direccion:        La direccion del estudiante
    :type       direccion:        str

    :returns:   La tupla actualizada en la relación
    :rtype:     dict
    """
    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(ESTUDIANTE_UPDATE, (nombre, numero_telefono, direccion))

        cur2 = conn.cursor()
        cur2.execute(ESTUDIANTE_QUERY_ID, (id_estudiante,))
        result = cur2.fetchone()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        cur2.close()
        conn.close()

        return result 
    except Exception as e:
        raise e


def delete(id_estudiante):
    """
    Elimina una tupla de la relación

    :param      id_estudiante:  The identifier estudiante
    :type       id_estudiante:  { type_description }

    :returns:   La tupla eliminada de la relación.
    :rtype:     dict 
    """

    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(ESTUDIANTE_DELETE, (id_estudiante,))

        cur2 = conn.cursor()
        cur2.execute(ESTUDIANTE_QUERY_ID, (id_estudiante,))
        result = cur2.fetchone()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        cur2.close()
        conn.close()

        return result 
    except Exception as e:
        raise e

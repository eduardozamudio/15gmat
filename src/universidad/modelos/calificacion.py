from universidad.helpers import helpers

CALIFICACION_QUERY = "SELECT * FROM calificaciones WHERE id_estudiante ILIKE %s OR id_asignatura ILIKE %s OR edicion ILIKE %s ESCAPE '';"
CALIFICACION_QUERY_ALL = "SELECT * FROM calificaciones;" 
CALIFICACION_QUERY_ID = "SELECT * FROM calificaciones WHERE id_estudiante = %s AND id_asignatura = %s AND edicion = %s;"
CALIFICACION_INSERT = "INSERT INTO calificaciones (id_estudiante, id_asignatura, edicion, calificacion) VALUES (%s, %s, %s, %s);"
CALIFICACION_DELETE = "DELETE FROM calificaciones WHERE id_estudiante = %s AND id_asignatura = %s AND edicion = %s;"
CALIFICACION_UPDATE = "UPDATE calificaciones SET calificacion = %s WHERE id_estudiante = %s AND id_asignatura = %s AND edicion = %s;"


def add(id_estudiante, id_asignatura, edicion, calificacion):
    """
    Agrega una tupla en la relación Estudiante.
    
    Keyword arguments:
    
    :param      id_estudiante:  El identificador del estudiante
    :type       id_estudiante:  str
    :param      id_asignatura:  El identificadir de la asignatura
    :type       id_asignatura:  str
    :param      edicion:        La edición de la asignatura
    :type       edicion:        str
    :param      calificacion:   La calificación del estudiante
    :type       calificacion:   int
    
    :returns:   La tupla de calificacion
    :rtype:     dict
    """

    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(CALIFICACION_INSERT,
                    (id_estudiante, id_asignatura, edicion, calificacion))

        cur2 = conn.cursor()
        cur2.execute(CALIFICACION_QUERY_ID, (id_estudiante, id_asignatura, edicion))

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
        cur.execute(CALIFICACION_QUERY_ALL)
        
        result = cur.fetchall()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        conn.close()

        return result 

    except Exception as e:
        raise e


def get_by_id(id_estudiante, id_asignatura, edicion):
    """
    Obtiene la tupla de la relación Estudiantes con el identificador
    
    :param      id_estudiante:  El identificador del estudiante
    :type       id_estudiante:  str
    :param      id_asignatura:  El identificadir de la asignatura
    :type       id_asignatura:  str
    :param      edicion:        La edición de la asignatura
    :type       edicion:        str
    
    :returns:   La tupla de la relación
    :rtype:     dict
    """
    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(CALIFICACION_QUERY_ID, (id_estudiante, id_asignatura, edicion))
        result = cur.fetchone()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        conn.close()

        return result 
    except Exception as e:
        raise e


def get(id_estudiante, id_asignatura, edicion):
    """
    Obtiene todos las tuplas de la relación Estudiantes
    
    :param      id_estudiante:  El identificador del estudiante
    :type       id_estudiante:  str
    :param      id_asignatura:  El identificadir de la asignatura
    :type       id_asignatura:  str
    :param      edicion:        La edición de la asignatura
    :type       edicion:        str
    
    :returns:   Todas las tuplas de la relación
    :rtype:     list
    """

    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(CALIFICACION_QUERY, (id_estudiante, id_asignatura, edicion))
        result = cur.fetchall()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        conn.close()

        return result 

    except Exception as e:
        raise e


def update(id_estudiante, id_asignatura, edicion, calificacion):
    """
    Actualiza la tupla de la relación Estudiante con id_calificaciones
    
    :param      id_estudiante:  El identificador del estudiante
    :type       id_estudiante:  str
    :param      id_asignatura:  El identificadir de la asignatura
    :type       id_asignatura:  str
    :param      edicion:        La edición de la asignatura
    :type       edicion:        str
    :param      calificacion:   La calificación del estudiante
    :type       calificacion:   int
    
    :returns:   La tupla actualizada en la relación
    :rtype:     dict
    """
    try:
        conn = helpers.get_connection()
        cur = conn.cursor()
        cur.execute(CALIFICACION_UPDATE, (calificacion, id_estudiante, id_asignatura, edicion))

        cur2 = conn.cursor()
        cur2.execute(CALIFICACION_QUERY_ID, (id_estudiante, id_asignatura, edicion))
        result = cur2.fetchone()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        cur2.close()
        conn.close()

        return result 
    except Exception as e:
        raise e


def delete(id_estudiante, id_asignatura, edicion):
    """
    Elimina una tupla de la relación
    
    :param      id_estudiante:  El identificador del estudiante
    :type       id_estudiante:  str
    :param      id_asignatura:  El identificadir de la asignatura
    :type       id_asignatura:  str
    :param      edicion:        La edición de la asignatura
    :type       edicion:        str
    
    :returns:   La tupla eliminada de la relación.
    :rtype:     dict
    """

    try:
        conn = helpers.get_connection()
        cur = conn.cursor()
        cur.execute(CALIFICACION_DELETE, (id_estudiante, id_asignatura, edicion))

        cur2 = conn.cursor()
        cur2.execute(CALIFICACION_QUERY_ID, (id_estudiante, id_asignatura, edicion))
        
        result = cur2.fetchone()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        cur2.close()
        conn.close()

        return result 
    except Exception as e:
        raise e

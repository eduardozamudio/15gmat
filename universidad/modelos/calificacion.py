CALIFICACION_QUERY = "SELECT * FROM calificaciones WHERE id_estudiante ILIKE %s OR id_asignatura ILIKE %s OR edicion ILIKE %s ESCAPE '';"
CALIFICACION_QUERY_ALL = "SELECT * FROM calificaciones;" 
CALIFICACION_QUERY_ID = "SELECT * FROM calificaciones WHERE id_estudiante = %s AND id_asignatura = %s AND edicion = %s;"
CALIFICACION_INSERT = "INSERT INTO calificaciones (id_estudiante, id_asignatura, edicion, calificacion) VALUES (%s, %s, %s, %s);"
CALIFICACION_DELETE = "DELETE FROM calificaciones WHERE id_estudiante = %s AND id_asignatura = %s AND edicion = %s;"
CALIFICACION_UPDATE = "UPDATE calificaciones SET calificacion = %s, WHERE id_estudiante = %s, id_asignatura = %s, edicion = %s;"


def add(conn, id_estudiante, id_asignatura, edicion, calificacion):
    """
    Agrega una tupla en la relación Estudiante.
    
    Keyword arguments:
    
    :param      conn:           La conexión a la base de datos
    :type       conn:           Instancia de pyscopg2.connection
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
        cur = conn.cursor()
        cur.execute(CALIFICACION_INSERT,
                    (id_estudiante, id_asignatura, edicion, calificacion))

        cur2 = conn.cursor()
        cur2.execute(CALIFICACION_QUERY_ID, (id_estudiante, id_asignatura, edicion))
        return cur2.fetchone()

    except Exception as e:
        raise e


def get_all(conn):
    """
    Obtiene todas las tuplas de la relación Estudiantes
    
    :param      conn:  La conexión a la base de datos
    :type       conn:  Instancia de pyscopg2.connection
    
    :returns:   Todas las tuplas de la relación.
    :rtype:     list
    """
    try:
        cur = conn.cursor()
        cur.execute(CALIFICACION_QUERY_ALL)
        return cur.fetchall()
    except Exception as e:
        raise e


def get_by_id(conn, id_estudiante, id_asignatura, edicion):
    """
    Obtiene la tupla de la relación Estudiantes con el identificador
    
    :param      conn:           La conexión a la base de datos
    :type       conn:           Instancia de pyscopg2.connection
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
        cur = conn.cursor()
        cur.execute(CALIFICACION_QUERY_ID, (id_estudiante, id_asignatura, edicion))
        return cur.fetchone()
    except Exception as e:
        raise e


def get(conn, id_estudiante, id_asignatura, edicion):
    """
    Obtiene todos las tuplas de la relación Estudiantes
    
    :param      conn:           La conexión a la base de datos
    :type       conn:           Instancia de pyscopg2.connection
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
        cur = conn.cursor()
        cur.execute(CALIFICACION_QUERY, (id_estudiante, id_asignatura, edicion))
        return cur.fetchall()
    except Exception as e:
        raise e


def update(conn, id_estudiante, id_asignatura, edicion, calificacion):
    """
    Actualiza la tupla de la relación Estudiante con id_calificaciones
    
    :param      conn:           La conexión a la base de datos
    :type       conn:           Instancia de pyscopg2.connection
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
        cur = conn.cursor()
        cur.execute(CALIFICACION_UPDATE, (calificacion, id_estudiante, id_asignatura, edicion))

        cur2 = conn.cursor()
        cur2.execute(CALIFICACION_QUERY_ID, (id_estudiante, id_asignatura, edicion))
        return cur2.fetchone()
    except Exception as e:
        raise e


def delete(conn, id_estudiante, id_asignatura, edicion):
    """
    Elimina una tupla de la relación
    
    :param      conn:           The connection
    :type       conn:           { type_description }
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
        cur = conn.cursor()
        cur.execute(CALIFICACION_DELETE, (id_estudiante, id_asignatura, edicion))

        cur2 = conn.cursor()
        cur2.execute(CALIFICACION_QUERY_ID, (id_estudiante, id_asignatura, edicion))
        return cur2.fetchone()
    except Exception as e:
        raise e

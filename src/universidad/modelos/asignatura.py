from universidad.helpers import helpers

ASIGNATURA_QUERY = "SELECT * FROM asignatura WHERE id_asignatura ILIKE %s OR nombre ILIKE %s OR grado ILIKE %s OR anio = %s OR semestre = %s OR tipo ILIKE %s OR creditos = %s ;"
ASIGNATURA_QUERY_ALL = "SELECT * FROM asignatura;"
ASIGNATURA_QUERY_ID = "SELECT * FROM asignatura WHERE id_asignatura = %s;"
ASIGNATURA_INSERT = "INSERT INTO asignatura (id_asignatura, nombre, grado, anio, semestre, tipo, creditos) VALUES (%s, %s, %s, %s, %s, %s, %s);"
ASIGNATURA_DELETE = "DELETE FROM asignatura WHERE id_asignatura = %s;"
ASIGNATURA_UPDATE = "UPDATE asignatura SET nombre = %s, grado = %s, anio = %s, semestre = %s, tipo = %s, creditos = %s WHERE id_asignatura = %s;"


def add(id_asignatura, nombre, grado, anio, semestre, tipo, creditos):
    """
    Agrega una tupla en la relación Estudiante.

    Keyword arguments:

    :param      id_asignatura:  El identificador del asignatura
    :type       id_asignatura:  str
    :param      nombre:         El nombre del asignatura
    :type       nombre:         str
    :param      grado:          El grado de la asignatura
    :type       grado:          str
    :param      anio:           El anio de la asignatura
    :type       anio:           int
    :param      semestre:       El semestre de la asignatura
    :type       semestre:       int
    :param      tipo:           El tipo de la asignatura
    :type       tipo:           str
    :param      creditos:       Los creditos de la asignatura
    :type       creditos:       int

    :returns:   La tupla del asignatura
    :rtype:     dict
    """

    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(ASIGNATURA_INSERT, (id_asignatura, nombre,
                                        grado, anio, semestre, tipo, creditos))

        cur2 = conn.cursor()
        cur2.execute(ASIGNATURA_QUERY_ID, (id_asignatura,))
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
        cur.execute(ASIGNATURA_QUERY_ALL)
        result = cur.fetchall()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        conn.close()

        return result
    except Exception as e:
        raise e


def get_by_id(id_asignatura):
    """
    Obtiene la tupla de la relación Estudiantes con el identificador

    :param      id_asignatura:  El identificador de la asignatura
    :type       id_asignatura:  str

    :returns:   Todas las tuplas de la relación.
    :rtype:     dict
    """
    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(ASIGNATURA_QUERY_ID, (id_asignatura,))
        result = cur.fetchone()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        conn.close()

        return result
    except Exception as e:
        raise e


def get(id_asignatura, nombre, grado, anio, semestre, tipo, creditos):
    """
    Obtiene todos las tuplas de la relación Asignatura

    :param      id_asignatura:  El identificador de la asignatura
    :type       id_asignatura:  str
    :param      nombre:         El nombre del asignatura
    :type       nombre:         str
    :param      grado:          El grado de la asignatura
    :type       grado:          str
    :param      anio:           El anio de la asignatura
    :type       anio:           int
    :param      semestre:       El semestre de la asignatura
    :type       semestre:       int
    :param      tipo:           El tipo de la asignatura
    :type       tipo:           str
    :param      creditos:       Los creditos de la asignatura
    :type       creditos:       int

    :returns:   Todas las tuplas de la relación
    :rtype:     list
    """

    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(ASIGNATURA_QUERY, (id_asignatura, nombre,
                                       grado, anio, semestre, tipo, creditos))
        result = cur.fetchall()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        conn.close()

        return result
    except Exception as e:
        raise e


def update(id_asignatura, nombre, grado, anio, semestre, tipo, creditos):
    """
    Actualiza la tupla de la relación Estudiante con id_asignatura

    :param      id_asignatura:  El identificador actual del asignatura
    :type       id_asignatura:  str
    :param      nombre:         El nombre nuevo del asignatura
    :type       nombre:         str
    :param      grado:          El grado de la asignatura
    :type       grado:          str
    :param      anio:           El anio de la asignatura
    :type       anio:           int
    :param      semestre:       El semestre de la asignatura
    :type       semestre:       int
    :param      tipo:           El tipo de la asignatura
    :type       tipo:           str
    :param      creditos:       Los creditos de la asignatura
    :type       creditos:       int

    :returns:   La tupla actualizada en la relación
    :rtype:     dict
    """
    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(ASIGNATURA_UPDATE, (nombre, grado, anio,
                                        semestre, tipo, creditos, id_asignatura))

        cur2 = conn.cursor()
        cur2.execute(ASIGNATURA_QUERY_ID, (id_asignatura,))
        result = cur2.fetchone()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        cur2.close()
        conn.close()

        return result
    except Exception as e:
        raise e


def delete(id_asignatura):
    """
    Elimina una tupla de la relación

    :param      id_asignatura:  The identifier asignatura
    :type       id_asignatura:  { type_description }

    :returns:   La tupla eliminada de la relación.
    :rtype:     dict 
    """

    try:
        conn = helpers.get_connection()

        cur = conn.cursor()
        cur.execute(ASIGNATURA_DELETE, (id_asignatura,))

        cur2 = conn.cursor()
        cur2.execute(ASIGNATURA_QUERY_ID, (id_asignatura,))
        result = cur2.fetchone()

        # Confirma los cambios y libera recursos
        conn.commit()

        cur.close()
        cur2.close()
        conn.close()

        return result
    except Exception as e:
        raise e

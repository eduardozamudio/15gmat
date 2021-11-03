from universidad.modelos import calificacion
from universidad import helpers


def get_promedio_asignatura(id_asignatura, edicion):
    """
    Obtiene el primedio de una asignatura para una edicion

    :param      id_asignatura:  El identificador de la asignatura
    :type       id_asignatura:  str
    :param      edicion:        La edición
    :type       edicion:        str
    """

    conn = helpers.get_connection()

    calificaciones = calificacion.get(conn, id_estudiante = '', id_asignatura = id_asignatura, edicion = edicion)    

    calificaciones_individuales = [row['calificacion'] for row in calificaciones]

    if (len(calificaciones_individuales) != 0):
        return sum(calificaciones_individuales) / len(calificaciones_individuales)
    else:
        return None
 
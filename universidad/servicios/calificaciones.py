from universidad.modelos import calificacion


def get_promedio_asignatura(id_asignatura, edicion):
    """
    Obtiene el primedio de una asignatura para una edicion
    
    :param      id_asignatura:  El identificador de la asignatura
    :type       id_asignatura:  str
    :param      edicion:        La edición
    :type       edicion:        str
    
    :returns:   El promedio de la asignatura.
    :rtype:     float
    """

    calificaciones = calificacion.get(id_estudiante = '', id_asignatura = id_asignatura, edicion = edicion)    

    calificaciones_individuales = [row['calificacion'] for row in calificaciones]

    if (len(calificaciones_individuales) != 0):
        return sum(calificaciones_individuales) / len(calificaciones_individuales)
    else:
        return None
 
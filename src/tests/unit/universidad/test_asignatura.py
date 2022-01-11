import pytest
from universidad.modelos import asignatura


def test_get_by_id(id_asignatura):
    """
    Debe obtener la asignatura con id_asignatura
    
    :param      id_asignatura:   El identificador de la asignatura
    :type       id_asignatura:   str
    
    """

    asignatura_query = asignatura.get_by_id(id_asignatura)
    if (asignatura_query != None):
        assert asignatura_query['id_asignatura'] == id_asignatura
        assert asignatura_query['nombre'] == "Programación III: Bases de datos y programación"  # 1 - Nombre
    else:
        assert 0


def test_get(asignatura_filtro):
    """
    Debe obtener el asignatura con el filtro
    
    :param      asignatura_filtro:  Filtros de la asignatura
    :type       asignatura_filtro:  dict
    
    """

    id_asignatura = asignatura_filtro["id_asignatura"]
    nombre = asignatura_filtro["nombre"]
    grado = asignatura_filtro["grado"]
    anio = asignatura_filtro["anio"]
    semestre = asignatura_filtro["semestre"]
    tipo = asignatura_filtro["tipo"]
    creditos = asignatura_filtro["creditos"]

    asignatura_query = asignatura.get(id_asignatura, nombre, grado, anio, semestre, tipo, creditos)
    if (asignatura_query[0] != None):
        assert asignatura_query[0]['nombre'] == "Programación III: Bases de datos y programación"  # 1 - Nombre
    else:
        assert 0


@pytest.fixture(scope="module")
def id_asignatura():
    return "15GMAT"


@pytest.fixture(scope="module")
def asignatura_filtro():
    filtro = {"id_asignatura": "15GMAT%",
              "nombre": "%Programación%",
              "grado": "",
              "anio": 2,
              "semestre": 1,
              "tipo" : "Obligatoria",
              "creditos": 6,
              }
    return filtro

import pytest
from universidad.modelos import estudiante


def test_get_by_id(id_estudiante):
    """
    Debe obtener el estudiante con el id_estudiante
    
    :param      id_estudiante:   El identificador de estudiante
    :type       id_estudiante:   int
    
    """

    estudiante_query = estudiante.get_by_id(id_estudiante)
    if (estudiante_query != None):
        assert estudiante_query['id_estudiante'] == id_estudiante
        assert estudiante_query['nombre'] == "Eduardo"  # 1 - Nombre
    else:
        assert 0


def test_get(estudiante_filtro):
    """
    Debe obtener el estudiante con el filtro
    
    :param      estudiante_filtro:  El identificador de estudiante
    :type       estudiante_filtro:  int
    
    """

    id_estudiante = estudiante_filtro["id_estudiante"]
    nombre = estudiante_filtro["nombre"]
    numero_telefono = estudiante_filtro["numero_telefono"]
    direccion = estudiante_filtro["direccion"]

    estudiante_query = estudiante.get(id_estudiante, nombre, numero_telefono, direccion)
    if (estudiante_query[0] != None):
        assert estudiante_query[0]['nombre'] == "Eduardo"  # 1 - Nombre
    else:
        assert 0


@pytest.fixture(scope="module")
def id_estudiante():
    return "29441979"


@pytest.fixture(scope="module")
def estudiante_filtro():
    filtro = {"id_estudiante": "29441%",
              "nombre": "Eduar%",
              "numero_telefono": "",
              "direccion": ""
              }
    return filtro

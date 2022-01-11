import pytest
from universidad.servicios import calificaciones


def test_get_promedio_asignatura(id_asignatura, edicion):
    
    promedio = calificaciones.get_promedio_asignatura(id_asignatura, edicion)
    assert promedio == 8.5



@pytest.fixture(scope="module")
def id_asignatura():
    return "15GMAT"

@pytest.fixture(scope="module")
def edicion():
    return "Octubre 2021"
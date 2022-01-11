from universidad.helpers import helpers


def test_get_connection(get_connection):
    """
    Debe establecer una conexión con la base de datos
    """

    conn = get_connection()
    assert conn.info.status == 0

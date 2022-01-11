import pytest
import universidad.helpers

@pytest.fixture(scope="module")
def get_connection():
    return universidad.helpers.helpers.get_connection
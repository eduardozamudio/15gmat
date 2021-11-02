import unittest

import sys

# sys.path.append('../')
# sys.path.append('.env')
# sys.path.append('')

from universidad import helpers


class TestEstudiante(unittest.TestCase):

    def test_get_connection(self):
        """
        Unit test for get_connection
        """

        conn = helpers.get_connection()
        self.assertEqual(conn.info.status, 0)


if __name__ == '__main__':
    unittest.main()

# unittest clase Persona
import unittest
from Persona import Persona
from datetime import datetime


class TestPersona(unittest.TestCase):

    # Metodo que se ejecuta al inicio de cada caso
    def setUp(self):
        self.juancito = Persona('Juancito', 'Gomez', '123',
                        datetime(2000, 11, 28))

    # Metodo que se ejecuta al finalizar cada caso para liberar recursos
    def tearDown(self):
        pass

    def test_juancito(self):
        self.assertEqual(self.juancito.get_nombre(), 'Juancito')
        self.assertEqual(self.juancito.get_apellido(), 'Gomez')
        self.assertEqual(self.juancito.get_id_personal(), '123')
        self.assertEqual(self.juancito.get_fecha_nacimiento(),
                         datetime(2000, 11, 28))

    def test_edad_positiva(self):
        self.assertGreaterEqual(self.juancito.get_edad(), 0)


if __name__ == '__main__':
    unittest.main(verbosity=0)

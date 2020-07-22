# unittest clase Persona
import unittest
from Persona import Persona


class TestPersona(unittest.TestCase):

    # Metodo que se ejecuta al inicio de cada caso
    def setUp(self):
        self.juancito = Persona('Juancito', 'Gomez', '123', '20/01/1980')
        
    # Metodo que se ejecuta al finalizar cada caso para liberar recursos
    def tearDown(self):
        pass

    def test_juancito(self):
        self.assertEqual(self.juancito.get_nombre(), 'Juancito')
        self.assertEqual(self.juancito.get_apellido(), 'Gomez')
        self.assertEqual(self.juancito.get_id_personal(), '123')
        self.assertEqual(self.juancito.get_fecha_nacimiento(), '20/01/1980')


if __name__ == '__main__':
    unittest.main(verbosity=0)
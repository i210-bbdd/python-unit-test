# Fragmento de Sistema ERP (modulo web bancario)
import unittest
from CuentaBancaria import cuentaBancaria
# from Clientes import clientes
# from TipoCuentas import tipoCuentas
# from TipoClientes import tipoClientes


class TestCuentaBancaria(unittest.TestCase):

    # Metodo que se ejecuta al inicio de cada caso
    def setUp(self):
        self.cb1 = cuentaBancaria('CC', '1234', 0)
        self.cb2 = cuentaBancaria('CA', '3456', 0)

    # Metodo que se ejecuta al finalizar cada caso para liberar recursos
    def tearDown(self):
        pass

    def test_saldo_inicial(self):
        self.assertEqual(self.cb1.getSaldo(), 0, "Debe mostrar 0")
        self.assertEqual(self.cb1.getCantMovimientos(), 1, "Debe mostrar 1")

    def test_saldo_100(self):
        self.cb1.depositar(100)
        self.assertEqual(self.cb1.getSaldo(), 100, "Debe mostrar 100")
        self.assertEqual(self.cb1.getCantMovimientos(), 2, "Debe mostrar 2")

    def test_saldo_menos_100(self):
        self.cb1.retirar(100)
        self.assertEqual(self.cb1.getSaldo(), 0, "Debe mostrar 0")

    def test_saldo_varios_movimiento(self):
        self.cb1.retirar(100)
        self.cb1.depositar(100)
        self.cb1.retirar(100)
        self.cb1.depositar(100)
        self.cb1.retirar(100)
        self.assertEqual(self.cb1.getSaldo(), 0, "Debe mostrar 0")

    def test_saldo_tras_movimientos_entre_cuentas(self):
        self.cb1.depositar(100)
        self.cb1.retirar(20)
        self.cb2.depositar(20)
        self.cb2.retirar(20)
        self.cb1.retirar(80)
        cant = self.cb1.getSaldo() - self.cb2.getSaldo()
        self.assertEqual(cant, 0, "Debe mostrar 0")
        cant = self.cb1.getCantMovimientos()+self.cb2.getCantMovimientos()
        self.assertEqual(cant, 7, "Debe mostrar 7 movimientos en total")

    def test_nro_y_tipo_cuenta(self):
        self.assertEqual(self.cb1.getNroCuenta(), '1234', "Debe mostrar 1234")
        self.assertEqual(self.cb1.getTipoCuenta(), 'CC', "Debe mostrar CA")


if __name__ == '__main__':
    unittest.main(verbosity=0)

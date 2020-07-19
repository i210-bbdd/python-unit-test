# Autor: Felipe Morales
# Fragmento de Sistema LK-ERP (modulo web bancario)
import unittest
from CuentaBancaria import cuentaBancaria, cuentaBancaria_CajaAhorro
from CuentaBancaria import cuentaBancaria_CuentaCorriente
# from tipoCuentas import tipoCuenta


class TestCuentaBancaria(unittest.TestCase):
    # Metodo que se ejecuta al inicio de cada caso
    def setUp(self):
        self.cb1 = cuentaBancaria(0)
        self.cb2 = cuentaBancaria(0)
        self.cb_ca = cuentaBancaria_CajaAhorro(0)
        self.cb_cc = cuentaBancaria_CuentaCorriente(0)

    # Metodo que se ejecuta al finalizar cada caso para liberar recursos
    def tearDown(self):
        pass

    def test_saldo_inicial(self):
        self.assertEqual(self.cb1.getSaldo(), 0, "Debe mostrar 0")
        self.assertEqual(self.cb1.getCantMovimientos(), 1, "Debe mostrar 1")
        self.assertEqual(self.cb1.ultimo_error[0], 0, "CA. Código de error 0")

    def test_saldo_100(self):
        self.cb1.depositar(100)
        self.assertEqual(self.cb1.getSaldo(), 100, "Debe mostrar 100")
        self.assertEqual(self.cb1.getCantMovimientos(), 2, "Debe mostrar 2")
        self.assertEqual(self.cb1.ultimo_error[0], 0, "CA. Código Error 0")

    def test_saldo_menos_100(self):
        self.cb1.retirar(100)
        self.assertEqual(self.cb1.getSaldo(), -100, "Debe mostrar 0")
        self.assertEqual(self.cb1.ultimo_error[0], 0, "CA. Código Error 0")

    def test_saldo_varios_movimiento(self):
        self.cb1.retirar(100)
        self.cb1.depositar(100)
        self.cb1.retirar(100)
        self.cb1.depositar(100)
        self.cb1.retirar(100)
        self.assertEqual(self.cb1.getSaldo(), -100, "Debe mostrar 0")
        self.assertEqual(self.cb1.ultimo_error[0], 0, "CA. Código Error 0")

    def test_saldo_tras_movimientos_entre_cuentas(self):
        self.cb1.depositar(100)
        self.cb1.retirar(20)
        self.cb2.depositar(20)
        self.cb2.retirar(20)
        self.cb1.retirar(80)
        cant = self.cb1.getSaldo()-self.cb2.getSaldo()
        self.assertEqual(cant, 0, "Debe mostrar 0")
        cant = self.cb1.getCantMovimientos()+self.cb2.getCantMovimientos()
        self.assertEqual(cant, 7, "Debe mostrar 7 movimientos en total")
        self.assertEqual(self.cb1.ultimo_error[0], 0, "CA. Código Error 0")
        self.assertEqual(self.cb2.ultimo_error[0], 0, "CA. Código Error 0")

    def test_retiro_negativo_caja_ahorro(self):
        self.cb_ca.retirar(100)
        self.assertEqual(self.cb_ca.getSaldo(), 0, "CA. Debe mostrar 0")
        self.assertEqual(self.cb_ca.ultimo_error[0], -1, "CA. Código Error -1")

    def test_retiro_negativo_cuenta_corriente(self):
        self.cb_cc.retirar(100)
        self.assertEqual(self.cb_cc.getSaldo(), -100, "CC. Debe mostrar 0")
        self.assertEqual(self.cb_cc.ultimo_error[0], 0, "CC. Código Error 0")


if __name__ == '__main__':
    unittest.main(verbosity=0)

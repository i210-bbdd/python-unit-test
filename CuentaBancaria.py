# Clase CuentaBancaria
class cuentaBancaria():
    # Tipo de cuenta: CA: Caja de Ahorro,CC: Cuenta Corriente, CS:Cuenta Sueldo
    tipo_cuenta = ''
    nro_cuenta = ''
    saldo = 0
    movimientos = 0
    consultas_saldo = 0

    def __init__(self, tipo_cuenta, nro_cuenta, saldo):
        self.movimientos += 1
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta
        self.nro_cuenta = nro_cuenta

    def depositar(self, aMount):
        self.movimientos += 1
        self.saldo = self.saldo + aMount

    def retirar(self, aMount):
        # Condiciono a que tenga saldo
        if self.saldo >= aMount:
            self.movimientos += 1
            self.saldo = self.saldo - aMount

    def getSaldo(self):
        self.consultas_saldo += 1
        return self.saldo

    def getCantMovimientos(self):
        return self.movimientos

    def getCantConsultasSaldo(self):
        return self.consultas_saldo

    def getNroCuenta(self):
        return self.nro_cuenta

    def getTipoCuenta(self):
        return self.tipo_cuenta     
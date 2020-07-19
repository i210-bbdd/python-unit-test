# Clase CuentaBancaria
class cuentaBancaria():
    saldo = 0
    movimientos = 0
    consultas_saldo = 0

    def __init__(self, saldo):
        self.movimientos += 1
        self.saldo = saldo

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

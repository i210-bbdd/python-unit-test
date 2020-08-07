# Clase CuentaBancaria
class cuentaBancaria():

    def __init__(self, tipo_cuenta, nro_cuenta, saldo):
        self.saldo = saldo
        # Tipo de cuenta: CA: Caja de Ahorro,CC: Cta Corriente, CS:Cta Sueldo
        self.tipo_cuenta = tipo_cuenta
        self.nro_cuenta = nro_cuenta
        self.movimientos = 1
        self.consultas_saldo = 0
        self.porc_comision = 0

    def depositar(self, aMount):
        self.movimientos += 1
        self.saldo = self.saldo + aMount

    def retirar(self, aMount):
        # Condiciono a que tenga saldo
        if self.saldo >= aMount:
            self.movimientos += 1
            self.saldo = self.saldo - aMount

    def get_Saldo(self):
        self.consultas_saldo += 1
        return self.saldo

    def get_CantMovimientos(self):
        return self.movimientos

    def get_CantConsultasSaldo(self):
        return self.consultas_saldo

    def get_NroCuenta(self):
        return self.nro_cuenta

    def get_TipoCuenta(self):
        return self.tipo_cuenta

    def set_NroCuenta(self, nro_cuenta):
        self.nro_cuenta = nro_cuenta

    def set_TipoCuenta(self, tipo_cuenta):
        self.tipo_cuenta = tipo_cuenta

    def get_porc_comision(self):
        return self.porc_comision

    def set_porc_comision(self, comision):
        self.porc_comision = comision

# Autor: Felipe Morales
# Fecha: 26/07/2020
class tipoCuenta():

    def __init__(self, tipo, nombre, limite, max_operaciones):
        self.tipo = tipo
        self.nombre = nombre
        self.limite = limite
        self.max_operaciones = max_operaciones

    def get_tipo(self):
        return self.tipo

    def get_nombre(self):
        return self.nombre

    def get_limite(self):
        return self.limite

# Autor: Felipe Morales
class tipoCuenta():

    def __init__(self, tipo, nombre, limite):
        self.tipo = tipo
        self.nombre = nombre
        self.limite = limite

    def get_tipo(self):
        return self.tipo

    def get_nombre(self):
        return self.nombre

    def get_limite(self):
        return self.limite

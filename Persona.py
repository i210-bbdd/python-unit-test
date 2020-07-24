from datetime import date


class Persona:
    def __init__(self, nombre, apellido, id_personal, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.id_personal = id_personal
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = ""
        self.email = ""

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_id_personal(self):
        return self.id_personal

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def get_edad(self):
        return (date.today().year - self.fecha_nacimiento.year)

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_email(self, email):
        self.email = email

    def __str__(self):
        return "nombre: " + self.nombre + " , " + "apellido: " + self.apellido

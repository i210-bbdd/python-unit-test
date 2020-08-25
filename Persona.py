# Autor: Felipe Morales
from datetime import date


class Persona:
    def __init__(self, nombre, apellido, id_personal, fecha_nacimiento):
        'Método de inicialización'
        self.nombre = nombre
        self.apellido = apellido
        self.id_personal = id_personal
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = ""
        self.email = ""
        self.sexo = ""
        self.altura = 0
        self.peso = 0

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_id_personal(self):
        return self.id_personal

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def get_telefono(self):
        return self.telefono

    def get_email(self):
        return self.email

    def get_edad(self):
        return (date.today().year - self.fecha_nacimiento.year)

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_email(self, email):
        self.email = email

    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_sexo(self):
        return self.sexo

    def set_altura(self, altura):
        self.altura = altura

    def get_altura(self):
        return self.altura

    def set_peso(self, peso):
        self.peso = peso

    def get_peso(self):
        return self.peso

    def __str__(self):
        return "Nombre: " + self.nombre + " , " + "Apellido: " + self.apellido

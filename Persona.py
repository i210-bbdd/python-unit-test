class Persona:
    def __init__(self, nombre, apellido, id_personal, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.id_personal = id_personal
        self.fecha_nacimiento = fecha_nacimiento

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_id_personal(self):
        return self.id_personal

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def __str__():
        return "nombre: " + nombre + " , " + "apellido: " + apellido + " , " + "id_personal: " + id_personal + " , " + "fecha_nacimiento: " + fecha_nacimiento

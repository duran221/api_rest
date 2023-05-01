from src.models.usuario import *

class Estudiante(Usuario):

    def __init__(self,documento,nombres,apellidos,fecha_nacimiento,edad,genero,direccion,promedio):
        self.promedio=promedio
        super().__init__(documento, nombres, apellidos, fecha_nacimiento, edad, genero, direccion)

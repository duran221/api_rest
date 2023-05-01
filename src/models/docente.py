from src.models.usuario import *

class Docente(Usuario):

    def __init__(self,codigo_docente,documento,nombres,apellidos,fecha_nacimiento,edad,genero,direccion,salario):
        self.salario=salario
        self.codigo_docente=codigo_docente
        super().__init__(documento, nombres, apellidos, fecha_nacimiento, edad, genero, direccion)
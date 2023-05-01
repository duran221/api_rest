from src.models.docente import  Docente

class Asignatura:

    def __init__(self,codigo_asignatura,codigo_docente,nombre_asignatura,numero_creditos):
        self.codigo_asignatura=codigo_asignatura
        self.codigo_docente=codigo_docente
        self.nombre_asignatura=nombre_asignatura
        self.numero_creditos=numero_creditos
        self.nota_asignatura= 0
        self.docente = None
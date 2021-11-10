

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        lista=[]
        for x in kwargs.values():
            lista.append(Asignatura(x))
        self.asignarNombre = lista
        lista.clear()

    def agregarAlumno(self, alumno, lista=[]):
        if(len(lista) != 0):
            lista.append(alumno)
            self.listadoAlumnos =  lista
        else:
            self.listadoAlumnos = [alumno]

    def __str__(self):
        cadena = "Grupo de estudiantes: " + self._grupo
        return cadena

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre

from datetime import time
from pony.orm import *

db = Database("sqlite", "database.sqlite", create_db=True)

class Universidad(db.Entity):
    idUni = PrimaryKey(str)
    NombreUni = Required(str)
    escuelas = Set("Escuela")
    
    
class Escuela(db.Entity):
    idEsc = PrimaryKey(str)
    Nombre = Required(str)
    universidad = Required(Universidad)
    departamentos = Set("Departamento")


class Asignatura(db.Entity):
    idAsig = PrimaryKey(int)
    Nombre = Required(str)
    departamento = Required("Departamento")
    cambios = Set("Cambio")


class Departamento(db.Entity):
    idDep = PrimaryKey(str)
    Nombre = Required(str)
    escuela = Required(Escuela)
    asignaturas = Set(Asignatura)


class Cambio(db.Entity):
    idC = PrimaryKey(int, auto=True)
    Titulo = Required(str)
    Body = Required(str)
    Fecha = Optional(time)
    asignatura = Required(Asignatura)
    categoria = Required("Categoria")


class Categoria(db.Entity):
    idCat = PrimaryKey(int, auto=True)
    Nombre = Required(str)
    cambios = Set(Cambio)


sql_debug(True)
db.generate_mapping(create_tables=True)

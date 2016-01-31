#!/usr/bin/pyhton
from pony.orm import *


@db_session
def conexion(raiz_db):
    db = Database('sqlite', raiz_db, create_db=False)
    print "Se ha realizado la conexion a la base de datos"
    return db



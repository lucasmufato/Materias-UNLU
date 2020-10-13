
from __future__ import print_function

import csv
import difflib
import enum
import psycopg2
import unicodedata

from pgdb import Cursor, Connection

hostname = 'localhost'
port = 54321
username = 'BDM'
password = 'bdm'
database = 'BDM'

def sacar_acentos(text):
    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    return str(text)

class Medio(enum.Enum):
     ID = 0
     NOMBRE = 1
     PROV = 2
     CIUDAD = 3
     TIPO = 4
     ESP = 5
     DIR = 6

def getProvinciasFromDb(conn) :
    cur = conn.cursor()
    cur.execute( "SELECT * FROM provincias" )
    prov = {}
    for id, descripcion in cur.fetchall() :
        prov[descripcion] = id
    return prov

def clean_string(word: str):
    return sacar_acentos( word ).lower().strip()

def findClosestProvincia(provincia: str, posibles_provincias: dict):
    prov_mas_parecida = difflib.get_close_matches(provincia, posibles_provincias.keys() , 1)
    if len(prov_mas_parecida) == 0:
        return None
    else:
        provincia_id = posibles_provincias[prov_mas_parecida.pop()]
        return provincia_id

def getProvincia(provincia, connection):
    clean_provincia = clean_string(provincia)
    if len(clean_provincia) < 3:
        return None
    return findClosestProvincia(clean_provincia, getProvinciasFromDb(connection) )


def getCiudadesPorProvincia(provincia_id, conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM ciudades where id_provincia = "+ str(provincia_id))
    ciudades = {}
    for id, nombre, prov in cur.fetchall():
        ciudades[nombre] = id
    return ciudades


def insertarEnCiudad(ciudad, provincia, conn):
    cur:Cursor = conn.cursor()
    cur.execute("INSERT INTO ciudades(nombre, id_provincia) VALUES (%s, %s) RETURNING id", (ciudad, provincia))
    conn.commit()
    return cur.fetchone()


def getCiudad(ciudad:str, provincia, connection):
    clean_ciudad = clean_string(ciudad)
    if len(clean_ciudad)< 3:
        clean_ciudad = "Faltante"
    if clean_ciudad == "Faltante" and provincia == None:
        return None
    posiblesCiudades:dict = getCiudadesPorProvincia(provincia, connection)
    if posiblesCiudades.keys().__contains__(clean_ciudad):
        return posiblesCiudades[ clean_ciudad ]
    else:
        return insertarEnCiudad(clean_ciudad, provincia, connection)


def getMediosFromDb(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tipo_medio")
    tipos = {}
    for id, descripcion in cur.fetchall():
        tipos[descripcion] = id
    return tipos


def findClosest(some_string, posibles_strings):
    mas_parecidos = difflib.get_close_matches(some_string, posibles_strings.keys(), 1)
    if len(mas_parecidos) == 0:
        return None
    else:
        return posibles_strings[mas_parecidos.pop()]


def getTipo(tipo_medio, connection: Connection):
    clean_medio = clean_string(tipo_medio)
    if len(clean_medio) < 3:
        return None
    return findClosest(clean_medio, getMediosFromDb(connection))


def getEspecialidadFromDb(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM especialidades")
    tipos = {}
    for id, descripcion in cur.fetchall():
        tipos[descripcion] = id
    return tipos


def getEspecialidad(especialidad, connection):
    clean_especialidad = clean_string(especialidad)
    if len(clean_especialidad) < 3:
        return None
    return findClosest(clean_especialidad, getEspecialidadFromDb(connection))


def insertarMedio(id, nombre, especialidad, tipo,direccion, ciudad_id, conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO medios( nombre, id_especialidad, id_tipo_medio, direccion, id_ciudad) VALUES ( %s, %s, %s, %s, %s)", ( nombre, especialidad, tipo, direccion, ciudad_id))
    conn.commit()


def pasarABd(line, connection):
    provincia = getProvincia(line[Medio.PROV.value], connection)
    ciudad_id = getCiudad(line[Medio.CIUDAD.value], provincia, connection)
    tipo = getTipo(line[Medio.TIPO.value], connection)
    especialidad = getEspecialidad(line[Medio.ESP.value], connection)
    direccion = getDireccion(line)
    insertarMedio(line[Medio.ID.value], line[Medio.NOMBRE.value], especialidad, tipo, direccion, ciudad_id, connection)
    print(line[Medio.ID.value] + " - " + str(provincia) + " - " + str(ciudad_id) + " - " + str(tipo) + " - " + str(especialidad))


def getDireccion(line):
    dir = clean_string(line[Medio.DIR.value])
    if len(dir)<3:
        return None
    return dir


print( "init" )
connection = psycopg2.connect(host=hostname, port=port, user=username, password=password, dbname=database)
with open("files/01-01-Medios.csv", mode="r") as file:
    skippedFirsLine = False
    for line in csv.reader(file, dialect="excel"):
        if skippedFirsLine:
            pasarABd(line, connection)
        else:
            skippedFirsLine=True
connection.close()
print( "end" )
from Concurso import Concurso
from Archivo import Archivo
from PageScratcher import PageScratcher
from Mail import Mail
import time

print "Iniciando el demonio buscador de pasantias para sistemas"

#segundo * minutos * hs * dias = 1 semana en segundos
intervalo = 60 * 60 * 24 * 7

p = PageScratcher()
a = Archivo()

while True:
    # parseo la pagina y saco los concursos
    p.parsearPagina()
    #leo el archivo y obtengo los concursos guardados
    a.leerArchivo()
    #comparo los concursos q hay en la pag con los que tengo en el archivo
    nuevoConcursos = []
    for concursoParseado in p.concursos:
        esta = False
        for concursoLeido in a.concursos:
            if concursoParseado.expediente == concursoLeido.expediente:
                esta=True
        if esta == False:
            nuevoConcursos.append(concursoParseado)

    #guardo los nuevos concursos en el archivo y informo
    if len(nuevoConcursos)>0:
        print "Los nuevos concursos son: "
        for n in nuevoConcursos:
            print "*----      ",n
        a.guardar(nuevoConcursos)
        mail = Mail()
        mail.mandarMail(nuevoConcursos)
    else:
        print "No hay nuevos concursos"
    print 'durmiendo por ', intervalo, ' segundos'
    time.sleep(intervalo)

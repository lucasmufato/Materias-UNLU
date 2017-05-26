# -*- coding: utf-8 -*-
import random
import math

class Cluster:

    def __init__(self, datos, headers, Kclusters):
        self.datos = datos
        self.headers = headers
        self.Kclusters = Kclusters
        #valor para inicializar nomas
        self.silueta = 0
        #cada elemento tiene una lista con los valores del centroide para esa columna
        # centroides[0] = x=1, y=2,5
        # centroides[1] = x=8, y=10
        self.Centroides = []
        for i in range(0, self.Kclusters):
                self.Centroides.append([])
        #cada elemento tiene una lista de los puntos para ese cluster EJ:
        # cluster[0] : a1,a3,a4
        # cluster[1] : a2,a5
        self.distribucionActual = []
        for i in range(0, self.Kclusters):
                self.distribucionActual.append([])
        self.distribucionAnterior = []
        for i in range(0, self.Kclusters):
                self.distribucionAnterior.append([])

    def repartirPuntos(self):
        #este metodo agrega de la manera aleatoria puntos(subindices de los datos)
        #a la cada cluster (cada claster tiene un subindice de la lista de clusters)
        for i in range(0, len(self.datos)):
            x = random.randint(0, self.Kclusters - 1)
            self.distribucionActual[x].append(i)
        print "la matriz con los puntos para cada cluster queda:\n %s \n" % self.distribucionActual
        #si me quedo un cluster sin puntos vuelvo a llamar a la funcion
        #puede fallar
        for i in range(0, self.Kclusters):
            if len(self.distribucionActual[i]) == 0:
                self.repartirPuntos()

    def calcular(self):
        iteraciones = 0
        while self.distribucionActual != self.distribucionAnterior and iteraciones<50:
            self.calcularCentroides()
            self.calcularCluster()
            iteraciones+=1
        print "iteraciones: ",iteraciones

    def calcularCentroides(self):
        print "CALCULO CENTROIDES \n"
        #por cada centroide
        for i in range(0, self.Kclusters):
            print "para el centroide sub %i " % i
            #armo una lista que va a tener el promedio para cada atributo
            promAtr = []
            #inicializo la lista en cero
            for w in range(0, len(self.headers)):
                promAtr.append(0)
            #muestro los puntos asociados a ese cluster
            print "tengo la distribucion %s " % self.distribucionActual[i]
            #for j in range(0, len(self.distribucionActual[i])):
                #print self.datos[ self.distribucionActual[i][j] ]
            #print "\n"
            #por cada subitem perteneciente a ese cluster
            for j in range(0, len(self.distribucionActual[i])):
                #tomo el item EJ: a1 de la lista de datos, dado el subindice que esta
                #en la lista distribucion actual
                dato = self.datos[ self.distribucionActual[i][j] ]
                #por cada atributo de a1 se lo sumo a la lista promAtr ej:
                # a1{x=1,y=2} | promAtr[0] += a1[0]
                for z in range(0, len(self.headers)):
                    #print dato[self.headers[z]]
                    promAtr[z] = promAtr[z] + int(dato[self.headers[z]])
            #ya hice la suma de cada atributo correspondiente al cluster, ahora saco el promedio
            #print "la sumatoria para cada valor es: "
            #print promAtr
            for z in range(0, len(self.headers)):
                promAtr[z] = promAtr[z] / float( len(self.distribucionActual[i]) )
            #tengo el promedio para cada atributo para el centroide [i]
            self.Centroides[i] = promAtr
            print "el promedio le quedo: %s \n" % self.Centroides[i]

    def calcularCluster(self):
        #copio la distribucion actual a la vieja, y limpio la actual
        self.distribucionAnterior = self.distribucionActual
        del self.distribucionActual
        self.distribucionActual = []
        for i in range(0, self.Kclusters):
            self.distribucionActual.append([])
        print "ARMO MATRIZ DE DISTANCIAS \n"
        indice = 0
        #por cada atributo calculo su distancia a cada centroide y lo asigno al centroide con menor dist
        for dato in self.datos:
            distancias = []
            for index in range(0, len(self.Centroides)):
                distancias.append( self.calcularDistancia(dato, self.Centroides[index]) )
            #busco la distancia minima
            minimo = distancias[0]
            indexmin = 0
            for i in range(1, len(distancias)):
                if distancias[i]<minimo:
                    minimo = distancias[i]
                    indexmin = i
            #agrego el dato a la lista de el centroide que dio con la dist menor
            self.distribucionActual[indexmin].append(indice)
            indice += 1
        print "distribucion actual: ", self.distribucionActual
        print "distribucion anterior: ", self.distribucionAnterior

    def getSilueta(self):
        return self.silueta

    def calcularDistancia(self,dato, centroide):
        #distancia de euclides
        distancia = 0.0
        for i in range(0, len(self.headers)):
            resta =float(dato[self.headers[i]]) - centroide[i]
            resta = resta**2
            distancia += resta
        distancia = math.sqrt(distancia)
        print "la distancia entre ", dato," y ",centroide, " es: ",distancia
        return distancia
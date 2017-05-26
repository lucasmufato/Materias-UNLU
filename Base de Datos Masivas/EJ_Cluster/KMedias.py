# -*- coding: utf-8 -*-
from Cluster import Cluster

class KMedias:

    def __init__(self, datos, headers):
        self.datos = datos
        self.headers = headers

    def armarCluster(self, cantCluster, repeticiones):
        self.Kclusters = cantCluster
        self.repeticiones = repeticiones
        #lista de clusters, cada sub-indice tendra el cluster generado
        self.clusters = []
        print "armando clusters: \n"
        for i in range(0, self.repeticiones):
            #hago un nuevo cluster
            cluster = Cluster(self.datos, self.headers, self.Kclusters)
            #le digo q se ponga puntos al azar
            cluster.repartirPuntos()
            #le digo que se encuentre sus centroides
            cluster.calcular()
            #lo guardo en la lista de clusters
            self.clusters.append(cluster)
        #ahora busco el mejor de los clusters en base a su silueta
        self.buscarMejor()
        self.imprimirMejorCluster()

    def buscarMejor(self):
        mejorSilueta = self.clusters[0].getSilueta()
        mejorCluster = self.clusters[0]
        for i in range(0, self.repeticiones):
            silueta = self.clusters[i].getSilueta()
            if(silueta < mejorSilueta):
                mejorSilueta = silueta
                mejorCluster = self.clusters[i]
        self.mejorCluster = mejorCluster

    def imprimirMejorCluster(self):
        #print " El mejor cluster es: \n"
        #print self.mejorCluster
        print "no hay mejor cluster por que no comparo siluetas"


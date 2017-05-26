
library(cluster)
library(fpc)
#punto 5

#para el primer cluster
#armo el cluster
clusters_trigo <- kmeans(x = trigo, centers =3)
summary(clusters_trigo)
#imprimo datos
print(clusters_trigo$centers)
#grafico comprensivo
plotcluster(trigo, clusters_trigo$cluster)
#para sacar la silueta uso:
distancias.ds=dist(trigo, method="euclidean")
silueta_cluster <- silhouette(clusters_trigo$cluster, distancias.ds)
#grafico de silueta
plot(silueta_cluster, col=brewer.pal(3,"Set1"), cex.names=0.7)
#veo mas info de la silueta
summary(silueta_cluster)

#para el punto 6

cluster_encuesta_1 <- kmeans(x=enc, centers = 3)
distancias.enc=dist(enc, method="euclidean")
silueta_encuesta <- silhouette(cluster_encuesta_1$cluster, distancias.enc)
plot(cluster_encuesta_1, col=brewer.pal(3,"Set1"), cex.names=0.7)
#tira error al tener valores nulos

#para el punto 7
dist_tirgo <- dist(trigo, method = "euclidian")
cluster_jerarquico <- hclust(dist_tirgo, method = 'median')
plot(cluster_jerarquico)

diana_trigo <- diana(x = trigo, diss = FALSE, metric = "euclidean")
plot(diana_trigo)

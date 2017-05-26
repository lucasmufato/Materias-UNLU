data(USArrest)
lineal.fit= lm(muerder~assault,USArrest)
plot(lineal.fit$residuals)
#se observa que los residuos no siguen ningun patron

mean(lineal.fit$residuals)

qqnorm(lineal.fit$residuals)
#qq plot tiene que dar como una linea
hist(lineal.fit$residuals)
#el histograma tiene q dar como una campana

#con esto confimamos los supuestos

#TP
#1
#A

llamadas <- llamadas[c(-1)]
names(llamadas)<- c("minutos","reparaciones")
plot(llamadas)

#B
llam.cor <- cor(llamadas)
print(llam.cor)

#C crear la recta de regresion

mediay <- mean(llamadas$X1.1)
mediax <- mean(llamadas$X23)

#para calcular B1
#la parte de arriba de la division
partearriba <- 0
for (i in 1:13) {
  partearriba <- partearriba + ((llamadas[i,3]-mediay)*(llamadas[i,2]-mediax))
}

#la parte de abajo de la division
parteabajo <- 0
for(i in llamadas$X23){
  parteabajo <- parteabajo + (i-mediax)^2
}

b1<- partearriba/parteabajo
b0<- mediay - (b1 * mediax)

print(b1)
#D  a mano lo hago despues
llam.reg <- lm(reparaciones~minutos ,llamadas)
summary(llam.reg)

#E
plot(y=llamadas$reparaciones,x = llamadas$minutos)
abline(llam.reg)

#F
#Suma Cuadratica Total
# SST <- 0
# mediay <- median(llamadas$X1.1)
# for(y in llamadas$X1.1){
#   SST <- SST + ((y - mediay)^2)
# }
# 
# SSM <- 0
# mediay <- median(llamadas$X1.1)
# for(y in llamadas$X1.1){
#   SSM <- SSM + ((y - mediay)^2)
# }

#sino otra opcion usando el COR es:
dfllamadas <- data.frame(reparaciones =llamadas$reparaciones)
prediccionesF <- predict(llam.reg,dfllamadas )
#ahora que tengo los valores predictos para cada valor
#uso la formulaa
R <- (cor(llamadas$X23,prediccionesF) )^2
print(R)
#G
df <- data.frame(X23 =c(160,25,119))
predicciones <- predict(llam.reg,df )
print(predicciones)

#2
#A linealidad
animals <- read.csv("~/Documentos/datos R/tp regresion lineal/ds/02/animals.csv")
#saco el index
animals <- animals[,-c(1)]
an <- animals[-c(33,19),]
plot(an$brain_weight, an$body_weight)
# correlacion
an <- cor(animals)
an
ani.reg <- lm(brain_weight~body_weight ,animals)
summary(ani.reg)
abline(ani.reg)

plot(ani.reg$residuals)

dwtest(formula = ani.reg, data = animals)

#3
plot(machines2)
#saco las variables categoricas
machines2 <- machines[-c(1,2)]
names(machines2) <- c("MYCT","MMIN","MMAX","CACH","CHMIN","CHMAX","PRP")
View(machines2)
machines2.cor
#observo la relacion entre las variables
#B
plot(machines2.log)
#C
#se ve una pequeña relacion entre las variables MMIN y MMAX con la variable objetivo que es PRP
machines2.cor <- cor(machines2)
#hay una relacion entre los datos contra el dato objetivo que es el PRP
#para ver la relacion de mejor manera se aplica una transformacion logaritmica
machines2.log <- log(machines2+1)

#hago la regresion
machines2.reg <- lm(machines2.log$PRP~. , machines2.log)
summary(machines2.reg)
#se puede observar un alto Rcuadrado y un alto Rcuadrado ajustado

#el supuesto de los residuos se cumple ya no siguen un patron
plot(machines2.reg$residuals)
#para independencia de los residuos tengo q hacer dublin watson, me tiene q dar entre 1,5 y 2,5
dwtest(formula = machines2.reg, data = machines)

#normalidad con qqplot y histograma
plot(machines2.reg)
hist(machines2.reg$residuals)


#ejemplo con chartejee
superv <- chatterjee_cap4_supervisors
head(superv)
#hago la regresion multiple
#tambien se puede hacer lm(Y~X1+X2+X3, superv)
fit.lin = lm(Y~., superv)
#modulo para probar el "dublin watson" o algo asi
install.packages("lmtest")

predecir2 <- predecir[,-c(1,2)]
names(predecir2) <- c("MYCT","MMIN","MMAX","CACH","CHMIN","CHMAX")
val_predic <- predict(machines2.reg,predecir2)
val_predic

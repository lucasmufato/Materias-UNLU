#completar el dataset encuesta_universitaria
#utlizo la formula del tp anterior para reemplazar por la media en los atributos que le faltan datos
#primero relleno tiempo de traslado
promedio <- median(encuesta_universitaria$X.Tiempo_Traslado., na.rm = TRUE)
nuevotiempotraslado <- NULL
for(t in encuesta_universitaria$X.Tiempo_Traslado.){
  if(is.null(t) || is.na(t)){
    nuevotiempotraslado <- c(nuevotiempotraslado,promedio)
  }else{
    nuevotiempotraslado <- c(nuevotiempotraslado,t)
  }
}

nueva_encuesta <- encuesta_universitaria
#saco las 2 columanas que voy a modificar
nueva_encuesta <- nueva_encuesta[ -c(5,25)]
#agrego la columna que habia saco sin datos faltantes
nueva_encuesta$X.nuevoTiempoTraslado <- nuevotiempotraslado

#ahora hago lo mismo para cantidad grupo familiar
promedio <- median(encuesta_universitaria$X.Cantidad_Grupo_Familiar., na.rm = TRUE)
nuevotiempotraslado <- NULL
for(t in encuesta_universitaria$X.Cantidad_Grupo_Familiar.){
  if(is.null(t) || is.na(t)){
    nuevotiempotraslado <- c(nuevotiempotraslado,promedio)
  }else{
    nuevotiempotraslado <- c(nuevotiempotraslado,t)
  }
}
nueva_encuesta$X.nuevoCantGrupoFlia <- nuevotiempotraslado

#la guardo
save(nueva_encuesta, file="nueva_encuesta.csv")
#obtengo los valores unico para esa columna
unique(x=nueva_encuesta$X.Grupo_Familiar.)
#reviso si esa columna tiene NA
anyNA(nueva_encuesta$X.Grupo_Familiar.)

#reviso si me quedaron columnas con datos nulos
for(i in 1:33){
  v <- nueva_encuesta[,i]
  print(i)
  resultado<-anyNA(v)
  print(resultado)
}
print(names(nueva_encuesta)[1])
#obtengo los diferentes datos para una columna
for(i in 1:33){
  v <- nueva_encuesta[,i]
  print(" ")
  print(names(nueva_encuesta)[i])
  print(" ")
  u<-unique(v)
  #print(u)
  for(w in u){
    print(w)
  }
}
nueva2 <- nueva_encuesta
write.table(nueva_encuesta, file = "nueva_encuesta.csv", row.names = FALSE, quote = FALSE, sep = ",")

#install.packages("/home/lucas/Descargas/e1071_1.6-7.tar.gz", repos = NULL, type="source")
#fit.bayes= naiveBayes(compra_computadora[] cosito .,pc)
fit.zoo <- zoo[,-c(1)]
zoo.bayes <- naiveBayes(x = fit.zoo,fit.zoo$type)
summary(zoo.bayes)
zoo.bayes$apriori
zoo.bayes$tables
zoo.bayes$call
zoo.bayes$levels

nuevos_animales <- nuevos_animales[,-c(1)]
#predict(modelo que ajuste, dato a predecir)
prediccion <- predict(zoo.bayes,nuevos_animales)
summary(prediccion)
prediccion

# Clase binaria
Entropy <- function(vect_class){
  tbl <- data.frame(table(vect_class))
  p1 <- (tbl[1,]$Freq/length(vect_class))
  p2 <- (tbl[2,]$Freq/length(vect_class))
  E<--p1*log2(p1) - p2*log2(p2)
  if(is.na(E)){
    return(0)
  }else{
    return(E)  
  }
}

InforGain <- function(ds, cla ,att){
  EE <- 0
  Es <- Entropy(ds[[cla]])
  
  for(v in unique(ds[[att]])){
    Sv.S <- length(ds[ds[[att]] ==v,][[cla]])/length(ds[[cla]])
    EE <- EE + Sv.S*Entropy(ds[ds[[att]] ==v,][[cla]]) 
  }
  return(Es - EE)
}


Entropy(ejemplo_playtenis[ejemplo_playtenis$Wind == 'Strong',]$PlayTennis)
Entropy(ejemplo_playtenis[ejemplo_playtenis$Wind == 'Weak',]$PlayTennis)


InforGain(ds, "PlayTennis","Wind")
InforGain(ds, "PlayTennis","Humidity")
InforGain(ds, "PlayTennis","Outlook")

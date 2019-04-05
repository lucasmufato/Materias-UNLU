from tokenizer import tokenizar
linea = """
En el gran instituto de la NASA la Dra. Miriam Roberta y su ayudante Lic. Juan Marcos nacido en E.E.U.U y 
cuyo mail es juan_12marcos@nasa.gov.us.com arman la pagina web http://www.nasa.gov.us.com la cual cuenta con 12.123 lineas de codigo,
250 etiquetas, 6,5 hs de programacion diaria
"""
quim = """
H2O + K2O2 => 2KOH + O
​
Se puede obtener oxígeno por calcinación de bióxido de manganeso y Clorato de potasio.
​
3MnO2 => Mn3O4 + O2
​
ClO3K => KCl + 3O
​
2ClO3K => ClO4K + KCl + O2


O22- + H2O => HO2- + OH-

2O2- + H2O => O2 + HO2- + OH-

"""

tokens = tokenizar(quim)
for t in tokens:
    print(t)



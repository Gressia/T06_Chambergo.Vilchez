#Programa 28
import os
nombre,fecha_actual,fecha_de_nacimiento,Edad="",0.0,0.0,0

#INPUT VIA OS
nombre=os.sys.argv[1]
fecha_actual=float(os.sys.argv[2])
fecha_de_nacimiento=float(os.sys.argv[3])

#PROCESSING
Edad=fecha_actual-fecha_de_nacimiento
# condicion multiples
#Si su edad > 18 ("Es mayor de edad")
if(Edad > 18):
    print("Es mayor de edad")
#Si su edad 15 y 17 ("es menor de edad")
if(Edad >= 15 and Edad <= 17):
    print("es menor de edad")
#Si su edad 0 y 1 ("recien nacido")
if(Edad >= 0  and Edad <= 1  ):
    print("recien nacido")
#fin_if

#Programa 18
import os
nombre,fecha_actual,fecha_de_nacimiento,Edad="",0.0,0.0,0

#INPUT VIA OS
nombre=os.sys.argv[1]
fecha_actual=float(os.sys.argv[2])
fecha_de_nacimiento=float(os.sys.argv[3])

#PROCESSING
#Si su edad >= 18, mostar "Es mayor de edad"
#caso contrario mostrar "es menor de edad"
Edad=fecha_actual-fecha_de_nacimiento
if(Edad >= 18):
    print("Es mayor de edad")
else:
    print("es menor de edad")
#fin_if

#Programa 07
import os
nombre_alumno,nota_1,nota_2,nota_3,promedio="",0,0,0,0

#INPUT VIA OS
nombre_alumno=os.sys.argv[1]
nota_1=int(os.sys.argv[2])
nota_2=int(os.sys.argv[3])
nota_3=int(os.sys.argv[4])
promedio=int(os.sys.argv[5])

#PROCESSING
promedio=nota_1+nota_2+nota_3/3
#Condicion multiple
#Si el promedio >= 14 ("nota aprobatoria")
if(promedio >= 14):
    print("nota aprobatoria")
#Si el promedio <= 13 ("nota aprobatoria baja")
if(promedio <= 13):
    print("nota aprobatoria baja")
#Si el promedio <=10 ("nota desaprobatoria)
if(promedio <= 10):
    print("nota desaprobtoria")
#fin_if

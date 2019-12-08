#Programa 07
import os
nombre_alumno,nota_1,nota_2,nota_3="",0,0,0

#INPUT VIA OS
nombre_alumno=os.sys.argv[1]
nota_1=int(os.sys.argv[2])
nota_2=int(os.sys.argv[3])
nota_3=int(os.sys.argv[4])

#PROCESSING
#Si el promedio supera 14, mostrar "nota aprobatoria"
#Caso contrario mostrar "nota desaprobatoria"
if(promedio > 14 ):
    print(promedio, "nota aprobatoria")
else:
    print(promedio,"nota desaprobatoria")
#fin_if

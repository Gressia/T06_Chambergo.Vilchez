#Programa 03
import os
alumno,horas_dedicadas_al_estudio_por_dia="",0

#INPUT VIA OS
alumno=os.sys.argv[1]
horas_dedicadas_al_estudio_por_dia=int(os.sys.argv[2])

#PROCESSING
#Si el numero de horas supera 7, mostrar "buen rendimiento academico"
if(horas_dedicadas_al_estudio_por_dia > 7 ):
    print(alumno, "buen rendimiento academico")
#fin_if

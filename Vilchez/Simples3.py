# Programa 03
import os
alumno,horas_dedicadas_al_estudio_por_dia,total_de_horas_por_semana="",0,0.0

#INPUT VIA OS
alumno=os.sys.argv[1]
horas_dedicadas_al_estudio_por_dia=int(os.sys.argv[2])

#PROCESSING
#Si el total de horas por semana es menor 30, mostrar "Bajo rendimiento academico"
total_de_horas_por_semana=(horas_dedicadas_al_estudio_por_dia)*7
if(total_de_horas_por_semana < 30):
    print("Bajo rendimiento academico")
#Fin_if

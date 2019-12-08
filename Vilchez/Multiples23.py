# Programa 23
import os
alumno,horas_dedicadas_al_estudio_por_dia,total_de_horas_por_semana="",0,0.0

#INPUT VIA OS
alumno=os.sys.argv[1]
horas_dedicadas_al_estudio_por_dia=int(os.sys.argv[2])

#PROCESSING
total_de_horas_por_semana=(horas_dedicadas_al_estudio_por_dia)*7

# condicion multiple
#Si el total de horas por semana es mayor 48 ("Buen rendimiento academico")
if(total_de_horas_por_semana > 48):
    print("Buen rendimiento academico")
#Si el total de horas de estudio por semana 28 y 42 ("Bajo rendimiento academico)
if( total_de_horas_por_semana >= 28 and total_de_horas_por_semana <= 42 ):
    print("Bajo rendimiento academico")
#Si el total de horas de estudio por semana 14 y 21 ("pesimo rendimiento academico")
if( total_de_horas_por_semana >= 14 and total_de_horas_por_semana <= 21 ):
    print("pesimo rendimiento academico")
#fin_if

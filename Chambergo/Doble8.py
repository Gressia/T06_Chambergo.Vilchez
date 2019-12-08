#Programa 08
import os
trabajador,horas_de_jornada_laboral_por_dia,dias_de_jornada_laboral="",0,0

#INPUT VIA OS
trabajador=os.sys.argv[1]
horas_de_jornada_laboral_por_dia=int(os.sys.argv[2])
dias_de_jornada_laboral=int(os.sys.argv[3])

#PROCESSING
#Si el total de horas por semana supera 40, mostrar "cumplimiento de horas de trabajo"
#Caso contrario mostrar "incumplimiento de horas de trabajo"
if(total > 40 ):
    print(trabajador, "cumplimiento de horas de trabajo")
else:
    print(trabajador,"incumplimiento de horas de trabajo")
#fin_if

#Programa 08
import os
trabajador,horas_de_jornada_laboral_por_dia,dias_de_jornada_laboral,total="",0,0,0

#INPUT VIA OS
trabajador=os.sys.argv[1]
horas_de_jornada_laboral_por_dia=int(os.sys.argv[2])
dias_de_jornada_laboral=int(os.sys.argv[3])
total=int(os.sys.argv[4])

#PROCESSING
total=horas_de_jornada_laboral_por_dia*dias_de_jornada_laboral
#Condicion multiple
#Si total de jornada laboral >= 40 ("cumplimiento de horas de trabajo")
if(total >= 40):
    print ("cumplimiento de horas de trabajo")
#Si total de jornada laboral <= 35 ("cumplimiento moderado de horas de trabajo")
if(total <= 35):
    print("cumplimiento moderado de horas de trabajo")
#Si total de jornada laboral <= 30 ("incumplimiento de horas de trabajo")
if(total <= 30):
    print("incumplimiento de horas de trabajo")
#fin_if

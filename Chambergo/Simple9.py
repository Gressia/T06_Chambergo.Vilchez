#Programa 09
import os
nombre,horas_dedicadas_a_la_television_por_dia,horas_dedicadas_a_la_television_por_semana="",0,0

#INPUT VIA OS
nombre=os.sys.argv[1]
horas_dedicadas_a_la_television_por_dia=int(os.sys.argv[2])
horas_dedicadas_a_la_television_por_semana=int(os.sys.argv[3])

#PROCESSING
#Si las horas por semana supera 60, mostrar "adiccion a la tv"
if(horas_dedicadas_a_la_television_por_semana > 60 ):
    print(nombre, "adiccion a la tv")
#fin_if

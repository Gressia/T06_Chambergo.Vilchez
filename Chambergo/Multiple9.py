#Programa 09
import os
nombre,horas_dedicadas_a_la_television_por_dia,horas_dedicadas_a_la_television_por_semana,total_horas="",0,0,0

#INPUT VIA OS
nombre=os.sys.argv[1]
horas_dedicadas_a_la_television_por_dia=int(os.sys.argv[2])
horas_dedicadas_a_la_television_por_semana=int(os.sys.argv[3])
total_horas=int(os.sys.argv[4])

#PROCESSING
#Condicion multiple
#Si total de horas >= 60 ("adiccion a la tv")
if(total_horas >= 60):
    print("adiccion a la tv")
#Si total de horas <= 30 ("uso moderado de la tv")
if(total_horas <= 30):
    print("uso moderado de la tv")
#Si total de horas <= 10 ("no ve mucha tv")
if(total_horas <= 10):
    print("no ve mucha tv")
#fin_if

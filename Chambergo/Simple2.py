#Programa 02
import os
usuario,cant_de_horas_por_dia="",0

#INPUT VIA OS
usuario=os.sys.argv[1]
cant_de_horas_por_dia=int(os.sys.argv[2])

#PROCESSING
#Si el numero de horas supera 12, mostrar "adiccion a las redes sociales"
if(cant_de_horas_por_dia > 12 ):
    print(usuario, "adiccion a las redes sociales")
#fin_if

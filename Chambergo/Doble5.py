#Programa 05
import os
nombre,deporte,cant_horas_diarias="","",0

#INPUT VIA OS
nombre=os.sys.argv[1]
deporte=str(os.sys.argv[2])
cant_horas_diarias=int(os.sys.argv[3])

#PROCESSING
#Si la cantidad de horas supera 5, mostrar "inclinacion al deporte"
#Caso contrario mostrar "disgusto por el deporte"
if(cant_horas_diarias > 5 ):
    print(nombre, "inclinacion al deporte")
else:
    print(nombre,"disgusto por el deporte")
#fin_if

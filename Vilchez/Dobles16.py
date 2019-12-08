#Programa 16
import os
nombre,profesion,edad,tiempo_de_trabajo="","",0,""

#INPUT VIA OS
nombre=os.sys.argv[1]
profesion=os.sys.argv[2]
edad=int(os.sys.argv[3])
tiempo_de_trabajo=os.sys.argv[4]

#PROCESSING
#Si su profesion es Doctor and su tiempo de trabajo es igual 2 años, mostrar "Nombrado"
# caso contrario mostrar "
if(profesion=="Doctor")and(tiempo_de_trabajo=="24meses"):
    print("Nombrado")
else:
    print("CAS")
#fin_if

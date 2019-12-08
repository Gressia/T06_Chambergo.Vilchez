#Programa 26
import os
nombre,profesion,edad,tiempo_de_trabajo="","",0,""

#INPUT VIA OS
nombre=os.sys.argv[1]
profesion=os.sys.argv[2]
edad=int(os.sys.argv[3])
tiempo_de_trabajo=os.sys.argv[4]

#PROCESSING
# condicion multiple
#Si su profesion es Doctor and su tiempo de trabajo es igual 24meses ("Nombrado")
if(profesion=="Doctor")and(tiempo_de_trabajo=="24meses"):
    print("Nombrado")
# si su profesion es abogado and su tiempo de trabajo es igual 18meses ("CAS")
if(profesion=="abogado")and(tiempo_de_trabajo=="18meses"):
    print("CAS")
#si su profesion es contador and su tiempo de trabajo es igual a 14meses ("independiente")
if(profesion=="contador")and(tiempo_de_trabajo=="14meses"):
    print("independiente")
#fin_if

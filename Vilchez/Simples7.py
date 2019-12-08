# Programa 07
import os
paciente,tipo_de_atencion,edad,pago_consulta="","",0,""

#INPUT VIA OS
paciente=os.sys.argv[1]
tipo_de_atencion=os.sys.argv[2]
edad=int(os.sys.argv[3])
pago_consulta=os.sys.argv[4]

#PROCESSING
# Si su atencion es particular and si pago consulta, mostrar "No tiene SIS"
if(tipo_de_atencion=="Particular")and(pago_consulta=="Si"):
    print("No tiene SIS")
#fin_if

# Programa 27
import os
paciente,tipo_de_atencion,edad,pago_consulta="","",0,""

#INPUT VIA OS
paciente=os.sys.argv[1]
tipo_de_atencion=os.sys.argv[2]
edad=int(os.sys.argv[3])
pago_consulta=os.sys.argv[4]

#PROCESSING
#condicion multiple
# Si su atencion es particular and si pago consulta ("No tiene SIS")
if(tipo_de_atencion=="Particular")and(pago_consulta=="Si"):
    print("No tiene SIS")
# si su atencion es por SIS anda si no pago consulta ("Tiene SIS")
if(tipo_de_atencion=="SIS")and(pago_consulta=="No"):
    print("Tiene SIS")
# si su atencion es por ESsalud and si pago consulta ("Tinene ESsalud")
if(tipo_de_atencion=="ESsalud")and(pago_consulta=="Si"):
    print("Tiene ESsalud")
#fin_if

#Programa 12
import os
empleado,nrodias,costo,horas_extra,total="",0,0.0,0,0.0

# INPUT VIA OS
empleado=os.sys.argv[1]
nrodias=int(os.sys.argv[2])
costo=float(os.sys.argv[3])
horas_extra=int(os.sys.argv[4])

# PROCESSING
# Si el salario supera 1500, mostrar "salario"
# caso contrario mostrar "salario minimo"
Total=(nrodias*costo)+(horas_extra*10)
if( Total > 1500):
    print("salario")
else:
    print("salario minimo")
#fin_if

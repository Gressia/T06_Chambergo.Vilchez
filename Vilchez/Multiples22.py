#Programa 22
import os
empleado,nrodias,costo,horas_extra,total="",0,0.0,0,0.0

# INPUT VIA OS
empleado=os.sys.argv[1]
nrodias=int(os.sys.argv[2])
costo=float(os.sys.argv[3])
horas_extra=int(os.sys.argv[4])

# PROCESSING
Total=(nrodias*costo)+(horas_extra*10)

# condicion multiple
# Si el salario supera 1500 ("salario" )
if( Total > 1500):
    print("salario")
#Si el salario 1200 y 1500 ("salario minimo")
if( Total >= 1200 and Total <= 1500 ):
    print("salario minimo")
#Si el producto 900 y 1000 ("pago por horas")
if( Total >= 700  and Total <= 1000 ):
    print("pago por horas")
#fin_if


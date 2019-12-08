#Programa 06
import os
cliente,producto,cant_producto,costo_total="","",0,0.0

#INPUT VIA OS
cliente=os.sys.argv[1]
producto=str(os.sys.argv[2])
cant_producto=int(os.sys.argv[3])
costo_total=float(os.sys.argv[4])

#PROCESSING
#Si el costo no supera 50, mostrar "comprador pasivo"
if(costo_total < 50 ):
    print(producto, "costo total")
#fin_if

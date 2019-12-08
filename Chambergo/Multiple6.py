#Programa 06
import os
cliente,costo_producto,cant_producto,costo_total="",0.0,0,0.0

#INPUT VIA OS
cliente=os.sys.argv[1]
costo_producto=float(os.sys.argv[2])
cant_producto=int(os.sys.argv[3])
costo_total=float(os.sys.argv[4])

#PROCESSING
costo_total=cant_producto*costo_producto
#Condicion multiple
#Si el costo total >= 500 ("comprador compulsivo")
if(costo_total >= 500):
    print("comprador compulsivo")
#Si el costo total <= 300 ("comprador pasivo")
if(costo_total <= 300):
    print("comprador pasivo")
#Si el costo total >= 100 ("comprador cauteloso")
if(costo_total <= 100):
    print("comprador cauteloso")
#fin_if

#Programa 04
import os
producto,costo_producto="",0.0

#INPUT VIA OS
producto=os.sys.argv[1]
costo_producto=float(os.sys.argv[2])

#PROCESSING
#Si el producto supera 200, mostrar "buena calidad"
if(costo_producto > 200 ):
    print(producto, "buena calidad")
#fin_if

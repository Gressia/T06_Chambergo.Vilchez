#Programa 04
import os
producto,precio_unit_de_producto,cantidad_de_producto="",0.0,0

#INPUT VIA OS
producto=os.sys.argv[1]
precio_unit_de_producto=float(os.sys.argv[2])
cantidad_de_producto=int(os.sys.argv[3])

#PROCESSING
total=precio_unit_de_producto*cantidad_de_producto
#Condicion multiple
#Si el total es >= 300 ("buena calidad")
if(total >= 300):
    print("buena calidad")
#Si el total es <= 200 ("calidad media")
if(total <= 200):
    print("calidad media")
#Si el total es <= 80 ("mala calidad")
if(total <= 80):
    print("mala calidad")
#fin_if


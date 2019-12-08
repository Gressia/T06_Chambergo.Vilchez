# Programa 01
import os
producto,costo_Uni="",0.0

#INPUT VIA OS
producto=os.sys.argv[1]
costo_Uni=float(os.sys.argv[2])

#PROCESSING
#Si el producto supera 300, mostrar "marca original"
if(costo_Uni > 300 ):
    print(producto, "marca original")
#fin_if


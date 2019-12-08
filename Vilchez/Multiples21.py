# Programa 21
import os
producto,costo_Uni="",0.0

#INPUT VIA OS
producto=os.sys.argv[1]
costo_Uni=float(os.sys.argv[2])

#PROCESSING
#condicion multiple
#Si el producto supera 300 ("marca original")
if( costo_Uni > 300 ):
    print(producto, "marca original")
#Si el producto 200 y 300 ("marca figuratica")
if( costo_Uni >= 200 and costo_Uni <= 300 ):
    print(producto, "marca figurativa")
#Si el producto 80 y 135
if(costo_Uni >= 80 and costo_Uni <=135):
    print(producto, "marca mixta")
#fin_if


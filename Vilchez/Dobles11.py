# Programa 11
import os
producto,costo_Uni="",0.0

#INPUT VIA OS
producto=os.sys.argv[1]
costo_Uni=float(os.sys.argv[2])

#PROCESSING
#Si el producto supera 300, mostrar "marca original"
# caso contrario mostrar "Replica"
if(costo_Uni > 300 ):
    print(producto, "marca original")
else:
    print(producto, "Replicas")

#fin_if

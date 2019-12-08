#Programa 15
import os
cliente,producto,cant,costo,total="","",0,0.0,0.0

#INPUT VIA OS
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
cant=int(os.sys.argv[3])
costo=float(os.sys.argv[4])

#PROCESSING
# Si el total supera 400, mostar "comprador compulsivo"
# caso contrario mostrar "comprador normal"
total=cant*costo
if(total > 400):
    print("comprador compulsivo")
else:
    print("comprador normal")
#fin_if

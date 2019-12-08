#Programa 05
import os
cliente,producto,cant,costo,total="","",0,0.0,0.0

#INPUT VIA OS
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
cant=int(os.sys.argv[3])
costo=float(os.sys.argv[4])

#PROCESSING
# Si el total supera 400, mostar "comprador compulsivo"
total=cant*costo
if(total > 400):
    print("comprador compulsivo")
#fin_if

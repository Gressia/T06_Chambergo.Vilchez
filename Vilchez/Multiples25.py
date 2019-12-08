#Programa 25
import os
cliente,producto,cant,costo,total="","",0,0.0,0.0

#INPUT VIA OS
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
cant=int(os.sys.argv[3])
costo=float(os.sys.argv[4])

#PROCESSING
total=cant*costo
#condicion multiple
# Si el total supera 400 ("comprador compulsivo")
if(total > 400):
    print("comprador compulsivo")
# si el total 200 y 300 ("comprador normal")
if(total >= 200 and total <= 300 ):
    print("comprador normal")
#Si el total 50 y 120 ("misio")
if(total >= 50 and total <= 120 ):
    print("misio")
#fin_if

#Programa 29
import os
jefe_de_unidad,cargo,costo,nro_faltas,descuento="","",0.0,0,0

#INPUT VIA OS
jefe_de_unidad=os.sys.argv[1]
cargo=os.sys.argv[2]
costo=float(os.sys.argv[3])
nro_faltas=int(os.sys.argv[4])

#PROCESSING
descuento=costo*nro_faltas
#condicon multiple
#Si el descuento supera 500 ("Dejar el cargo")
if(descuento > 500):
    print("Dejar el cargo")
#si el descuento supera 700 ("vacaciones sin pagar")
if(descuento > 700):
    print("vacaciones sin pagar")
#Si no falto <= 0 ("continuar con su cargo")
if(descuento <= 0):
    print("continuar con su cargo")
#fin_if

#Programa 09
import os
jefe_de_unidad,cargo,costo,nro_faltas,descuento="","",0.0,0,0

#INPUT VIA OS
jefe_de_unidad=os.sys.argv[1]
cargo=os.sys.argv[2]
costo=float(os.sys.argv[3])
nro_faltas=int(os.sys.argv[4])

#PROCESSING
#Si el descuento supera 500, mostar "Dejar el cargo"
descuento=costo*nro_faltas
if(descuento > 500):
    print("Dejar el cargo")
#fin_if


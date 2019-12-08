#Programa 10
import os
promotores,precio_entrada_al_concierto_pre_venta,nro_entradas_vendidas,total_recaudado_de_la_pre_venta="",0,0,0

#INPUT VIA OS
promotores=os.sys.argv[1]
precio_entrada_al_concierto_pre_venta=int(os.sys.argv[2])
nro_entradas_vendidas=int(os.sys.argv[3])

#PROCESSING
# Si el total recaudado de la pre venta es igual o pasa 7000, mostar "Vivo por el Rock"
total_recaudado_de_la_pre_venta=precio_entrada_al_concierto_pre_venta*nro_entradas_vendidas
if(total_recaudado_de_la_pre_venta >= 7000):
    print("Vivo por el Rock")
#fin_if

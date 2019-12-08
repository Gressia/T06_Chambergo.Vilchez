#Programa 30
import os
promotores,precio_entrada_al_concierto_pre_venta,nro_entradas_vendidas,total_recaudado_de_la_pre_venta="",0,0,0

#INPUT VIA OS
promotores=os.sys.argv[1]
precio_entrada_al_concierto_pre_venta=int(os.sys.argv[2])
nro_entradas_vendidas=int(os.sys.argv[3])

#PROCESSING
total_recaudado_de_la_pre_venta=precio_entrada_al_concierto_pre_venta*nro_entradas_vendidas
# condicion multiple
# Si el total recaudado de la pre venta es igual o pasa 19000  ("Vivo por el Rock","platinum")
if(total_recaudado_de_la_pre_venta >= 19000):
    print("Vivo por el Rock","platinum")
# si el total recaudado  de la pre venta 9000 y 12000 ("Vivo por el Rock","vip")
if(total_recaudado_de_la_pre_venta >= 9000 and total_recaudado_de_la_pre_venta <= 12000):
    print("Vivo por el rock","vip")
#Si el total recaudado de la pre venta 5000 y 7000 ("Vivo por el Rock","general")
if(total_recaudado_de_la_pre_venta >= 5000 and total_recaudado_de_la_pre_venta <= 7000 ):
    print("Vivo por el rock","general")
#fin_if

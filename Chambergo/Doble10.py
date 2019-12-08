#Programa 10
cliente,horas_dedicadas_al_gimnasio_por_dia,horas_dedicadas_al_gimnasio_por_semana="",0,0

#INPUT VIA OS
cliente=os.sys.argv[1]
horas_dedicadas_al_gimnasio_por_dia=int(os.sys.argv[2])
horas_dedicadas_al_gimnasio_por_semana=int(os.sys.argv[3])

#PROCESSING
#Si el numero de horas por semana supera 50, mostrar "adiccion al gimnasio"
#Caso contrario mostrar "visita moderada al gimnasio"
if(total > 50 ):
    print(cliente, "adiccion al gimnasio")
else:
    print(cliente,"visita moderada al gimnasio")
#fin_if

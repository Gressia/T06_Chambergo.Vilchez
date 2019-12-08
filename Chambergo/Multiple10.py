#Programa 10
cliente,horas_dedicadas_al_gimnasio_por_dia,horas_dedicadas_al_gimnasio_por_semana,total_horas="",0,0,0

#INPUT VIA OS
cliente=os.sys.argv[1]
horas_dedicadas_al_gimnasio_por_dia=int(os.sys.argv[2])
horas_dedicadas_al_gimnasio_por_semana=int(os.sys.argv[3])
total_horas=int(os.sys.argv[4])

#PROCESSING
total_horas=horas_dedicadas_al_gimnasio_por_dia*horas_dedicadas_al_gimnasio_por_semana
#Condicion multiple
#Si total de horas >= 50 ("adiccion al gimnasio")
if(total_horas >= 50):
    print("adiccion al gimnasio")
#Si total de horas <= 30 ("visita moderada al gimnasio")
if(total_horas <= 30):
    print("visita moderada al gimnasio")
#Si total de horas <=10 ("visita normal al gimnasio")
if(total_horas <= 10):
    print("visita normal al gimnasio")
#fin_if

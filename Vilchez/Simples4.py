# Programa 04
import os
alumno,nota1,nota2,nota3,nota4="",0,0,0,0

#INPUT VIA OS
alumno=os.sys.argv[1]
nota1=int(os.sys.argv[2])
nota2=int(os.sys.argv[3])
nota3=int(os.sys.argv[4])
nota4=int(os.sys.argv[5])

#PRECESSING
# Si el promedio es mayor a 15, mostar "aprobado"
prom=(nota1+nota2+nota3+nota4)/4
if(prom > 15):
    print("aprobado")
#fin_if

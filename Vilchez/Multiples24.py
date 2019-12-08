# Programa 24
import os
alumno,nota1,nota2,nota3,nota4="",0,0,0,0

#INPUT VIA OS
alumno=os.sys.argv[1]
nota1=int(os.sys.argv[2])
nota2=int(os.sys.argv[3])
nota3=int(os.sys.argv[4])
nota4=int(os.sys.argv[5])

#PRECESSING
prom=(nota1+nota2+nota3+nota4)/4
# condicion multiple
# Si el promedio es mayor a 18 ("aprobado")
if(prom > 18):
    print("aprobado")
# si el promedio 15 y 17 ("Recuperacion")
if(prom >= 15 and prom <= 17 ):
    print("Recuperacion")
# si el promedio 10 y 11 ("desaprobado")
if(prom >= 10 and prom <= 11 ):
    print("desaprobado")
#fin_if

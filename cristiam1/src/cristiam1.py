# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Alumno"
__date__ = "$14/10/2015 10:17:19 AM$"

print("elige el menu" )
print("1.ARCHIBO")
print("2.BUSCAR")
print("3.SALIR")
opcion=input ("elegir la opcion:")

if opcion>3:
    print("opcion incorrecta:")

    
if opcion<4:
 datos={ 1: "estas en los archivos"}
 datos={2:"usted busco bien"}
 datos={3:"usted deseas salir"}
 resultado = datos[opcion]
 print resultado
    


print("----------------------------------------------")
print("                   MENU ")
print("   1) archivo\n   2) buscar\n   3) salir")
print("----------------------------------------------")




valor = input ("Ingrese la opcion:" )

if valor>3:
    print("opcion incorrecta")

if valor<4:
 datos = { 1: "  --> usted entro a los archivos", 2: "  --> usted busco correctamente", 3: "  --> saliendo de los archivos" }
 resultado = datos[valor]
 print resultado
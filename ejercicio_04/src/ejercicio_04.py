import math  
op1=float(input("ingresa el primer operador:\n"))  
op2=float(input("ingresa el segundo operador:\n"))  
print("Seleccione una operacion:\n")
print("------------------------------")
print("1) Suma:")  
print("2) Resta:")  
print("3) Multiplicacion:")  
print("4) Division:")  
print("5) Potencia:")  
print("6) Raiz cuadrada operador:")  
print("7) Inversa Operador:")  
print("8) Cuadrado de operador:")  
print("9) Modulo:")  
print("10) Valor negativo de Operador:")  
print("------------------------------")
fun=int(input())  
if(fun==1):  
 print(op1+op2)  
if(fun==2):  
 print(op1-op2)  
if(fun==3):  
 print(op1*op2)  
if(fun==4):  
 if(op2==0):  
  print("no se puede dividir entre cero")  
 else:  
  print(op1/op2)   
if(fun==5):  
 print(pow(op1,op2))  
if(fun==6):  
 print(sqrt(op1))  
if(fun==7):  
 if(op1==0):  
  print("no se puede dividir entre cero")  
 else:  
  print(1/op1)  
if(fun==8):  
 print(pow(op1,2))  
if(fun==9):  
 print(int(op1%op2))   
if(fun==10):  
 print((-1)*op1) 
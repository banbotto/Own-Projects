#Calculadora en Python

#Opciones:
#(1) Suma
#(2) Resta
#(3) Multiplicación
#(4) División


def calculadora(op, num1, num2):
    print("Bienvenido a la calculadora hecha en Python".center(50,"-"))
    if op == 1:
        return(f"El resultado de la suma de {num1} mas {num2} es: {num1 + num2}")
    elif op == 2:
        return(f"El resultado de la resta de {num1} menos {num2} es: {num1 - num2}")
    elif op == 3:
        return(f"El resultado de la multiplicación de {num1} por {num2} es: {num1 * num2}")
    elif op == 4:
        return(f"El resultado de la división de {num1} entre {num2} es: {num1 / num2}")
    else:
        return("Opción no válida")

variable 1 = int(input("Ingrese el primer valor: "))
variable 2 = int(input("Ingrese el segundo valor: "))

print (calculadora(1, variable 1, variable 2))
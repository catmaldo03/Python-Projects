print("Hola, esto es una calculadora basica en Python")
print("Por favor, introduce dos numeros para realizar una operacion")
#Se pide los dos numeros y se pasan a float
num1 = input("Introduce el primer numero: ")
num1 = float(num1)
num2 = input("Introduce el segundo numero: ")
num2 = float(num2)
#print que indican las operaciones que se pueden realizar
print("Eliga una operacion: ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
#Lo convierte en un int  que lo pasa en un if para realizar una operacion
operacion = input("Introduce el numero de la operacion: ")
operacion = int(operacion)
if operacion == 1:
    print("El resultado de la suma es: ", num1 + num2)
elif operacion == 2:
    print("El resultado de la resta es: ", num1 - num2)
elif operacion == 3:
    print("El resultado de la multiplicacion es: ", num1 * num2)
elif operacion == 4:
    if num2 == 0: #se asegura que no se divida por 0
        print("No se puede dividir entre 0")
    else:
        print("El resultado de la division es: ", num1 / num2)
else:
    print("Operacion no valida")
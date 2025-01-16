import random
print("Este es un juego para adivinar numeros")
print("Se le indicara si el numero ingresado es mayor, menor o igual al numero a adivinar")
print("El numero a adivinar esta entre 1 y 1000")
random_num=random.randint(1,1000)
atempt = 0
print("Ingrese el numero")
user_num=int(input())
atempt+=1
while(user_num!=random_num):
    if user_num>random_num:
        print("El numero es mayor que el numero a adivinar")
    else:
        print("El numero es menor que el numero a adivinar")
    print("Ingrese otro numero")
    user_num=int(input())
    atempt+=1
print("Felicidades, ha adivinado el numero")
print("Sus intentos fueron:",atempt)
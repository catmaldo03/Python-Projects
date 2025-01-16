import random
import string
print("Hola, la idea de este programa es generar una contraseña, segun tus necesidades")
print("1. Ingresa el largo de la contraseña")
print("2. Tamaño al azar entre 8 y 16 caracteres")
option = int (input())
if option == 1:
    password_length = int(input())
elif option == 2:
    password_length = random.randint(8,16)
else:
    print("Opcion no valida")
    exit()
print("¿Que tipo de caracteres necesita?")
print("1. Letras Minusculas")
print("2. Letras Mayusculas")
print("3. Numeros")
print("4. Simbolos")
print("5. Toda la contraseña al azar")
password_characters=[]
a= 0
while a < password_length:
    print("Ingrese el numero de la opcion que necesita")
    option = int(input())
    if option == 1:
        password_characters.append(random.choice(string.ascii_lowercase))
    elif option == 2:
        password_characters.append(random.choice(string.ascii_uppercase))
    elif option == 3:
        password_characters.append(random.choice(string.digits))
    elif option == 4:
        password_characters.append(random.choice(string.punctuation))
    elif option == 5:
        b = 0
        while b < password_length:
            password_characters.append(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation))
            b +=1
        break
    else:
        print("Opcion no valida")
        exit()
    a +=1

password_characters = ''.join(password_characters)
print("Tu contraseña es: ", password_characters)

import random

from more_itertools.more import rstrip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Evaluación de seguridad al ingreso:
if nr_symbols == 0 or nr_letters == 0 or nr_numbers == 0:
    print("Atención: Una contraseña segura incluye números, símbolos y letras.")
elif nr_symbols + nr_letters + nr_numbers < 8:
    print("Atención: Una contraseña segura debe tener mas de 8 caracteres.")
else:
    print(f"Entonces vamos a generar una passwd de {nr_letters} letras, {nr_symbols} símbolos y {nr_numbers} números...\n" )
    #Inicializo una lista para después hacer append al final:
    passwd = []
    # #Voy a hacer nr_letters búsquedas aleatorias dentro de la lista letters:
    for _ in range(nr_letters):
         passwd.append(random.choice(letters))
    # Voy a hacer nr_symbols búsquedas aleatorias dentro de la lista symbols:
    for _ in range(nr_symbols):
        passwd.append(random.choice(symbols))
    #     passwd = passwd + (random.choice(symbols))
    # # Voy a hacer nr_numbers búsquedas aleatorias dentro de la lista numbers:
    for _ in range(nr_numbers):
        passwd.append(random.choice(numbers))
    #     passwd = passwd + (random.choice(numbers))
    #
    # Imprimo lista passwd, pero primero shuffleo
    random.shuffle(passwd)
    #print(f"Tu passwd será :\n\n{passwd}") <<< Comentado por mejora
    # print (str(passwd) [1:-1].replace(",", "").replace("'","".replace(" ",""))) <<< Estrambótico y no funciona
    for letra in passwd:
        print (letra, end="")

    diccionario_de_passw_malas = ['123456', 'abcdefg', 'password', 'constraseña','abretesesamo', '654321','qwerty','1029384756']
    seguridad = int(0)
    password_str = "".join(passwd)

    for palabra in diccionario_de_passw_malas:
        if palabra == password_str:
           seguridad += 1
    if seguridad > 0:
       print("Atención: La seguridad de la contraseña está comprometida y se recomienda cambiarla ahora mismo.")




# [x] Armar un to-do con líneas comentadas y tildes de "Realizado" de alguna forma
# [x] Shuflear cada categoría
# [x] Shufflear la passwd Completa
# [x] No permitir el ingreso de nada que no sea números <<< Resuelto por int. Se podría meter en un while pero todavía no lo estudiamos
# [x] Evaluación de seguridad previa a la generación según recomendaciones actuales (6 caracteres, al menos un numero,letra y simbolo).
# [x] Evaluación de seguridad después de shufflear contra un diccionario.
# [x] Corregido bug al hacer comparación con or == 0 individual vs x 3






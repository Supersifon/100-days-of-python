print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bienvenida a la isla del tesoro.")
print("Tu misión será encontrar el TESORO!!!")
izq_o_der = input("Llegaste a una isla desconocida... Girás a la izq o a la der ? :")
if izq_o_der == "der":
    nadar_o_esperar = input("Encontrás un lago pestilente. Cruzás nadando o esperás a ver si te vienen a buscar en bote? (nadar / esperar) ")
    if nadar_o_esperar == "nadar":
        que_choza = input("Ves tres cuevas al pie de una montaña. Cada una vigilada por un animal diferente. A cuál de ellos te vas a enfrentar? (mono / serpiente / aguila) ")
        if que_choza == "mono":
            print("El mono se rinde ante tu poder y te deja entrar a la cueva. Felicitaciones!!! Encontraste el tesoro!")
        elif que_choza == "serpiente":
            print("La serpiente se abalanza rápidamente. Estás perdida... \n Game Over")
        else:
            print("El águila sacude sus alas y levanta vuelo. De la cueva sale un olor terrible que hacer perder el sentido... \n Game Over")
    else:
        print("Esperás hasta que cae la noche. MALA IDEA \n GAME OVER")
else:
    print("Sentís un golpe en la cabeza. Los caníbales te invitan a cenar. \n Game Over - Juego Terminado")




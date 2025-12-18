import random
while True:
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    # defino la lista:
    rps = ["rock", "paper", "scissors"]
    # Hago un sorteo y lo dejo guardado.
    computer = random.choice(rps)
    # Dejo que el usuario elija y también queda guardado.
    # noinspection PyTypeHints
    eleccion = int(input("Qué elegís?: ?  0 para piedra, 1 papel, 2 tijera: \n"))
    persona = rps[eleccion]

    # Imprimo elecciones:
    print ("computadora eligió: \n")
    if computer == "rock":
        print (rock)
    elif computer == "paper":
        print(paper)
    else:
        print(scissors)

    print ("\nusuario eligió: \n")
    if persona == "rock":
        print (rock)
    elif persona == "paper":
        print(paper)
    else:
        print(scissors)
    # defino ganador:
    if persona == computer:
        print("Es un empate... :o|")
    elif persona == "paper" and computer == "rock" or persona == "rock" and computer == "scissors" or persona == "scissors" and computer == "paper":
        print(" G A N A S T E ! :oD")
    else:
        print("P E R D I S T E :o( ")


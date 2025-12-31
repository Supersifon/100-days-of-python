import random
import time
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player1 = {
    "Nombre": "Dealer",
    "Puntos": 0,
    "Carta 1": 0,
    "Carta 2": 0
}
player2 = {
    "Nombre": "Diego",
    "Puntos": 0,
    "Carta 1": 0,
    "Carta 2": 0
}
def espera(texto,name_user):
    print(f"{texto} {name_user}", end="", flush=True)
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

def estado(player):
    print(f"\nJugador:  {player["Nombre"]}")
    player["Puntos"] = 0
    for key in player:
        if key.startswith("Carta"):
            print(f"{key}: {player[key]}")
            player["Puntos"] += int(player[key])

    print(f"Puntos : {player["Puntos"]}")

def shuffle_and_deal(player, cards):
    """Mezclar el mazo, dar 2 cartas a player"""

    name_user = (player["Nombre"])
    espera("\nMezclando el maso y repartiendo 2 cartas a", name_user)
    random.shuffle(cards)
    player["Carta 1"] = cards[0]
    player["Carta 2"] = cards[1]

def hit(player, cards):
    """ La idea es dar una carta a player (dealer es un player)
    Se mezcla el mazo nuevamente y tomo la primer carta"""
    name_user = (player["Nombre"])
    espera("\nMezclar el mazo y dar una carta a", name_user)
    random.shuffle(cards)
    cant_cartas = 0
    for key in player:
        if key.startswith("Carta"):
            cant_cartas += 1
    nueva_carta = cant_cartas + 1
    player[f"Carta {nueva_carta}"] = cards[0]

wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
while wanna_play == "y":

    print(logo)

    player1 = {
        "Nombre": "Dealer",
        "Puntos": 0,
        "Carta 1": 0,
        "Carta 2": 0
    }

    player2 = {
        "Nombre": "Montoto",
        "Puntos": 0,
        "Carta 1": 0,
        "Carta 2": 0
    }

    player2["Nombre"] = input("Dígame su nombre: ")
    print("=" * 40)
    print(f"\nHola {player2["Nombre"]} Te enfrentarás a Dealer. Estás preparad@?")
    time.sleep(1)
    shuffle_and_deal(player1, cards)
    time.sleep(1)
    estado(player1)
    shuffle_and_deal(player2, cards)
    time.sleep(1)
    estado(player2)
    time.sleep(3)

    otra_carta = "y"

    while otra_carta == "y" and player2["Puntos"] <= 21:
        otra_carta = input (f"\n{player2["Nombre"]}, desea otra carta? ['y' or 'n']").lower()
        if otra_carta == "y":
            hit(player2, cards)
            estado(player1)
            estado(player2)
            time.sleep(2)
        else:
            break

    if player2["Puntos"] > 21:
        print(f"{player2["Nombre"]} se pasó de 21!!!")
        ganador = player1["Nombre"]
        print(f"\nEl ganador es {ganador}!!!")
        wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
        continue

    print(f"\nTurno de {player1["Nombre"]}")
    time.sleep(3)
    while player1["Puntos"] < 17:
        print(f"\n{player1["Nombre"]}, desea otra carta?: ")
        time.sleep(1)
        print(f" Y")
        hit(player1, cards)
        estado(player1)
        estado(player2)
        time.sleep(2)
    print(f"\n{player1["Nombre"]}, desea otra carta?: ")
    time.sleep(1)
    print(f"\n{player1["Nombre"]} dice: No mas cartas para mí...")

    ganador = None
    if player1["Puntos"] > 21:
        print(f"\n{player1["Nombre"]} se pasó de 21!!!")
        ganador = player2["Nombre"]
    elif player1["Puntos"] >= player2["Puntos"]:
        ganador = player1["Nombre"]
    else:
        ganador = player2["Nombre"]

    print(f"\nEl ganador es {ganador}!!!")

    wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
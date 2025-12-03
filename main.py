import random
import time
import os
"""from nicegui import ui

ui.label('Hello NiceGUI!')

ui.run()"""

game = True

deck1 = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
        ]
deck2 = [

                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
            ]

while game == True:

    card1 = random.choice(deck1)
    card2 = random.choice(deck2)

    deck1.remove(card1)
    deck2.remove(card2)

    #os.system('cls')
    print("Cards in deck 1: ", len(deck1))
    print("Cards in deck 1: ", len(deck2))

    print("Drawing cards...\n")
    time.sleep(1)

    print("Player 1: ", card1)
    print("Player 2: ", card2)
    print("")
    time.sleep(1)

    if card1 > card2:
        print("Player 1 wins!")
        deck1.append(card1)
        deck1.append(card2)
    elif card2 > card1:
        print("Player 2 wins!")
        deck2.append(card1)
        deck2.append(card2)
    else:
        print("Tie!")

    time.sleep(1)
    #os.system('cls')

    print("Cards in deck 1: ", len(deck1))
    print("Cards in deck 2: ", len(deck2))

    print(deck1)
    print(deck2)
    print("")
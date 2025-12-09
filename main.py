import random
import time
import os

"""from nicegui import ui

ui.label('Hello NiceGUI!')

ui.run()"""

# Add a test for multiple face-offs
# Add logging for error checking/statistic gathering, export it to database
# Add a gui

game = True
tie = False

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

def draw_cards(deck1, deck2):
    card1 = random.choice(deck1)
    card2 = random.choice(deck2)

    deck1.remove(card1)
    deck2.remove(card2)
    os.system('cls')

    return card1, card2

def print_message(card1, card2, deck1, deck2):
    print("Cards in deck 1: ", len(deck1))
    print("Cards in deck 2: ", len(deck2))
    print("Drawing cards...\n")
    time.sleep(1)
    print("Player 1: ", card1)
    print("Player 2: ", card2)
    print("")
    time.sleep(1)

def decide_winner(card1, card2, deck1, deck2):
    if card1 > card2:
        print("Player 1 wins!")
        deck1.append(card1)
        deck1.append(card2)
    elif card2 > card1:
        print("Player 2 wins!")
        deck2.append(card1)
        deck2.append(card2)
    else:
        print("Tie! Time to face off!")
        tie = True
        pot1.append(card1)
        pot2.append(card2)
        print(deck1)
        print(deck2)
        print("Press any key to continue: ")
        x = input()
        face_off(tie, deck1, deck2, pot1, pot2)

def face_off(tie, deck1, deck2, pot1, pot2):
    while tie == True:
        for x in range(0, 3):
            card1, card2 = draw_cards(deck1, deck2)
            pot1.append(card1)
            pot2.append(card2)

        print("")
        print("Pot 1: ", pot1)
        print("Pot 2: ", pot2)
        time.sleep(3)

        card1, card2 = draw_cards(deck1, deck2)

        print("")
        print("And the winner is...")
        time.sleep(3)
        print("Player 1: ", card1)
        print("Player 2: ", card2)

        if card1 > card2:
            print("Player 1!")
            deck1.append(card1)
            deck1.append(card2)
            deck1.extend(pot1)
            deck1.extend(pot2)
            print("Deck 1: \n", deck1)
            print("Deck 1: \n", deck2)
            print("Press any key to continue: ")
            x = input()
            tie = False
            pot1.clear(), pot2.clear()
            return tie, deck1, deck2, pot1, pot2

        elif card2 > card1:
            print("Player 2!")
            deck2.append(card1)
            deck2.append(card2)
            deck2.extend(pot1)
            deck2.extend(pot2)
            print("Deck 1: \n", deck1)
            print("Deck 1: \n", deck2)
            print("Press any key to continue: ")
            x = input()
            time.sleep(5)
            tie = False
            pot1.clear(), pot2.clear()
            return tie, deck1, deck2, pot1, pot2
        
        else:
            continue

while game == True:

    # Check win condition

    """if len(deck1) or len(deck2) == 0:
        game == False
        print("Game over!")
        time.sleep(1)
        break """
    
    pot1 = []
    pot2 = []

    card1, card2 = draw_cards(deck1, deck2)
    print_message(card1, card2, deck1, deck2)
    decide_winner(card1, card2, deck1, deck2)

    

    time.sleep(1)
    os.system('cls')

    print("Cards in deck 1: ", len(deck1))
    print("Cards in deck 2: ", len(deck2))

    print(deck1)
    print(deck2)
    print("")



import os
from re import S 
import time
import ascii_assets as ascii

def shuffle_deck():
    global deck, evaluation
    
    deck = []
    
    values = []
    evaluation = []
    
    suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
    
    cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    for suit in suits:
        for card in cards:
            deck.append(card + ' of ' + suit)
            values.extend([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 10, 10, 10, 11])
            
    card_evaluation = dict(zip(deck, values))
    print(card_evaluation)

    return deck
def __init__():
    shuffle_deck()

if __name__ == "__main__":
    __init__()
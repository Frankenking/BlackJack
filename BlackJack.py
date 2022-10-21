import os
import time
import ascii_assets as ascii
import random

def clear():
    os.system('cls')
    
def hit():
    card = deck[random.randint(0,len(deck)-1)]
    card_remove = deck.index(card)
    deck.pop(card_remove)
    return(card)


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
    for suit in suits:        
        values.extend([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 10, 10, 10, 11])
            
    card_evaluation = dict(zip(deck, values))


def __init__():
    shuffle_deck()
    
if __name__ == "__main__":
    __init__()
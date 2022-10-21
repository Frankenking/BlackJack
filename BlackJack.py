###############################
# Artyom Curtis
# BlackJack.py
# 10/20
# Version 1.0.0
###############################


import os
import time
import ascii_assets as ascii
import random
def breakf():
    pass
def pause():
    os.system('pause')

def clear():
    os.system('cls')
    
def hit():
    card = deck[random.randint(0,len(deck)-1)]
    card_index = deck.index(card)
    deck.pop(card_index)
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
            
    evaluation = dict(zip(deck, values))


def __Game__():
    global player_cards, dealer_cards, player_cards_value, dealer_cards_value

    player_cards = []
    dealer_cards = []
    
    player_cards_value = []
    dealer_cards_value = []

    for _ in range(2):
        card = hit()
        player_cards.append(card)
    for _ in range(2):
        card = hit()
        dealer_cards.append(card)
    
    player_cards_value = [evaluation.get(pcards) for pcards in player_cards]
    dealer_cards_value = [evaluation.get(dcards) for dcards in dealer_cards]
    breakf()
def __Set__():
    
    global money, pot_money

    shuffle_deck()
    
    print("Welcome To BlackJack, Made by Artyom Curtis Version {}".format(version))
    pause()
    clear()

    print(ascii.black_jack)
    pause()
    clear()
    
    print(ascii.settings)
    money = int(input("Please Input the Money to Start With:\n"))
    clear()

    pot_money = int(input("Money to Put into Pot:\n"))
    money -= pot_money
    print("Money In Pot: {}\n Money In Balance: {}".format(pot_money, money))
    pause()
    clear()

if __name__ == "__main__":
    version = '1.0.0'
    __Set__()
    __Game__()

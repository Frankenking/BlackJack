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


def ace_check(entryhand, cardsvalue):
    pass


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

def Win_scenario():
    if total_dcard > 21 and total_pcard <= 21:
        print("Dealer Bust! {}, You Win!, {}".format(total_dcard, total_pcard))
    elif total_pcard > 21:
        print("You Bust.. {}, Dealer Wins!, {}".format(total_pcard, total_dcard))
    elif total_pcard > total_dcard:
        print("You Win!, {}".format(total_pcard))
    else:
        print("Dealer Wins, {}".format(total_dcard))
    breakf()
def Optional(x):

    x = x.lower()

    if x in hlist:
        print('hitlist')
        card = hit()
        player_cards.append(card)
        print("Player Drew assumming hit")
        if total_dcard <= 16:
            card = hit()
            dealer_cards.append(card)
            print("Dealer Drew assuming hit or stand")
        return True
    elif x in slist:
        print('slist')
        if total_dcard <= 16:
            card = hit()
            dealer_cards.append(card)
            print("Dealer Drew assuming hit or stand")

        return False
    else:
        print("Invalid Option")
        
    print(dealer_cards, player_cards)
def __Game__():
    global player_cards, dealer_cards, player_cards_value, dealer_cards_value, total_dcard, total_pcard

    stand = True
    total_pcard = int()
    total_dcard = int()

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
    
    player_cards_value = ([evaluation.get(pcards) for pcards in player_cards])
    dealer_cards_value = ([evaluation.get(dcards) for dcards in dealer_cards])

    [int(elements) for elements in player_cards_value]
    [int(elements) for elements in dealer_cards_value]
    

    for element in range(0, len(player_cards_value)):
        total_pcard = total_pcard + player_cards_value[element]

    for element in range(0, len(dealer_cards_value)):
        total_dcard = total_dcard + dealer_cards_value[element]


    clear()
    print("The Dealer Deals you a {0}".format(*player_cards))
    pause()

    print("To Himself a {0}".format(*dealer_cards))
    pause()

    print("Back to you a {1}".format(*player_cards))
    pause()

    print("Back to Himself a Unkown Card".format())
    pause()

    print("This Gives you a hand worth {} and him a hand worth at least {}".format(total_pcard, dealer_cards_value[0]))
    pause()
    clear()
    
    print(total_dcard, total_pcard)


    while stand:
            trigger = bool()
            x = str(input("Would you like to Hit/Stand:\n"))
            stand = bool(Optional(x))


            player_cards_value = ([evaluation.get(pcards) for pcards in player_cards])
            dealer_cards_value = ([evaluation.get(dcards) for dcards in dealer_cards])
            [int(elements) for elements in player_cards_value]
            [int(elements) for elements in dealer_cards_value]
            
            for i in range(1):
                
                if stand == True:

                    for element in range(2 + i, len(player_cards_value)):
                        total_pcard += player_cards_value[element]
                

                if total_pcard >= 21:
                    print("Hit was over 21 failure")
                    trigger = True
                    stand = False
                    Win_scenario()
                else:
                    for element in range(2 + i, len(dealer_cards_value)):
                        total_dcard += dealer_cards_value[element]
                        
                        if total_dcard >= 21:
                            print("Hit was over 21 failure")
                            trigger = True
                            stand = False
                            Win_scenario()
                i += 1

                print(total_dcard, total_pcard)

    if trigger == False and stand == False:
        Win_scenario()

    breakf()


def __Set__():
    
    global money, pot_money, hlist, slist

    hlist = ('h', 'hit')
    slist = ('s', 'stand')

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

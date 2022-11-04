###############################
# Artyom Curtis
# BlackJack.py
# 10/20
# Version 1.0.0
###############################

#I didnt comment anything and the efficency is garbage it's also overcomplicated 💀

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
    global deck, evaluation, aces
    
    deck = []
    
    values = []
    evaluation = []
    
    suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
    
    cards = ['1', '2', '3','4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    for suit in suits:
        for card in cards:
            deck.append(card + ' of ' + suit)
    for suit in suits:        
        values.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])
            
    evaluation = dict(zip(deck, values))

def Win_scenario():
    if total_dcard > 21 and total_pcard <= 21:
        print("Dealer Bust! {}, You Win!, {}".format(total_dcard, total_pcard))
        win = True
    elif total_pcard > 21:
        print("You Bust.. {}, Dealer Wins!, {}".format(total_pcard, total_dcard))
        win = False
    elif total_pcard > total_dcard:
        print("You Win!, {}".format(total_pcard))
        win = True
    elif total_pcard == total_dcard:
        print("Tie!")
        win = None
    else:
        print("Dealer Wins, {}".format(total_dcard))
        win = False

    return win

def Optional(x):

    if x in hlist:
        print('You Hit')
        card = hit()
        player_cards.append(card)
        print("You Drew: ", card)
        if total_dcard <= 16:
            card = hit()
            dealer_cards.append(card)
            print("Dealer Drew a Unkown Card")
        return True
    elif x in slist:
        print('You Stand')
        if total_dcard <= 16:
            card = hit()
            dealer_cards.append(card)
            print("Dealer Drew a Unkown Card")

        return False
        

def __Game__(money):

    global player_cards, pot_money, dealer_cards, player_cards_value, dealer_cards_value, total_dcard, total_pcard, hlist, slist, ylist



    stand = True
    total_pcard = int()
    total_dcard = int()

    player_cards = []
    dealer_cards = []
    
    player_cards_value = []
    dealer_cards_value = []

    ylist = ('y', 'yes')
    hlist = ('h', 'hit')
    slist = ('s', 'stand')

    shuffle_deck()
    

    print(ascii.black_jack)
    pause()
    clear()
    try:
        pot_money = int(input("Money to Put into Pot:\n"))
    except:
        print("Invalid Input")
        pause()
        return __Game__(money)

    if pot_money > money:
            print("You dont have that Money!")
            pause()
            return __Game__(money)
    elif pot_money <= 0:
            print("Invalid Amount")
            pause()
            return __Game__(money)
        
    money -= pot_money
    print("Money In Pot: {}\n Money In Balance: {}".format(pot_money, money))
    pause()
    clear()
    
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


    #fix stuff below this
    while stand:
            trigger = bool()
        
            x = str(input("Would you like to Hit/Stand:\n"))
            x = x.lower()
            if x  in hlist or x in slist:
                stand = bool(Optional(x))
                

                player_cards_value = ([evaluation.get(pcards) for pcards in player_cards])
                dealer_cards_value = ([evaluation.get(dcards) for dcards in dealer_cards])
                
                [int(elements) for elements in player_cards_value]
                [int(elements) for elements in dealer_cards_value]
                
                for i in range(1):
                    
                    if stand:

                        for element in range(2 + i, len(player_cards_value)):
                            total_pcard += player_cards_value[element]
                            
                                
                                
                        if total_pcard >= 21:
                            trigger = True
                            stand = False
                            win = Win_scenario()
                        
                    else:
                        
                        for element in range(2 + i, len(dealer_cards_value)):
                            total_dcard += dealer_cards_value[element]
                            
                        
                        if total_dcard >= 21:
                            trigger = True
                            stand = False
                            win = Win_scenario()
                        
                    i += 1

                
            else:
                raise Exception("Invalid Option")


    if trigger == False and stand == False:
        win = Win_scenario()
    
    if money != 0:
        if win == True:
            money += pot_money * 2
            pot_money = 0
        elif win == None:
            money += pot_money
            pot_money = 0
        elif win == False:
            pot_money = 0
    elif pot_money != 0:
        if win == True:
            money += pot_money * 2
            pot_money = 0
        elif win == None:
            money += pot_money
            pot_money = 0
        elif win == False:
            pot_money = 0
    else:
        print("You Lost All Your Money :( Better Luck Next Time")
        pause()
    
    print("You have {}$ left".format(money))
    x = input("Play Again? Y/N")
    x = x.lower()
    if x in ylist:
        clear()
        return __Game__(money)
    
    else:
        print("You Ended The Game With {}".format(money))

    
    breakf()
def __Setting__():
    print(ascii.settings)
    try:
        money = int(input("Money To Start With: "))
    except:
        print("Invalid Option")
        return __Setting__()
    
    __Game__(money)
    
if __name__ == "__main__":
    
    version = '1.0.0'
    
    print("Welcome To BlackJack, Made by Artyom Curtis Version {}".format(version))
    pause()
    clear()
    __Setting__()
    
            
    

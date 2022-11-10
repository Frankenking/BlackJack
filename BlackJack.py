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

#FUNCTIONS

def breakf():
    pass

        #invokes a pause in the console
def pause():
    os.system('pause')

    #clears the console
def clear():
    os.system('cls')

        #this function chooses a card from the deck and returns it back then removes it from the deck
def hit():
    card = deck[random.randint(0,len(deck)-1)]
    card_index = deck.index(card)
    deck.pop(card_index)
    return(card)

        #this function shuffles the deck by making a dictionary and an array containg all cards in a full deck
def shuffle_deck():
    global deck, evaluation
    
    deck = []
    
    values = []
    evaluation = []
    
    suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
    
    cards = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']
    
    for suit in suits:
        for card in cards:
            deck.append(card + ' of ' + suit)

    for suit in suits:        
        values.extend([1,2,3,4,5,6,7,8,9,10,10,10,10,11]) #applys values to each entry
            
    evaluation = dict(zip(deck, values)) #makes the dict


        #caculates the winner and returns it dcard is dealer card p card is playercard, pretty easy to look out
def Win_scenario(total_pcard, total_dcard):
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

    #decided what to do based on the input of stand/hit
def Optional(x):

    if x in hlist:

        print('You Hit')
        card = hit()
        player_cards.append(card) #adds the hit card to your hand and then decideds if the dealer should draw or not
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



        #MAIN GAME FUNC
def __Game__(money, stand, total_dcard, total_pcard, pot_money) -> None:
    
    print("You have", total_pcard)
    #while the player doesn't choose stand 
    while stand:
        
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
                            if player_cards_value[element] == 11 and total_pcard > 21:
                                    print('ace p')
                                    total_pcard += -10
                                    player_cards_value[element] = 1

                        if total_pcard > 21:
                            stand = False
                        
                    else:
                        
                        for element in range(2 + i, len(dealer_cards_value)):
                            total_dcard += dealer_cards_value[element]

                            if dealer_cards_value[element] == 11 and total_dcard > 21:
                                    print('ace d')
                                    total_pcard += -10
                                    dealer_cards_value[element] = 1

                        if total_dcard > 21:
                            stand = False
                        
                    print("You have", total_pcard)
                    i += 1

                
            else:
                print("Invalid Option")
                pause()
                clear()
                return __Game__(money, stand, total_dcard, total_pcard)

    print("Your Cards Were {}".format(player_cards))
    print("His Cards Were {}".format(dealer_cards))
    win = Win_scenario(total_pcard, total_dcard)
    
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
    
    if money != 0:
        print("You have {}$ left".format(money))
        x = input("Play Again? Y/N")
        x = x.lower()
        if x in ylist:
            clear()
            return __Initial__(money)
        
        else:
            print("You Ended The Game With {}$".format(money))
    else:
        print("You Lost All Your Money :( Better Luck Next Time")
        pause()
    
    breakf()
def __Initial__(money) -> None:

    global pot_money
    stand = True

    global total_dcard, total_pcard
    total_pcard = int()
    total_dcard = int()

    global player_cards, dealer_cards
    player_cards = []
    dealer_cards = []
    
    global player_cards_value, dealer_cards_value
    player_cards_value = []
    dealer_cards_value = []

    global ylist, hlist, slist
    ylist = ('y', 'yes')
    hlist = ('h', 'hit')
    slist = ('s', 'stand')

    shuffle_deck()
    

    print(ascii.black_jack)
    pause()
    clear()

        #if someone inputs a invalid data type it returns an error and sends you back
    try:
        pot_money = int(input("Money to Put into Pot:\n"))
    except:
        print("Invalid Input")
        pause()
        return __Initial__(money)

        #if you try to enter an amount you dont have or otherwise it returns and error
    if pot_money > money:
            print("You dont have that Money!")
            pause()
            return __Initial__(money)
    elif pot_money <= 0:
            print("Invalid Amount")
            pause()
            return __Initial__(money)
        
        #tells you your money
    money -= pot_money
    print("Money In Pot: {}\n Money In Balance: {}".format(pot_money, money))
    pause()
    clear()
    
        #for 2 times the player and the dealer draws 2 cards
    for _ in range(2):
        card = hit()
        player_cards.append(card)
    for _ in range(2):
        card = hit()
        dealer_cards.append(card)
    
    
        #applies the dictionary to your cards into a new variable through a comprehension 
    player_cards_value = ([evaluation.get(pcards) for pcards in player_cards])
    dealer_cards_value = ([evaluation.get(dcards) for dcards in dealer_cards])

    # converts to type int
    [int(elements) for elements in player_cards_value]
    [int(elements) for elements in dealer_cards_value]

        #adds the total of the new list
    for element in range(0, len(player_cards_value)):
        total_pcard = total_pcard + player_cards_value[element]

        if player_cards_value[element] == 11 and total_pcard > 21:
                print('ace p')
                total_pcard += -10
                player_cards_value[element] = 1

    for element in range(0, len(dealer_cards_value)):
        total_dcard = total_dcard + dealer_cards_value[element]

        if dealer_cards_value[element] == 11 and total_dcard > 21:
                print('ace d')
                total_pcard += -10
                dealer_cards_value[element] = 1
        
        #tells what the dealer has and what you have

    print("The Dealer Deals you a {0}".format(*player_cards))
    pause()

    print("To Himself a {0}".format(*dealer_cards))
    pause()

    print("Back to you a {1}".format(*player_cards))
    pause()

    print("Back to Himself a Unkown Card")
    pause()

    print("This Gives you a hand worth {} and him a hand worth at least {}".format(total_pcard, dealer_cards_value[0]))
    pause()
    clear()

    clear()
        #starts the rest of the game
    __Game__(money, stand, total_dcard, total_pcard, pot_money)

def __Setting__():
    print(ascii.settings)
    try:
        money = int(input("Money To Start With: "))
    except:
        print("Invalid Option")
        return __Setting__()
    
    __Initial__(money)
    
if __name__ == "__main__":
    
    version = '1.0.0'
    
    print("Welcome To BlackJack, Made by Artyom Curtis Version {}".format(version))
    pause()
    clear()
    __Setting__()
    
            
    

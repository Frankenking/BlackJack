print("""
Made by Artyom Curtis
10/17/22
BlackJack.py
""")



    #packages
import ascii_assets as ascii
import random
import os
import time

def clear():
    os.system('CLS')

#Picking a card from the avaliable length of the list storing it then finding the index of it and removing it
def draw(current_deck):
    card = current_deck[random.randint(0,len(current_deck)-1)]
    card_remove = current_deck.index(card)
    current_deck.pop(card_remove)
    return(card)

def black_jack():
    os.system('pause')

def round2(current_deck, Dcard1_value):
    player_input = str(input("What would you like to do?:\n (Hit, Stand, Or Double Down) "))
    player_input = player_input.lower()
    if player_input in hitList or player_input in ddList:
        card = draw(current_deck)
        player_cards.append(card)
        
        Pcard1, Pcard2, Pcard3 = player_cards
        
        Pcard1_value = card_evaluation.get(Pcard1)
        Pcard2_value = card_evaluation.get(Pcard2)
        Pcard3_value = card_evaluation.get(Pcard3)
        
        total_Pcard_value = Pcard1_value + Pcard2_value + Pcard3_value
        
        if player_input in ddList:
            global double_down
            double_down = True
        
        if Dcard1_value <= 16:
            card = draw(current_deck)
            dealer_cards.append(card)
            
            Dcard1, Dcard2 = dealer_cards
            
            Dcard1_value = card_evaluation.get(Dcard1)
            Dcard2_value = card_evaluation.get(Dcard2)
            
            total_Dcard_value = Dcard1_value + Dcard2_value
        print()
    elif player_input in standList:
        if Dcard1_value <= 16:
            card = draw(current_deck)
            dealer_cards.append(card)

            Pcard1, Pcard2 = player_cards
            Dcard1, Dcard2 = dealer_cards
            
            Dcard1_value = card_evaluation.get(Dcard1)
            Dcard2_value = card_evaluation.get(Dcard2)
            
            total_Dcard_value = Dcard1_value + Dcard2_value

            print("You stand with your {} and {} the dealer draws again and reveals his cards to be a {} and a {}".format(Pcard1, Pcard2, Dcard1, Dcard2))
    black_jack()
def round1(current_deck):
    
    clear()
    try:
        print(ascii.money)
        
        #valid boundries check
        print("Your Money: ", starting_money)
        pot_money = int(input("How Much Would you like to put in the pot: "))
        if pot_money > starting_money or pot_money < 0:
            print("You cant put that much in")
            return(0)
    except:
        print("Invalid Data Type Please input Integer")
        return setting()
    clear()
    global player_cards, dealer_cards, Dcard1_value, total_Pcard_value, Pcard1, Pcard2

    player_cards = []
    dealer_cards = []
    
    #manual draws
    for _ in range(2):
        card = draw(current_deck)
        player_cards.append(card)
        
    card = draw(current_deck)
    dealer_cards.append(card)
    
    #to strings
    Pcard1, Pcard2 = player_cards
    Dcard1 = ''.join(dealer_cards)
    
    #total using dict keys
    Pcard1_value = card_evaluation.get(Pcard1)
    Pcard2_value = card_evaluation.get(Pcard2)
    total_Pcard_value = Pcard1_value + Pcard2_value
    
    Dcard1_value = card_evaluation.get(Dcard1)
    
    print("The dealer deals you a ", Pcard1)
    time.sleep(1)
    print("Then himself a", Dcard1)
    time.sleep(1)
    print("Then back to you a", Pcard2)
    time.sleep(1)
    print("You have a {} the Dealer has a {} this totals to you having {} in total and him {}".format(Pcard1 + ' and a ' + Pcard2, Dcard1, total_Pcard_value, Dcard1_value))
    os.system("pause")
    
    round2(current_deck, Dcard1_value)
    
        
def deck_generator():
        #deck maker
    card = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suit = ["Spades", "Hearts", "Clubs", "Diamonds"]
    
    card_values = []
    deck = []
    global card_evaluation
    for i in suit:
        for ii in card:
            card_values.extend([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
            deck.append(ii + 'of' + i)
          
          #making a global Dictonary using the deck and their corresponding values  
    card_evaluation = dict(zip(deck, card_values))
    

    return(deck)

    #player input settings
def setting():
    
    print(ascii.settings)
    
    current_deck = deck_generator()
    
    #tuple option
    global hitList, ddList, standList

    hitList = ('h', 'hit', 'deal', 'dealme', 'deal me')
    ddList = ('dd', 'doubledown', 'double down', 'all in')
    standList = ('s', 'stand')
    
    try:
        #starting money input
        global starting_money
        starting_money = int(input("Starting Money: "))
    except:
        print("Invalid Data Type Please Input a Integer")
    round1(current_deck)
    
    
if __name__ == "__main__":
    
    print("Thank You For Playing my BlackJack Game Version 1.0.0 Build")
    os.system("pause")
    clear()
    
    print(ascii.black_jack)
    os.system("pause")
    clear()
    
    setting()
    
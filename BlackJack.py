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

def phase2(current_deck):
    player_input = str(input("What would you like to do?:\n (Hit, Stand, Or Double Down) "))
    player_input = player_input.lower()
    #phase 3
        ################################################################
    
    
def game(current_deck):
    
    clear()
    print(ascii.money)
    
    #valid boundries check
    print("Your Money: ", starting_money)
    pot_money = int(input("How Much Would you like to put in the pot: "))
    if pot_money > starting_money or pot_money < 0:
        print("You cant put that much in")
        return(0)
    
    global player_cards, dealer_cards, total_Pcard_value, Dcard1_value

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
    
    #total
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
    
    phase2(current_deck)
    
        
def deck_generator():
        #deck maker
    card = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suit = ["Spades", "Hearts", "Clubs", "Diamonds"]
    
    card_values = []
    deck = []
    global card_evaluation
    for i in suit:
        for h in card:
            card_values.extend([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
            deck.append(h + 'of' + i)
          
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
    
    #starting money input
    global starting_money
    starting_money = int(input("Starting Money: "))
    
    game(current_deck)
if __name__ == "__main__":
    
    print("Thank You For Playing my BlackJack Game Version 1.0.0 Working Build")
    os.system("pause")
    clear()
    
    print(ascii.black_jack)
    os.system("pause")
    clear()
    
    setting()
    
###############################
# Artyom Curtis
# BlackJack.py
# 10/20
# Version 1.0.0
###############################


#MODULES
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

        #this function shuffles the deck by making an array containing all cards in a full deck
def shuffle_deck():
    global deck
    
    deck = []
    
    suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
    
    cards = ['1','2','3','4','5','6','7','8','9','Ten','J','Q','K','A']
    
    for suit in suits:
        for card in cards:
            deck.append(card + ' of ' + suit)
            

        #evaluates the given number/face and returns the corresponding value
def evaluator(element):
    match element[0]:
        case '1':
            return 1
        case '2':
            return 2
        case '3':
            return 3
        case '4':
            return 4
        case '5':
            return 5
        case '6':
            return 6
        case '7':
            return 7
        case '8':
            return 8
        case '9':
            return 9
        case 'T':
            return 10
        case 'J':
            return 10
        case 'Q':
            return 10
        case 'K':
            return 10
        case 'A':
            return 11
        
        #the game
def __Game__(money):
    
    shuffle_deck()
    
    #GAME VARIABLES
    optionValues = ['s', 'stand', 'h', 'hit']
    againValues = ['n', 'no', 'y', 'yes']
    player_hand = []
    dealer_hand = []
    player_hand_num = int()
    dealer_hand_num = int()

    player_hand_string = str()
    dealer_hand_string = str()
    
    #Prompts for money No Cheating!
    pot_money = int(input("Money to Put into Pot:\n"))
    if pot_money < 0 or pot_money > money:
        print("Cheaters Never Prosper")
        pause()
        raise Exception("Begone!")
    money -= pot_money
    
    print("Your Balance: {}$\n Money in the Pot: {}$".format(money, pot_money))
    pause()
    clear()
    
    #deals 2 cards and increments 'i' by 1 to print the next item in list
    i = 0
    for i in range(2):
        player_hand.append(hit())   #adds to hand
        print("You Recived a", player_hand[i])
        time.sleep(1)
        dealer_hand.append(hit())
        if i == 0:  
            print("The Dealer Recived a", dealer_hand[0])
        else:
            print("The Dealer Recived an Unkown Card")
        i += 1
        time.sleep(1)
    
        #for every card in your hand and dealer hand it is added to a numerical total that then is adjusted for aces
    for element in player_hand:
            element = evaluator(element)    #evlautes the card and adds it to a new variable
            player_hand_num += element
            if player_hand_num > 21 and element == 11:
                print("Fixed For Ace")
                element = -10
                player_hand_num += element
               
    print("You Have, ",player_hand_num)
    
    for element in dealer_hand:
            element = evaluator(element)
            dealer_hand_num += element
            if dealer_hand_num > 21 and element == 11:
                element = -10
                dealer_hand_num += element
    
    #repeats until both dealer and you stand or someone busts
    
    while True:
        
        #prompts for user input to stand/hit the rest of the code is the same as above just looped
            option = input("Stand or Hit:\n")
            option = option.lower()
            
            if option not in optionValues[:2]: #gets the first two values for ''hit
                
                player_hand.append(hit())
                element = player_hand[len(player_hand)-1]
                
                element = evaluator(element)
                player_hand_num += element
            
                if player_hand_num > 21 and element == 11:
                    element = -10
                    player_hand_num += element
                    
                elif player_hand_num > 21:
                    break
                
                
                print("You Recived a", player_hand[i]) #i = card most recent
                print("You Now Have, ",player_hand_num)
                i += 1
                if dealer_hand_num <= 16:
                        
                    dealer_hand.append(hit())
                    element = dealer_hand[len(dealer_hand)-1]
                        
                    element = evaluator(element)
                    dealer_hand_num += element
                        
                    if dealer_hand_num > 21 and element == 11:
                        element = -10
                        dealer_hand_num += element
                    elif dealer_hand_num > 21:
                        break
                    
                print("The Dealer Drew")
                
            elif dealer_hand_num <= 16:
                        
                dealer_hand.append(hit())
                element = dealer_hand[len(dealer_hand)-1]
                        
                element = evaluator(element)
                dealer_hand_num += element
                        
                if dealer_hand_num > 21 and element == 11:
                    element = -10
                    dealer_hand_num += element
                elif dealer_hand_num > 21:
                    break
                
                print("The Dealer Drew")
            else:
                break
            clear()
            
        #makes a neat string value of all cards to be revealed at the end of the game
    for i in player_hand:
        player_hand_string += i+ ', '
        
    for i in dealer_hand:
        dealer_hand_string += i+ ', '
        
        #the winning conditions simple math
    if player_hand_num > 21:
        print("You Lose, you had {} The dealer had {} You lost {}$".format(player_hand_string, dealer_hand_string, pot_money))
        pot_money = 0
        
    elif dealer_hand_num > 21:
        print("You Win, you had {} The dealer had {} You win {}$".format(player_hand_string, dealer_hand_string, pot_money))
        money += pot_money + pot_money
        
    elif player_hand_num < dealer_hand_num:
        print("You Lose, you had {} The dealer had {} You lost {}$".format(player_hand_string, dealer_hand_string, pot_money))
        pot_money = 0
        
    else:
        print("You Win, you had {} The dealer had {} You win {}$".format(player_hand_string, dealer_hand_string, pot_money))
        money += pot_money + pot_money
        
        
        #displays hand values
    print(player_hand_num,' Vs. ',dealer_hand_num)
    
    
        #prompts to play again or if they dont have money then no entry
    again = input("Play again? Y/N:\n")
    again = again.lower()
    
    if again not in againValues[:2] and money > 0: #gets the first two items and make sure money is > 0
        clear()
        return __Game__(money)
    
    elif money == 0:
        print("You have no money. Thanks For Playing!")
        pause()
        
    else:
        print("Thanks For Playing!")

    breakf()

    #main 
if __name__ == "__main__":
    
    version = '1.0.0'
    
    print("Welcome To BlackJack, Made by Artyom Curtis Version {}".format(version))
    pause()
    clear()
    
    print(ascii.black_jack)
    pause()
    clear()
    
    money = 100
    
    print("You Start With 100$ you may want to try to increase it.")
    __Game__(money)
            
    

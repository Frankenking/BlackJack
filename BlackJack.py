#Made by Artyom Curtis
#10/17/22
#BlackJack.py




    #packages
import ascii_assets as ascii
import time
import ai
import random

def cardselect(cardlist):
    for _ in range(2):
        card = ai.dealerai()
        if card == 0:
                pass
        else:
                card -= 1
        print(card)
        print(cardlist[card])
        cardlist.pop(card)
        return(card)

def game(settings, cardlist):

    money, ai_players, intelligence = settings[:3]
    print(money, ai_players, intelligence)
    
    player_cards = []
    ai1_cards = []
    ai2_cards = []
    player_cards.append(cardselect(cardlist))
    ai1_cards.append(cardselect(cardlist))
    ai2_cards.append(cardselect(cardlist))

    print("You have", player_cards,"Ai1:", ai1_cards,"Ai2:", ai2_cards)


        

    #game settings
def setting():
    print(ascii.settings)


    start_money = float(input("Money to Start With: "))
    ai_players_amount = int(input("How many Ai players (Max 2): "))
    ai_intelligence_factor = int(input("Ai BlackJack Smarts 0-10: "))

    if ai_players_amount > 2 or ai_players_amount < 0:
        print("Invalid Selection Of Ai Players Please Choose between 0-3") 
        return setting()   


    elif ai_intelligence_factor > 10 or ai_intelligence_factor < 0:
        print("Invalid Ai Intelligence Factor Please Choose between 0-10")
        return setting()


    return(start_money, ai_players_amount, ai_intelligence_factor)

def main():
            #cardlist a = redheart, b = blackspade, c = blackclub, d = rediamond
    cardlist = [
        'a2','a3','a4','a5','a6','a7','a8','a9','a10','aj10','aq10','ak10','a11',
        'b2','b3','b4','b5','b6','b7','b8','b9','b10','bj10','bq10','bk10','b11',
        'c2','c3','c4','c5','c6','c7','c8','c9','c10','cj10','cq10','ck10','c11',
        'd2','d3','d4','d5','d6','d7','d8','d9','d10','dj10','dq10','dk10','d11',
        ]

    print(ascii.black_jack)
    time.sleep(1.5)
    settings = setting()
    game(settings, cardlist)


if __name__ == "__main__":
    print("Thank You For Playing my BlackJack Game Vr 1.0.0")
    time.sleep(2)
    main()
    
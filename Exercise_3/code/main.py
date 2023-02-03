# File name: main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 3 of OOP course

import coin
import dice

# Functions for displaying coins

def create_coins_list():
    while True:
        try:
            amount = int(input("How many coins do you want:"))
            break
        except ValueError:
            print("Only give an integer")
			
    coins = []
    for i in range (0, amount):
        my_coin = coin.Coin()
        coins.append(my_coin)
        
    return coins    

def toss_all_coins(coins: list):
    
    for i in coins:
        i.toss()

def print_all_sideups(coins: list):
    
    for i in coins:
        print("Sideup:", i.get_sideup())


def main():

        
    coins_list = create_coins_list()
    print(coins_list)
    print_all_sideups(coins_list)
    toss_all_coins(coins_list)
    print("Coins are tossed, sideups are:")
    print_all_sideups(coins_list)
    
    my_coin = coin.Coin()
    my_dice = dice.Dice()
    strangers_dice = dice.Dice()
    
    print("\nState of my coin:", my_coin.get_sideup())
    print("Tossing the coin")
    my_coin.toss()
    print("New state of my coin:", my_coin.get_sideup())
    
    
    print("\nCurrency of my coin:", my_coin.get_currency())
    print("Exchanging the currency")
    my_coin.exchange()
    print("New currency of my coin:", my_coin.get_currency())

# Coin functions end
    
    print("\nThe dice rests with this face up:", my_dice.get_face())
    print("Rolling the dice")
    my_dice.roll()
    print("The dice now shows:", my_dice.get_face())

    
    print("\nThe strangers dice rests with this face up:", strangers_dice.get_face())
    print("Rolling the strangers dice")
    strangers_dice.roll()
    print("The strangers dice now shows:", strangers_dice.get_face())
    
    print(int(my_dice.get_face()) + int(strangers_dice.get_face()))
    

# Functions for displaying dice
    
    print("\nThe color of the dice is:", my_dice.get_color())
    print("Painting the dice")
    my_dice.paint()
    print("You painted the dice to be:", my_dice.get_color())

    
    print("\nThe color of the strangers dice is:", strangers_dice.get_color())
    print("Painting the strangers dice")
    strangers_dice.paint()
    print("The stranger painted the dice to be:", strangers_dice.get_color())

    
    print("\nThe material of the dice is:", my_dice.get_material())
    print("Transmogrifying the dice")
    my_dice.transmogrify()
    print("The material of the dice changed into:", my_dice.get_material())

    
    print("\nThe material of the strangers dice is:", strangers_dice.get_material())
    print("Transmogrifying the strangers dice")
    strangers_dice.transmogrify()
    print("The material of the strangers dice changed into:", strangers_dice.get_material())
# Dice functions end
    

    
#coin_full()
main()
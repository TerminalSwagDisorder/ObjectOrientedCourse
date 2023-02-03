# File name: Exercise3_BenjaminW.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing all the code for excercise 3 of OOP course

import random

# Class for coins
class Coin:
    def __init__(self):
        self.__sideup = "Heads"
        self.currency = "Euro"
        
    def toss(self):
        rng = random.randint(0, 11)
        if 0 <= rng <= 4:
            self.__sideup = "Heads"
        elif rng == 10:
            self.__sideup = "Side"
        elif rng == 11:
            self.__sideup = "Coin dissappears"
        else:
            self.__sideup = "Tails"
            
    def get_sideup(self):
        return self.__sideup

    def exchange(self):
        rng = random.randint(0, 4)
        if rng == 0:
            self.currency = "Euro"
        elif rng == 1:
            self.currency = "Dollar"
        elif rng == 2:
            self.currency = "Pound"
        elif rng == 3:
            self.currency = "Yen"
        else:
            self.currency = "Gold"
    
    def get_currency(self):
        return self.currency



# Function for displaying the coin

def coin_toss():

    my_coin = Coin()
    
    print("\nState of my coin:", my_coin.get_sideup())
    print("Tossing the coin")
    my_coin.toss()
    print("New state of my coin:", my_coin.get_sideup())

    
def coin_currency():
    
    my_coin = Coin()
    
    print("\nCurrency of my coin:", my_coin.get_currency())
    print("Exchanging the currency")
    my_coin.exchange()
    print("New currency of my coin:", my_coin.get_currency())


class Dice:
    def __init__(self):
        self.face = "1"
        self.color = "White"
        self.material = "Plastic"
        
    def roll(self):
        rng = random.randint(0, 5)
        if rng == 0:
            self.face = "1"
        elif rng == 1:
            self.face = "2"
        elif rng == 2:
            self.face = "3"
        elif rng == 3:
            self.face = "4"
        elif rng == 4:
            self.face = "5"
        else:
            self.face = "6"
    
    def get_face(self):
        return self.face
    
    def paint(self):
        rng = random.randint(0, 3)
        if rng == 0:
            self.color = "White"
        elif rng == 1:
            self.color = "Red"
        elif rng == 2:
            self.color = "Green"
        else:
            self.color = "Blue"
    
    def get_color(self):
        return self.color
    
    def transmogrify(self):
        rng = random.randint(0, 3)
        if rng == 0:
            self.material = "Plastic"
        elif rng == 1:
            self.material = "Bone"
        elif rng == 2:
            self.material = "Metal"
        else:
            self.material = "Foam"
    
    def get_material(self):
        return self.material
    
def dice_roll():
    
    my_dice = Dice()
    strangers_dice = Dice()

    
    print("\nThe dice rests with this face up:", my_dice.get_face())
    print("Rolling the dice")
    my_dice.roll()
    print("The dice now shows:", my_dice.get_face())

    
    print("\nThe strangers dice rests with this face up:", strangers_dice.get_face())
    print("Rolling the strangers dice")
    strangers_dice.roll()
    print("The strangers dice now shows:", strangers_dice.get_face())

    
def dice_paint():
    
    my_dice = Dice()
    strangers_dice = Dice()

    
    print("\nThe color of the dice is:", my_dice.get_color())
    print("Painting the dice")
    my_dice.paint()
    print("You painted the dice to be:", my_dice.get_color())

    
    print("\nThe color of the strangers dice is:", strangers_dice.get_color())
    print("Painting the strangers dice")
    strangers_dice.paint()
    print("The stranger painted the dice to be:", strangers_dice.get_color())

    
def dice_transmogrify():
    
    my_dice = Dice()
    strangers_dice = Dice()

    
    print("\nThe material of the dice is:", my_dice.get_material())
    print("Transmogrifying the dice")
    my_dice.transmogrify()
    print("The material of the dice changed into:", my_dice.get_material())

    
    print("\nThe material of the strangers dice is:", strangers_dice.get_material())
    print("Transmogrifying the strangers dice")
    strangers_dice.transmogrify()
    print("The material of the strangers dice changed into:", strangers_dice.get_material())

    
def coin_full():
    coin_toss()
    coin_currency()

def dice_full():
    dice_roll()
    dice_paint()
    dice_transmogrify()
    
coin_full()
dice_full()
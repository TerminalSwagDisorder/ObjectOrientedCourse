# File name: main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 3 of OOP course

import coin
import dice
import phone
import random
import collections


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

# Dice game with tiebreaker
def dice_game():
	my_dice = dice.Dice()
	strangers_dice = dice.Dice()
	friends_dice = dice.Dice()
	
	rng = random.randint(0, 1)
	i = 0
	my_rolls = 0
	strangers_rolls = 0
	friends_rolls = 0
	
	my_dice.paint()
	strangers_dice.paint()
	friends_dice.paint()
	my_color = my_dice.get_color()
	strangers_color = strangers_dice.get_color()
	friends_color = friends_dice.get_color()
	
	while i < 3:
		i += 1
		my_dice.roll()
		strangers_dice.roll()
		friends_dice.roll()

		print("\nRound", i)
		print("My:", my_dice.get_face())
		print("Strangers:", strangers_dice.get_face())
		print("Friends:", friends_dice.get_face())


		my_rolls += int(my_dice.get_face())
		strangers_rolls += int(strangers_dice.get_face())
		friends_rolls += int(friends_dice.get_face())

	players_dict = {
		"me" : my_rolls,
		"the stranger" : strangers_rolls,
		"my friend" : friends_rolls
	}
	
	max_points = max(players_dict.values())
	tie_players = [k for k, v in players_dict.items() if v == max_points]

	if len(tie_players) > 1:
		if my_color == "Blue":
			print("\nI automatically win because blue is best")
		elif strangers_color == "Blue":
			print("\nThe stranger automatically wins because blue is best")
		elif friends_color == "Blue":
			print("\nMy friend automatically wins because blue is best")
		else:
			win = random.choice(tie_players)
			print("\nThe winner is", win, "with", max_points, "total points, who won the tiebreaker!")
	else:
		win = tie_players[0]
		print("\nThe winner is", win, "with", max_points, "total points!")

	print("\nEnding scores")
	print("My points:", my_rolls, "| Strangers points:", strangers_rolls, "| Friends points:", friends_rolls)
	print("\nEnding colors")
	print("My color:", my_color, "| Strangers color:", strangers_color, "|friends color:", friends_color)

def phone_data():
	manufact = str(input("Please give the manufacturers name: "))
	model = str(input("Please give the model name: "))
	while True:
		try:
			retail_price = float(input("Please give the price: "))
			break
		except ValueError:
			print("Please use the format 'x.x' for the price")
		
	# Object creation
	cell_phone = phone.CellPhone(manufact, model, retail_price)
	
	# Accessing public methods
	print("\nManufacturer:", cell_phone.get_manufact())
	print("Model:", cell_phone.get_model())
	print("Retail price", cell_phone.get_retail_price())
	
def main():

# Coin functions
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
	
	# Call these functions inside of main
	dice_game()
	phone_data()

	
main()
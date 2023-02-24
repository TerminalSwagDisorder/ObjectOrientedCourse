# File name: main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 5 of OOP course

import dice
import player
import mammal
import random
from pprint import pprint as pprint


def main():
	# Initialization
	my_dice = dice.Dice()
	strangers_dice = dice.Dice()
	friends_dice = dice.Dice()
	pet_dice = dice.Dice()
	
	me = player.Player(1, "Me", "")
	stranger = player.Player(2, "Stranger", "")
	friend = player.Player(3, "Friend", "")

	dice_dict = {
		me: my_dice,
		stranger: strangers_dice,
		friend: friends_dice
	}
	

	pet_game(pet_dice, me, stranger, friend, dice_dict)
	dice_game(my_dice, strangers_dice, friends_dice, me, stranger, friend, dice_dict)
	
def pet_game(pet_dice, me, stranger, friend, dice_dict):
	# Pet game that gives a player a pet according to rolls

	# Pet game specific initialization
	unavailable = []
	mammal_dict = {}
	
	pet_rolls = {
		me.get_name(): 0,
		stranger.get_name(): 0,
		friend.get_name(): 0
	}
	
	# Give values for the pets
	for x in range(0, len(dice_dict)):
		ID = x + 1
		print("Pet", ID)

		species = str(input("\nPlease give the species of the mammal: "))
		name = str(input("Please give the name of the mammal: "))
		while True:
			try:
				height = float(input("Please give the height of the mammal (in centimeters): "))
				break
			except ValueError:
				print("Please use the format 'x.x' for the height")
				
		while True:
			try:
				weight = float(input("Please give the weight of the mammal (in kilograms): "))
				break
			except ValueError:
				print("Please use the format 'x.x' for the weight")
		mammal_data = mammal.Mammal(ID, species, name, height, weight)

		mammalx = "mammal" + str(ID)

		# Create a dict with the given values
		mammal_list = {"ID" :  mammal_data.get_ID(), 
					   "species" : mammal_data.get_species(), 
					   "name" : mammal_data.get_name(),
					   "height" : mammal_data.get_height(),
					   "weight" : mammal_data.get_weight()
					  }
		
		mammal_dict[mammalx] = mammal_list
		
	# Assign pets
	for owner in dice_dict.keys():
		# Roll the dice and get the total roll
		pet_dice.roll(random.randint(1, 6))
		roll1 = pet_dice.get_face()
		pet_dice.roll(random.randint(1, 6))
		roll2 = pet_dice.get_face()
		roll_tot = int(roll1) + int(roll2)

		# Add the roll total to the dictionary
		pet_rolls[owner.get_name()] = roll_tot

	# Sort the pet owners by their rolls (highest to lowest)
	pet_owners_sorted = sorted(pet_rolls.items(), key=lambda x: x[1], reverse=True)

	# Assign a pet to each owner based on their roll
	for petowner, petroll in pet_owners_sorted:
		if petowner not in unavailable:
			# Find the heaviest pet that hasn't been assigned yet
			max_weight = -1
			max_pet = ""
			for pet, data in mammal_dict.items():
				if pet not in unavailable and data["weight"] > max_weight:
					max_weight = data["weight"]
					max_pet = pet
					if pet:
						pet_data = {
							"ID": data["ID"],
							"name": data["name"]
						}

			# Assign the pet to the owner and mark both as unavailable
			owner = next(x for x in dice_dict.keys() if x.get_name() == petowner)
			owner.set_pet(pet_data)
			unavailable.append(max_pet)
			unavailable.append(petowner)
			
	pet_owners = {
		me.get_name(): me.get_pet(),
		stranger.get_name(): stranger.get_pet(),
		friend.get_name(): friend.get_pet()
	}
	
	
	print("\nPet rolls")
	pprint(pet_rolls)
	print("\nPet owners and their pets")
	pprint(pet_owners)
	

def dice_game(my_dice, strangers_dice, friends_dice, me, stranger, friend, dice_dict):
	# Dice game specific initialization
	rolls_dict = {
		me.get_name(): 0,
		stranger.get_name(): 0,
		friend.get_name(): 0
	}
	
	# Choose round amount
	i = 0
	while True:
		try:
			rounds = int(input("Please enter the amount of rounds you wish to have: "))
			break
		except ValueError:
			print("Please only use positive integers")

	# Start game
	for i in range(0, rounds):
		i += 1
		
		for roll in dice_dict.values():
			roll_amount = random.randint(1, 6)
			roll.roll(roll_amount)

		print("\nRound", i)
		
		for plr, roll in dice_dict.items():
			print(plr.get_name().capitalize(), "rolled:", roll.get_face())
			for tot_plrs in rolls_dict.keys():
				if tot_plrs == plr.get_name():
					rolls_dict[tot_plrs] += roll.get_face()

	max_points = max(rolls_dict.values())
	tie_plrs = [k for k, v in rolls_dict.items() if v == max_points]

	
	# Check for tie
	if len(tie_plrs) > 1:
		print("\nTiebreaker round!")
		tiebreaker_dice = dice.Dice()
		tiebreaker_points = {}
		
		for plr in tie_plrs:
			tiebreaker_points[plr] = 0
			
		while True:
			print("\n")
			for plr, roll in tiebreaker_points.items():
				roll_amount = random.randint(1, 6)
				tiebreaker_dice.roll(roll_amount)
				print(plr.capitalize(), "rolled:", tiebreaker_dice.get_face())
				tiebreaker_points[plr] = tiebreaker_dice.get_face()
				
			max_tiebreaker = max(tiebreaker_points.values())
			tiebreaker_winners = [k for k, v in tiebreaker_points.items() if v == max_tiebreaker]
			
			if len(tiebreaker_winners) == 1:
				win = tiebreaker_winners[0]
				print("\nThe winner is", win, "with", max_points, "points, who won the tiebreaker with", max_tiebreaker, "points!")
				break
			else:
				print("Tie! Rolling again...")
	else:
		win = tie_plrs[0]
		print("\nThe winner is", win, "points, with", max_points, "total points!")

	print("\nEnding scores")
	try:
		print("My points:", rolls_dict[me.get_name()], "| Strangers points:", rolls_dict[stranger.get_name()], "| Friends points:", rolls_dict[friend.get_name()], "| Tiebreaker winner:", win, max_points + max_tiebreaker )
	except UnboundLocalError:
		print("My points:", rolls_dict[me.get_name()], "| Strangers points:", rolls_dict[stranger.get_name()], "| Friends points:", rolls_dict[friend.get_name()])

		
		
main()
# File name: main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 5 of OOP course

import dice
import random

def dice_game():
	my_dice = dice.Dice()
	strangers_dice = dice.Dice()
	friends_dice = dice.Dice()
	dice_dict = {
		"my": my_dice, 
		"strangers": strangers_dice, 
		"friends": friends_dice
	}
	
	rolls_dict = {
		"my": 0,
		"strangers": 0,
		"friends": 0
	}

	i = 0
	while True:
		try:
			rounds = int(input("Please enter the amount of rounds you wish to have: "))
			break
		except ValueError:
			print("Please only use positive integers")

	for i in range(0, rounds):
		i += 1
		
		for roll in dice_dict.values():
			roll_amount = random.randint(1, 6)
			roll.roll(roll_amount)

		print("\nRound", i)
		
		for player, roll in dice_dict.items():
			print(player.capitalize(), "rolled:", roll.get_face())
			for tot_players in rolls_dict.keys():
				if tot_players == player:
					rolls_dict[tot_players] += roll.get_face()

	max_points = max(rolls_dict.values())
	tie_players = [k for k, v in rolls_dict.items() if v == max_points]

	if len(tie_players) > 1:
		print("\nTiebreaker round!")
		tiebreaker_dice = dice.Dice()
		tiebreaker_points = {}
		
		for player in tie_players:
			tiebreaker_points[player] = 0
			
		while True:
			print("\n")
			for player, roll in tiebreaker_points.items():
				roll_amount = random.randint(1, 6)
				tiebreaker_dice.roll(roll_amount)
				print(player.capitalize(), "rolled:", tiebreaker_dice.get_face())
				tiebreaker_points[player] = tiebreaker_dice.get_face()
				
			max_tiebreaker = max(tiebreaker_points.values())
			tiebreaker_winners = [k for k, v in tiebreaker_points.items() if v == max_tiebreaker]
			
			if len(tiebreaker_winners) == 1:
				win = tiebreaker_winners[0]
				print("\nThe winner is", win, "with", max_points, "points, who won the tiebreaker with", max_tiebreaker, "points!")
				break
			else:
				print("Tie! Rolling again...")
	else:
		win = tie_players[0]
		print("\nThe winner is", win, "points, with", max_points, "total points!")

	print("\nEnding scores")
	try:
		print("My points:", rolls_dict["my"], "| Strangers points:", rolls_dict["strangers"], "| Friends points:", rolls_dict["friends"], "| Tiebreaker winner:", win, max_points + max_tiebreaker )
	except UnboundLocalError:
		print("My points:", rolls_dict["my"], "| Strangers points:", rolls_dict["strangers"], "| Friends points:", rolls_dict["friends"])

dice_game()
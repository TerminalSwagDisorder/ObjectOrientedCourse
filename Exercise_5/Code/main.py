# File name: main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 5 of OOP course

import dice
import player
import mammal
import random
from pprint import pprint as pprint


def main():
	my_dice = dice.Dice()
	strangers_dice = dice.Dice()
	friends_dice = dice.Dice()
	pet_dice = dice.Dice()
	
	me = player.Player(1, "Me", "")
	stranger = player.Player(2, "Stranger", "")
	friend = player.Player(3, "Friend", "")

	unavailable = []
	mammal_dict = {}
	pet_rolls = {
		me.get_name(): 0,
		stranger.get_name(): 0,
		friend.get_name(): 0
	}

	dice_dict = {
		me: my_dice,
		stranger: strangers_dice,
		friend: friends_dice
	}
	
	rolls_dict = {
		me.get_name(): 0,
		stranger.get_name(): 0,
		friend.get_name(): 0
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
		
		for plr, roll in dice_dict.items():
			print(plr.get_name().capitalize(), "rolled:", roll.get_face())
			for tot_plrs in rolls_dict.keys():
				if tot_plrs == plr.get_name():
					rolls_dict[tot_plrs] += roll.get_face()

	max_points = max(rolls_dict.values())
	tie_plrs = [k for k, v in rolls_dict.items() if v == max_points]

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
# File:		 main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 5 of OOP course

import card
import deck

def main():
	
	print("Let's test that a single card works...")
	
	my_card = card.Card("Hearts", 12)
	my_card.show_card()
	print(my_card)

	print("Single card testing is over.\n")

	print("Let's test that a deck of card is created...")

	my_deck = deck.Deck()
	my_deck.show_deck()

	print("Card deck testing is over.\n")

	print("Let's shuffle the deck.")
	my_deck.shuffle_deck()

	print("Let's test that a deck of card is shuffled...")

	my_deck.show_deck()

	print("Cards should be suffled now.\n")

	print("Let's draw 2 cards and show them.")
	print("You draw:")
	card1 = my_deck.draw_card()
	card1.show_card()
	print("Your opponent draw:")
	card1 = my_deck.draw_card()
	card1.show_card()
	
	# Code your Exercise 5 taks 7 game here. 
	three_cards()
	
def three_cards():
	print("\n\nDraw three cards game")
	card_deck = deck.Deck()
	card_deck.shuffle_deck()

	# Draw three cards for each player
	my_cards = [card_deck.draw_card() for single_card in range(3)]
	opponent_cards = [card_deck.draw_card() for single_card in range(3)]

	# Calculate scores for each player
	my_score = sum([card.get_value() for card in my_cards])
	opponent_score = sum([card.get_value() for card in opponent_cards])
	
	# Print out the cards and scores
	print("\nYour cards:")
	for card in my_cards:
		print(card)
	print("\nOpponent's cards:")
	for card in opponent_cards:
		print(card)
		
	# Determine the winner
	if my_score > opponent_score:
		print("\nCongratulations, you win!")
	elif my_score < opponent_score:
		print("\nSorry, you lose.")
	else:
		print("\nTie! Redrawing...")

		# If there is a tie, redraw until there is a winner
		while my_score == opponent_score:
			my_cards = [card_deck.draw_card() for _ in range(3)]
			opponent_cards = [card_deck.draw_card() for _ in range(3)]
			my_score = sum([card.get_value() for card in my_cards])
			opponent_score = sum([card.get_value() for card in opponent_cards])
		print("\nYour new cards:")
		for card in my_cards:
			print(card)
		print("\nOpponent's new cards:")
		for card in opponent_cards:
			print(card)

		if my_score > opponent_score:
			print("\nCongratulations, you win!\n")
		else:
			print("\nSorry, you lose.\n")


	print("\nYour score:", my_score)
	print("Opponent's score:", opponent_score)


# Calling the main function here, do not change...
main()

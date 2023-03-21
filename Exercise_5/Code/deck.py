# File name: deck.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 5 of OOP course

import random
import card

class Deck:
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		for s in suits:
			for v in range(1,14):
				self.cards.append(card.Card(s, v))

	def show_deck(self):
		for c in self.cards:
			c.show_card()

	def shuffle_deck(self):
		random.shuffle(self.cards)

	def draw_card(self):
		return self.cards.pop()
	
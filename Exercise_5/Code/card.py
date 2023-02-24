# File name: card.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 5 of OOP course

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def show_card(self):
		if self.value == 1:
			val = "Ace"
		elif self.value == 11:
			val = "Jack"
		elif self.value == 12:
			val = "Queen"
		elif self.value == 13:
			val = "King"
		else:
			val = str(self.value)

		print(f"{val} of {self.suit}")
	
	def __str__(self):
		if self.value == 1:
			val = "Ace"
		elif self.value == 11:
			val = "Jack"
		elif self.value == 12:
			val = "Queen"
		elif self.value == 13:
			val = "King"
		else:
			val = str(self.value)

		return f"{val} of {self.suit}"

	def get_value(self):
		return self.value
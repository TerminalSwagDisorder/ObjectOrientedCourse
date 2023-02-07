# File name: Exercise3_BenjaminW.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 3 of OOP course

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
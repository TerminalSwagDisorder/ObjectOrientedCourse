# File name: dice.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 5 of OOP course

import random

# Class for dice
class Dice:
	def __init__(self):
		self.face = "1"
		
	def roll(self, amount):
		self.face = random.randint(1, amount)
	
	def get_face(self):
		return self.face
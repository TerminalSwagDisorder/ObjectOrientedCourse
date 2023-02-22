# File name: dice.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 4 of OOP course

import random

# Class for dice
class Dice:
	def __init__(self):
		self.face = "1"
		self.color = "White"
		self.material = "Plastic"
		
	def roll(self, amount):
		self.face = random.randint(1, amount)
	
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
	

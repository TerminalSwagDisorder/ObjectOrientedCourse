# File name: Exercise3_BenjaminW.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 3 of OOP course

import random

# Class for dice
class Dice:
	def __init__(self):
		self.face = "1"
		self.color = "White"
		self.material = "Plastic"
		
	def roll(self):
		rng = random.randint(0, 5)
		if rng == 0:
			self.face = "1"
		elif rng == 1:
			self.face = "2"
		elif rng == 2:
			self.face = "3"
		elif rng == 3:
			self.face = "4"
		elif rng == 4:
			self.face = "5"
		else:
			self.face = "6"
	
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
	

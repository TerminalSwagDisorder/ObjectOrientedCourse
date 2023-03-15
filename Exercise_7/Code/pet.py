# File name: pet.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 7 of OOP course

class Pet:
	def __init__(self, species, name, height, weight):
		self.species = species
		self.name = name
		self.height = height
		self.weight = weight


	def set_species(self, species):
		self.species = species

	def get_species(self):
		return self.species


	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name
	

	def set_height(self, height):
		self.height = height
	
	def get_height(self):
		return self.height


	def set_weight(self, weight):
		self.weight = weight
	
	def get_weight(self):
		return self.weight


	def __str__(self):
		return f'Species: {self.species}\nName: {self.name}\nHeight: {self.height}\nWeight: {self.weight}'
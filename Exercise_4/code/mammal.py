# File name: mammal.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 4 of OOP course

class Mammal:
	# Data attributes
	def __init__(self, ID, species, name, height, weight): # Init method
		self.ID = ID
		self.species = species # Encapsulation
		self.name = name # Encapsulation
		self.height = height # Encapsulation
		self.weight = weight # Encapsulation

	def __str__(self):
		return f"ID: {self.ID} \nSpecies: {self.species}\nName: {self.name}\nheight: {self.height}\nweight: {self.weight}"
		
	# Public methods
	def set_ID(self, ID):
		self.ID = ID
	
	def get_ID(self):
		return self.ID


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



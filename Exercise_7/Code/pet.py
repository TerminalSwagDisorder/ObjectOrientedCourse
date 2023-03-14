# File name: pet.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 7 of OOP course

class Pet:
	def __init__(self, species, name):
		self.species = species
		self.name = name


	def set_species(self, species):
		self.species = species

	def get_species(self):
		return self.species


	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name


	def __str__(self):
		return f'Species: {self.species}\nName: {self.name}'
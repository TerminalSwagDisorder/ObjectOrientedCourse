# File name: player.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 5 of OOP course

class Player:
	def __init__(self, ID, name, pet):
		self.ID = ID
		self.name = name
		self.pet = pet
		
	def __str__(self):
		return f"ID: {self.ID} \nName: {self.name}\nPet: {self.pet}"


	def set_ID(self, ID):
		self.ID = ID
	
	def get_ID(self):
		return self.ID
	
	
	def set_name(self, name):
		self.name = name
	
	def get_name(self):
		return self.name


	def set_pet(self, pet):
		self.pet = pet
	
	def get_pet(self):
		return self.pet
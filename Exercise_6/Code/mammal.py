# File name: mammal.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 6 of OOP course

class Mammal:
	def __init__(self, ID, species, height, weight, sound, diet):
		self.ID = ID
		self.species = species
		self.height = height
		self.weight = weight
		self.sound = sound
		self.diet = diet

	def __str__(self):
		return f"ID: {self.ID} \nSpecies: {self.species}\nHeight: {self.height}\nWeight: {self.weight}\nSound: {self.sound}\nDiet: {self.diet}"
		
	def set_ID(self, ID):
		self.ID = ID
	
	def get_ID(self):
		return self.ID


	def set_species(self, species):
		self.species = species
	
	def get_species(self):
		return self.species





	def set_height(self, height):
		self.height = height
	
	def get_height(self):
		return self.height


	def set_weight(self, weight):
		self.weight = weight
	
	def get_weight(self):
		return self.weight


	def set_sound(self, sound):
		self.sound = sound
	
	def get_sound(self):
		return self.sound

	
	def set_diet(self, diet):
		self.diet = diet
	
	def get_diet(self):
		return self.diet

class DomesticMammal(Mammal):
	def __init__(self, ID, species, name, height, weight, sound, diet, owner = None):  # Give values to be optional default values
		super().__init__(ID, species, height, weight, sound, diet) # Hard code values
		self.name = name
		self.owner = owner

	def set_name(self, name):
		self.name = name
	
	def get_name(self):
		return self.name
	
	
	def set_owner(self, owner):
		self.owner = owner
	
	def get_owner(self):
		return self.owner

	
	def __str__(self):
		return f'{super().__str__()}\nName: {self.name}\nOwner: {self.owner}'

class WildMammal(Mammal):
	def __init__(self, ID, species, height, weight, sound, diet, benefactor = None):
		super().__init__(ID, species, height, weight, sound, diet)
		self.benefactor = benefactor
		
	def set_benefactor(self, benefactor):
		self.benefactor = benefactor
	
	def get_benefactor(self):
		return self.benefactor


	def __str__(self):
		return f'{super().__str__()}\nBenefactor: {self.benefactor}'

class Cat(DomesticMammal):
	def __init__(self, ID, name, height, weight, owner = None):
		super().__init__(ID, "Cat", name, height, weight, "Meow", "Fish", owner)

class Dog(DomesticMammal):
	def __init__(self, ID, name, height, weight, owner = None):
		super().__init__(ID, "Dog", name, height, weight, "Woof", "Meat", owner)

class Mouse(WildMammal):
	def __init__(self, ID, height, weight, benefactor = None):
		super().__init__(ID, "Mouse", height, weight, "Squeak", "Cheese")

class Elephant(WildMammal):
	def __init__(self, ID, height, weight, benefactor = None):
		super().__init__(ID, "Elephant", height, weight, "Idk", "Leaves")

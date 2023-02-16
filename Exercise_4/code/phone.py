# File name: phone.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 4 of OOP course

class CellPhone:
	# Data attributes
	def __init__(self, ID, manufact, model, retail_price): # Init method
		self.ID = ID
		self.manufact = manufact # Encapsulation
		self.model = model # Encapsulation
		self.retail_price = retail_price # Encapsulation

	def __str__(self):
		return f"ID: {self.ID} \nManufacturer: {self.manufact}\nModel: {self.model}\nPrice: {self.retail_price}"
		
	# Public methods
	def set_ID(self, ID):
		self.ID = ID
	
	def get_ID(self):
		return self.ID
	
	
	def set_manufact(self, manufact):
		self.manufact = manufact
		
	def get_manufact(self):
		return self.manufact
	
	
	def set_model(self, model):
		self.model = model
		
	def get_model(self):
		return self.model
	
	
	def set_retail_price(self, retail_price):
		self.retail_price = retail_price
		
	def get_retail_price(self):
		return self.retail_price
	

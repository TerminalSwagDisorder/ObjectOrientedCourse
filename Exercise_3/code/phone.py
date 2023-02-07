# File name: Exercise3_BenjaminW.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 3 of OOP course

class CellPhone:
	# Data attributes
	def __init__(self, manufact, model, retail_price): # Init method
		self.manufact = manufact # Encapsulation
		self.model = model # Encapsulation
		self.retail_price = retail_price # Encapsulation

	# Public methods
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

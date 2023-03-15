# File name: car.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 7 of OOP course

class Car:
	def __init__(self, make, model, max_load, trunk_size):
		self.make = make
		self.model = model
		self.max_load = max_load
		self.trunk_size = trunk_size

	def set_make(self, make):
		self.make = make

	def get_make(self):
		return self.make


	def set_model(self, model):
		self.model = model

	def get_model(self):
		return self.model
		

	def set_max_load(self, max_load):
		self.max_load = max_load

	def get_max_load(self):
		return self.max_load
	

	def set_trunk_size(self, trunk_size):
		self.trunk_size = trunk_size
	
	def get_trunk_size(self):
		return self.trunk_size


	def __str__(self):
		return f"Make: {self.make} \nModel: {self.model}\nMaximum load limit: {self.max_load}\nSize of trunk: {self.trunk_size}"
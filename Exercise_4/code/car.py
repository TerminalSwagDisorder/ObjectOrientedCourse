# File name: car.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 4 of OOP course

class Car:
	def __init__(self, make, model, mileage, price, color, max_load, trunk_size):
		self.__make = make
		self.__model = model
		self.__mileage = mileage
		self.__price = price
		self.__color = color
		self.__max_load = max_load
		self.__trunk_size = trunk_size


	def __str__(self):
		return f"Make: {self.__make} \nModel: {self.__model}\nMileage: {self.__mileage}\nPrice: {self.__price}\nColor: {self.__color}\nMaximum load limit: {self.__max_load}\nSize of trunk: {self.__trunk_size}"


	def set_make(self, make):
		self.__make = make

	def get_make(self):
		return self.__make


	def set_model(self, model):
		self.__model = model

	def get_model(self):
		return self.__model


	def set_mileage(self, mileage):
		self.__mileage = mileage

	def get_mileage(self):
		return self.__mileage
		

	def set_price(self, price):
		self.__price = price

	def get_price(self):
		return self.__price
		

	def set_color(self, color):
		self.__color = color

	def get_color(self):
		return self.__color
		

	def set_max_load(self, max_load):
		self.__max_load = max_load

	def get_max_load(self):
		return self.__max_load
		

	def set_trunk_size(self, trunk_size):
		self.__trunk_size = trunk_size
	
	def get_trunk_size(self):
		return self.__trunk_size
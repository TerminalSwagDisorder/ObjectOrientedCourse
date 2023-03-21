# File name: cookies.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 8 of OOP course

import random


class Cookies:
	def __init__(self, flavour=None, frosting=None, doneness="raw"):
		self.flavour = flavour if flavour is not None else random.choice(["Chocolate chip", "Vanilla", "Hazelnut"])
		self.frosting = frosting
		self.doneness = doneness

	def __str__(self):
		return f"Doneness = {self.doneness}\nFlavour: {self.flavour}\nFrosting: {self.frosting}\n"

	def set_doneness(self, doneness):
		self.doneness = doneness

	def get_doneness(self):
		return self.doneness
	
	
	def set_flavour(self, flavour):
		self.flavour = flavour

	def get_flavour(self):
		return self.flavour

	def add_flavour(self, flavour):
		self.flavour_list.append(flavour)
		

	def set_frosting(self, frosting):
		self.frosting = frosting

	def get_frosting(self):
		return self.frosting

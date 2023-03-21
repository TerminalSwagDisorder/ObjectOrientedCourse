# File name: cookies.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 8 of OOP course

class Cookies:
	def __init__(self, flavour, frosting, doneness = "raw", state = 1):
		self.flavour = flavour
		self.frosting = frosting
		self.doneness = doneness
		self.state = state
		

	def __str__(self):
		return f"State: {self.state}\nDoneness = {self.doneness}\nFlavour: {self.flavour}\nFrosting: {self.frosting}\n"

	def set_doneness(self, doneness):
		self.doneness = doneness

	def get_doneness(self):
		return self.doneness


	def set_flavour(self, flavour):
		self.flavour = flavour

	def get_flavour(self):
		return self.flavour


	def set_frosting(self, frosting):
		self.frosting = frosting

	def get_frosting(self):
		return self.frosting


	def set_state(self, state):
		self.state = state

	def get_state(self):
		return self.state

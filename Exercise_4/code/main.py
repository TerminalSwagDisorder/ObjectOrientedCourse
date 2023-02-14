# File name: main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 3 of OOP course

import phone
import random

def phone_data():
	ID = random.randint(1, 6)
	manufact = str(input("Please give the manufacturers name: "))
	model = str(input("Please give the model name: "))
	retail_price = float(input("Please give the price: "))
	
	# Object creation
	cell_phone = phone.CellPhone(ID, manufact, model, retail_price)
	
	# Accessing public methods
	#print("Manufacturer:", cell_phone.get_manufact())
	#print("Model:", cell_phone.get_model())
	#print("Retail price", cell_phone.get_retail_price())
	
	print(cell_phone)
	
	
phone_data()
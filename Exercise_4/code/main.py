# File name: main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 4 of OOP course

import dice
import phone
import random

def phone_data():
	phone_list = []
	phone_dict = {}
	different_phone_dict = {}
	phone_dice = dice.Dice()

	while True:
		try:
			amount = int(input("How many phones do you want: "))
			if amount < 1:
				print("Value can not be less than 1")
			else:
				break
		except ValueError:
			print("Value must be a positive integer")
			
	phone_dice.roll(amount)
	rolled_num = phone_dice.get_face()
	
	for x in range(0, amount):
		ID = x + 1

		manufact = str(input("\nPlease give the manufacturers name: "))
		model = str(input("Please give the model name: "))
		
		while True:
			try:
				retail_price = float(input("Please give the price: "))
				break
			except ValueError:
				print("Please use the format 'x.x' for the price")
		
		print("\nPhone #" + str(ID))
		
		cell_phonex = "cell_phone" + str(ID)
		cell_phone_data = phone.CellPhone(ID, manufact, model, retail_price)

		phone_list = ["ID: " + str(cell_phone_data.get_ID()), "Manufacturer: " + cell_phone_data.get_manufact(), "Model: " + cell_phone_data.get_model(), "Retail price: " + str(cell_phone_data.get_retail_price())]
		
		phone_dict[cell_phonex] = phone_list
		print("\n")
		print(cell_phone_data)



	if "cell_phone" + str(rolled_num) in phone_dict:
		print("\nRandomly chosen phone")
		print(phone_dict["cell_phone" + str(rolled_num)])
	
	print("\nAll phones")
	print(phone_dict)
	
def main():
	phone_data()

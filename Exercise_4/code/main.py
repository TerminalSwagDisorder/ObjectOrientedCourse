# File name: main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 4 of OOP course

import dice
import phone
import car
import mammal
import random

def phone_data():
	# Initialization
	phone_list = []
	phone_dict = {}
	phone_dice = dice.Dice()

	# Choose the amount of phones
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
	
	# Give values to phone objects
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
		
		# Create dict of the phones
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
	
	
def car_moment():
	# Initialization
	mammal_dict = {}
	mammal_dice = dice.Dice()

	
	# Give values to the car object
	make = str(input("Please give the make of the car: "))
	model = str(input("Please give the model of the car: "))
	
	while True:
		try:
			mileage = float(input("Please give the mileage of the car (in kilometers): "))
			break
		except ValueError:
			print("Please use the format 'x.x' for the mileage")
			
	while True:
		try:
			price = float(input("Please give the price of the car: "))
			break
		except ValueError:
			print("Please use the format 'x.x' for the price")
		
	color = str(input("Please give the color of the car: "))
	
	while True:
		try:
			max_load = float(input("Please give the maximum load (in kilograms): "))
			break
		except ValueError:
			print("Please use the format 'x.x' for the maximum load")

	while True:
		try:
			trunk_size = float(input("Please give the trunk size (in centimeters): "))
			break
		except ValueError:
			print("Please use the format 'x.x' for the maximum trunk size")

	# Car object
	car1 = car.Car(make, model, mileage, price, color, max_load, trunk_size)
	
	print("\n")
	print(car1)

	# Choose amount of mammals you want
	while True:
		try:
			amount = int(input("\nHow many mammals do you want: "))
			if amount < 1:
				print("Value can not be less than 1")
			else:
				break
		except ValueError:
			print("Value must be a positive integer")

	mammal_dice.roll(amount)
	rolled_num = mammal_dice.get_face()
	
	# Give values to the mammal object
	for x in range(0, amount):
		ID = x + 1

		species = str(input("\nPlease give the species of the mammal: "))
		name = str(input("Please give the name of the mammal: "))
		
		while True:
			try:
				height = float(input("Please give the height of the mammal (in centimeters): "))
				break
			except ValueError:
				print("Please use the format 'x.x' for the price")
				
		while True:
			try:
				weight = float(input("Please give the weight of the mammal (in kilograms): "))
				break
			except ValueError:
				print("Please use the format 'x.x' for the price")

		
		print("\nMammal #" + str(ID))
		
		mammalx = "mammal" + str(ID)
		mammal_data = mammal.Mammal(ID, species, name, height, weight)

		# Create a dict with the given values
		mammal_list = {"ID" :  mammal_data.get_ID(), 
					   "species" : mammal_data.get_species(), 
					   "name" : mammal_data.get_name(), 
					   "height" : mammal_data.get_height(), 
					   "weight" : mammal_data.get_weight()
					  }
		
		mammal_dict[mammalx] = mammal_list
		print("\n")
		print(mammal_data)
		print(mammal_dict)
	
	# Choose a random mammal and check it against the car
	if "mammal" + str(rolled_num) in mammal_dict:
		print("\nRandomly chosen mammal")
		print(mammal_dict["mammal" + str(rolled_num)])
		if mammal_dict["mammal" + str(rolled_num)]["weight"] < float(car1.get_max_load()) and mammal_dict["mammal" + str(rolled_num)]["height"] < float(car1.get_trunk_size()):
			print(mammal_dict["mammal" + str(rolled_num)]["name"], "fits inside the car")
		else:
			print(mammal_dict["mammal" + str(rolled_num)]["name"], "does not fit inside the car")


def main():
	#phone_data()
	car_moment()

main()
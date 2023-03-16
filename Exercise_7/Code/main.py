# File name: main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 7 of OOP course

import os
from pprint import pprint as pprint
import random
import student
import pet
import car
import pcparts

def main():
	# Create Pet objects
	pet1 = pet.Pet("cat", "Fluffy", 8, 10)
	pet2 = pet.Pet("dog", "Buddy", 18, 25)
	pet3 = pet.Pet("hamster", "Squeaky", 2, 1)
	pet4 = pet.Pet("bird", "Tweety", 4, 1)
	pet5 = pet.Pet("fish", "Goldie", 1, 1)
	pet6 = pet.Pet("turtle", "Speedy", 6, 3)
	pet7 = pet.Pet("guinea pig", "Nibbles", 10, 1)
	pet8 = pet.Pet("horse", "Thunder", 1600, 500)
	pet9 = pet.Pet("bull", "Gerald", 150, 700)

	pet_list = [pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9]

	
	# Create Car objects
	car1 = car.Car("Toyota", "Camry", 500, 20)
	car2 = car.Car("Honda", "Civic", 400, 15)
	car3 = car.Car("Ford", "Mustang", 600, 25)
	
	car_list = [car1, car2, car3]


	# Create Student objects
	student1 = student.Student("Alice", "Smith", "001", [pet1.get_name(), pet2.get_name()])
	student2 = student.Student("Bob", "Johnson", "002")
	
	student1.add_car(car1)
	
	
	# Create Motherboard objects
	mobo1 = pcparts.Motherboard(1, "ASUS", "ROG STRIX Z590-E GAMING WIFI", "Z590", 3)
	mobo2 = pcparts.Motherboard(2, "Gigabyte", "B450M DS3H", "B450", 2)
	mobo3 = pcparts.Motherboard(3, "ASUS", "TUF GAMING B560M-PLUS WIFI", "B560", 2)
	mobo4 = pcparts.Motherboard(4, "ASRock", "B560M-ITX/ac", "B560", 1)
	mobo5 = pcparts.Motherboard(5, "MSI", "MPG Z590 GAMING FORCE", "Z590", 3)
	mobo6 = pcparts.Motherboard(6, "MSI", "MPG B550 Gaming Edge WIFI", "B550", 2)
	mobo7 = pcparts.Motherboard(7, "ASRock", "B450M PRO4-F", "B450", 1)


	# Create CPU objects
	cpu1 = pcparts.CPU(8, "Intel", "Core i9-11900K", "LGA 1200", 8, "3.5 GHz")
	cpu2 = pcparts.CPU(9, "AMD", "Ryzen 9 5950X", "AM4", 16, "3.4 GHz")
	cpu3 = pcparts.CPU(10, "Intel", "Core i5-10600K", "LGA 1200", 6, "4.1 GHz")
	cpu4 = pcparts.CPU(11, "AMD", "Ryzen 5 5600X", "AM4", 6, "3.7 GHz")
	cpu5 = pcparts.CPU(12, "Intel", "Core i7-10700K", "LGA 1200", 8, "3.8 GHz")
	cpu6 = pcparts.CPU(3, "AMD", "Ryzen 7 5800X", "AM4", 8, "3.8 GHz")

	# Create GPU objects
	gpu1 = pcparts.GPU(14, "NVIDIA", "GeForce RTX 3080", 16, "1.71 GHz")
	gpu2 = pcparts.GPU(15, "AMD", "Radeon RX 6800 XT", 16, "2.25 GHz")
	gpu3 = pcparts.GPU(16, "NVIDIA", "GeForce GTX 1660", 8, "1.53 GHz")
	
	
	mobo_list = [mobo1, mobo2, mobo3, mobo4, mobo5, mobo6, mobo7]
	cpu_list = [cpu1, cpu2, cpu3, cpu4, cpu5, cpu6]
	gpu_list = [gpu1, gpu2, gpu3]

	
	
	#rel_test(pet_list, car_list, student1, student2)
	#pet_car_check(pet_list, car_list)
	#country_quiz()
	pcparts_test(mobo_list, cpu_list, gpu_list)

def rel_test(pet_list, car_list, student1, student2):
	# Add the pet to the student
	for p in pet_list:
		if p.get_name() not in student1.get_pets():
			student2.add_pets(p)



	print(student1)
	print("\n")
	print(student1.get_car())
	print("\n")
	
	student1.remove_pets()
	print("Removed " + student1.get_first_name() + " " + student1.get_last_name() + "s pets")
	
	student1.remove_car()
	print("Removed " + student1.get_first_name() + " " + student1.get_last_name() + "s car")
	
	print("\n")
	print(student1)
	print("\n")
	print(student1.get_car())
	
def pet_car_check(pet_list, car_list):
	for c in car_list:
		#print("\n")
		for z in pet_list:
			if z.get_weight() > c.get_max_load() or z.get_height() > c.get_trunk_size():
				print("\n" + z.get_name() + " the " + z.get_species() + " does not fit into " + c.get_make() + " " + c.get_model())
				if z.get_weight() > c.get_max_load() and z.get_height() > c.get_trunk_size():
					print("Size warning: " + z.get_name() + " is too heavy, and the trunk of " + c.get_make() + " " + c.get_model() + " is too small\n")
				elif z.get_weight() > c.get_max_load():
					print("Weight warning: " + z.get_name() + " is too heavy\n")
				elif z.get_height() > c.get_trunk_size():
					print("Height warning: The trunk of " + c.get_make() + " " + c.get_model() + " is too small\n")
			else:
				print(z.get_name() + " the " + z.get_species() + " fits into " + c.get_make() + " " + c.get_model())
				
def country_quiz():
	points = 0
	countries_dict = {}
	already_guessed = set()
	countries = ["Afghanistan,Kabul", "Albania,Tirana", "Algeria,Algiers", "Argentina,Buenos Aires", "Australia,Canberra", "Austria,Vienna", "Bangladesh,Dhaka", "Belgium,Brussels", "Brazil,Brasilia", "Cambodia,Phnom Penh", "Canada,Ottawa", "China,Beijing", "Colombia,Bogota", "Croatia,Zagreb", "Cuba,Havana", "Denmark,Copenhagen", "Egypt,Cairo", "Finland,Helsinki", "France,Paris", "Germany,Berlin", "Greece,Athens", "India,New Delhi", "Indonesia,Jakarta", "Iran,Tehran", "Iraq,Baghdad", "Ireland,Dublin", "Italy,Rome", "Japan,Tokyo", "Kazakhstan,Nur-Sultan", "Kenya,Nairobi", "Mexico,Mexico City", "Netherlands,Amsterdam", "Nigeria,Abuja", "North Korea,Pyongyang", "Norway,Oslo", "Pakistan,Islamabad", "Peru,Lima", "Philippines,Manila", "Poland,Warsaw", "Portugal,Lisbon", "Russia,Moscow", "South Africa,Pretoria", "South Korea,Seoul", "Spain,Madrid", "Sweden,Stockholm", "Switzerland,Berne", "Thailand,Bangkok", "Turkey,Ankara", "Ukraine,Kyiv", "United Kingdom,London", "United States,Washington D.C."]


	while True:
		try:
			# Open file and insert elements into dict
			with open("countries.txt") as file:
				for line in file:
					stripped_line = line.strip("\n")
					split_line = stripped_line.split(",")
					countries_dict.update({split_line[0] : split_line[1]})
					#countries_dict[split_line[0]] = split_line[1]
			break

		# If file is not found, create one and insert data
		except FileNotFoundError:
			print("File not found, creating and filling file countries.txt")
			with open("countries.txt", "w") as file:
				for country in countries:
					file.write(country + "\n")

					
	check_dict = str(input("\nDo you want to check the contents of the dict? (y/yes) ")).capitalize()
	if check_dict == "Y" or check_dict == "Yes":
		pprint(countries_dict)



	# Actual game itself
	for game in range(10):
		print("\nRound " + str(game + 1))
		rng = random.choice(list(countries_dict.keys()))

		# If country has already been guessed, reroll 
		while rng in already_guessed:
				rng = random.choice(list(countries_dict.keys()))

		ans = str(input("\nWhat is the capital of " + str(rng) + ": ")).capitalize()
		already_guessed.add(rng)
		if ans == countries_dict[rng]:
			print("Correct")
			points += 1
		else:
			print("Wrong, the correct answer is " + countries_dict[rng])
		


	print("\nThe game is over, you have " + str(points) + " points!")
	
def pcparts_test(mobo_list, cpu_list, gpu_list):
	amd_chipsets = ["A320", "B350", "B450", "X370", "X470", "X570", "B550", "A520"]
	intel_chipsets = ["B560", "H510", "H570", "Q570", "Z590"]
	
	for m in mobo_list:
		print(m, "\n")
		
	for c in cpu_list:
		print(c, "\n")
		
	for g in gpu_list:
		print(g, "\n")
	
	
	check_comp = str(input("\nDo you want to check motherboard compatibility? (y/yes) ")).capitalize()
	if check_comp == "Y" or check_comp == "Yes":
		print("Compatible motherboards")
		
		for c in cpu_list:
			for m in mobo_list:
				
				if "AM4" in c.get_socket():
					if m.get_chipset() in amd_chipsets:
						print(c.get_model() + " fits in " + m.get_model())

				elif "LGA" in c.get_socket():
					if m.get_chipset() in intel_chipsets:
						print(c.get_model() + " fits in " + m.get_model())


main()
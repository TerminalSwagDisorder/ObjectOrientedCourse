# File name: main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 8 of OOP course

import random
from time import sleep as sleep
from pprint import pprint as pprint
import house
import cookies


def main():
	house1 = house.House(num_windows = 10, num_rooms = 5)


	#clean_house1(house1)
	#bake_cookies()
	#capital_quiz()
	exceptions()

def clean_house1(house1):	

	while house1.get_state() <= 5:
		
		while True:

			try:
				do_task = int(input("Do you want to perform task " + str(house1.get_state()) + " (1[y]/2[n])"))
			except ValueError:
				print("ValueError: Not an integer!")

			else:	
				try:
					if do_task == 1 or do_task == 2:
						break
					else:
						raise ValueError()

				except ValueError:
					print("ValueError: Not 1 or 2!")

			
				
		if house1.get_state() == 1 and do_task == 1:
			house1.set_windows_dirty(True)
			house1.set_bed_unmade(True)
			house1.set_surfaces_dusty(True)
			house1.set_fridge_empty(True)
			house1.set_toilet_paper_running_out(True)
			print(house1)
			house1.set_state(2)

		elif house1.get_state() == 2 and do_task == 1:
			house1.set_windows_dirty(False)
			house1.set_bed_unmade(False)
			print(house1)
			house1.set_state(3)


		elif house1.get_state() == 3 and do_task == 1:
			house1.set_floors_dirty(False)
			house1.set_surfaces_dusty(False)
			print(house1)
			house1.set_state(4)

		elif house1.get_state() == 4 and do_task == 1:
			house1.set_fridge_empty(False)
			house1.set_toilet_paper_running_out(False)
			print(house1)
			house1.set_state(5)
			
		elif house1.get_state() == 5 and do_task == 1:
			house1.set_toilet_paper_running_out(False)
			print(house1)
			print("\n\nFinished cleaning!")
			break
			
		elif do_task == 2:
			if house1.get_state() == 1:
				print("Not doing task 1")
				print(house1)
				house1.set_state(2)
				
			elif house1.get_state() == 2:
				print("Not doing task 2")
				print(house1)
				house1.set_state(3)
				
			elif house1.get_state() == 3:
				print("Not doing task 3")
				print(house1)
				house1.set_state(4)
				
			elif house1.get_state() == 4:
				print("Not doing task 4")
				print(house1)
				house1.set_state(5)
				
			elif house1.get_state() == 5:
				print("Not doing task 5")
				print(house1)
				print("\n\nFinished cleaning!")
				break
				
		sleep(0.5)
		
def bake_cookies():
	i = 0
	cookies_list = []

	while True:
		try:
			favourite_flavour = input("What is your favourite cookie flavour from these choices: Chocolate chip, Vanilla or Hazelnut: ").lower()
			if favourite_flavour in ["chocolate chip", "vanilla", "hazelnut", "d"]:
				break
			else:
				raise ValueError()
		except ValueError:
			print("ValueError: Not Chocolate chip, Vanilla or Hazelnut!")

	while len(cookies_list) < 10:
		i += 1
		cookie_data = cookies.Cookies()
		cookie_data.set_doneness("Cooked")
		cookiex = "cookie" + str(i)
		
		parsed_list = [cookiex, cookie_data.get_flavour(), cookie_data.get_frosting(), cookie_data.get_doneness()]

		cookies_list.append(parsed_list)

		
		
		if len(cookies_list) == 10:
				
			#print("\n")
			#pprint(cookies_list)
			for c in cookies_list:
				c[2] = "Frosted"
				
			#print("\n")
			#pprint(cookies_list)
			cookies_list = [c for c in cookies_list if favourite_flavour.capitalize() in c]

	
	#print("\n\n\n\n")
	pprint(cookies_list)

		
def capital_quiz():
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
					countries_dict.update({split_line[1] : split_line[0]})
					#countries_dict[split_line[0]] = split_line[1]
			break

		# If file is not found, create one and insert data
		except FileNotFoundError:
			print("File not found, creating and filling file countries.txt")
					
		finally:
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

		while True:
			try:
				ans = str(input("\nWhat is the country of " + str(rng) + ": ")).upper()
				break
			except ValueError:
				print("ValueError: Not a string!")
				

		already_guessed.add(rng)
		if ans == countries_dict[rng].upper():
			print("Correct")
			points += 1
		else:
			print("Wrong, the correct answer is " + countries_dict[rng])
		


	print("\nThe game is over, you have " + str(points) + " points!")
	
def exceptions():
	test_list = ["first", "second", "third"]


	try:
		result = 10 / 0
	except ZeroDivisionError as error:
		print(f"ZeroDivisionError: {error}")


	try:
		print(test_list[5])
	except IndexError as error:
		print(f"IndexError: {error}")


	try:
		print("What is 9 + 10" + 21)
	except TypeError as error:
		print(f"TypeError: {error}")


	try:
		print(asd)
	except NameError as error:
		print(f"NameError: {error}")
		
	
	try:
		print(int("qwe"))
	except ValueError as error:
		print(f"ValueError: {error}")
		
	

main()
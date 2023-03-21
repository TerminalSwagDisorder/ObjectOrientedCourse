# File name: main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 8 of OOP course

from time import sleep as sleep
import house
import cookies


def main():
	house1 = house.House(num_windows = 10, num_rooms = 5)
	
	cookies1 = cookies.Cookies("Vanilla", "Chocolate")
	cookies2 = cookies.Cookies("Chocolate chip", None)
	

	#clean_house1(house1)
	bake_cookies(cookies1, cookies2)

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
		
def bake_cookies(cookies1, cookies2):
	print(cookies1)
	print(cookies2)
			
main()
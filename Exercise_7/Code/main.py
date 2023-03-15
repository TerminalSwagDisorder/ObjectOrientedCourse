# File name: exercise7_3.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 7 of OOP course

import student
import pet
import car

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
	
	
	
	#rel_test(pet_list, car_list, student1, student2)
	#pet_car_check(pet_list, car_list)
	country_quiz()

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
	pass

main()
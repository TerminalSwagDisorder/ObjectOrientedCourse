# File name: exercise7_3.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 7 of OOP course

import student
import pet

def main():
	rel_test()

def rel_test():
	pet1 = pet.Pet("cat", "Fluffy")
	pet2 = pet.Pet("dog", "Buddy")
	pet3 = pet.Pet("hamster", "Squeaky")
	pet4 = pet.Pet("bird", "Tweety")
	pet5 = pet.Pet("fish", "Goldie")
	pet6 = pet.Pet("turtle", "Speedy")
	pet7 = pet.Pet("guinea pig", "Nibbles")
	
	pet_list = [pet1, pet2, pet3, pet4, pet5, pet6, pet7]

	# Create a Student object
	student1 = student.Student("Alice", "Smith", "001", [pet1.get_name(), pet2.get_name()])
	student2 = student.Student("Bob", "Johnson", "002")


	# Add the pet to the student
	for p in pet_list:
		if p.get_name() not in student1.get_pets():
			student2.add_pets(p)


	print(student1)
	print("\n")
	print(student2)
	
	student1.remove_pets()
	
	print("\n")
	print(student1)
	print("\n")
	print(student2)

main()
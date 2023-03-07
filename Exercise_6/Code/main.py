# File name: main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 6 of OOP course
import mammal

def main():
	mammal_test()
	
def mammal_test():
	cat1 = mammal.Cat(1, "Wille", 10, 5, "Me")
	cat2 = mammal.Cat(2, "Catto", 12, 4, "John")
	dog1 = mammal.Dog(3, "Fido", 25, 10, "Sam")
	mouse1 = mammal.Mouse(3, "Mr mouse", 3, 1)
	
	mammal_list = [cat1, cat2, dog1, mouse1]

	for mam in mammal_list:
		print(mam, "\n")
	
main()
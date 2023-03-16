class Animal:
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Dog(Animal):
    def make_sound(self):
        print("Woof")

# Create a list of animals
animals = [Cat(), Dog()]

# Call the make_sound() method for each animal
for animal in animals:
    animal.make_sound()

	
	
'''
	dPath = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
	finPath = dPath + "\\countries.txt"

	#Create countries file if it does not exist
	if not os.path.exists(finPath):
		with open("countries.txt", "w") as file:
			for country in countries:
				file.write(country + "\n")
	else:
'''
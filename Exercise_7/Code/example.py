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

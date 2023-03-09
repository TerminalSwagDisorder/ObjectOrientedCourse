# File name: main.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing functions for excercise 6 of OOP course

import random
import mammal
import person
import computerparts
from time import sleep as sleep

def main():
	
	# Initialize objects
	cat1 = mammal.Cat(1, "Wille", 10, 5)
	cat2 = mammal.Cat(2, "Catto", 12, 4)
	cat3 = mammal.Cat(3, "Whiskers", 7, 2)
	cat4 = mammal.Cat(4, "Mittens", 8, 3)
	dog1 = mammal.Dog(5, "Fido", 25, 10)
	dog2 = mammal.Dog(6, "Fluffkins", 25, 10)
	dog3 = mammal.Dog(7, "Rex", 35, 20)
	dog4 = mammal.Dog(8, "Buddy", 25, 18)
	mouse1 = mammal.Mouse(9, 3, 1)
	mouse2 = mammal.Mouse(10, 3, 1)
	mouse3 = mammal.Mouse(11, 2, 1)
	mouse4 = mammal.Mouse(12, 2, 1)
	elephant1 = mammal.Elephant(13, 300, 5000)
	elephant2 = mammal.Elephant(14, 250, 3500)
	elephant3 = mammal.Elephant(15, 320, 5500)
	elephant4 = mammal.Elephant(16, 280, 4500)
	cat5 = mammal.Cat(17, "Socks", 8, 3)
	dog5 = mammal.Dog(18, "Max", 40, 25)
	mouse5 = mammal.Mouse(19, 3, 2)
	elephant5 = mammal.Elephant(20, 350, 6000)
	
	
	student1 = person.Student(1, "John", "Smith", 20, "Male", "Python programming", 4)
	student2 = person.Student(2, "Jane", "Doe", 21, "Female", "Game programming", 3)
	teacher1 = person.Teacher(3, "Jack", "Jones", 45, "Male", "Python programming", 2500)
	teacher2 = person.Teacher(4, "Alice", "Alison", 34, "Female", "Computer hardware", 2200)
	
	
	# Create list of objects for ease of use
	all_mammals = [cat1,cat2, cat3, cat4, dog1, dog2, dog3, dog4, mouse1, mouse2, mouse3, mouse4, elephant1, elephant2, elephant3, elephant4, cat5, dog5, mouse5, elephant5]
	all_people = [student1, student2, teacher1, teacher2]

	
	#mammal_test(all_mammals)
	#school_people(all_people)
	#pet_owners(all_mammals, all_people)
	#multiple_pet_owners(all_mammals, all_people)
	pcparttest()
	
def mammal_test(all_mammals):
	for mam in all_mammals:
		print(mam, "\n")

def school_people(all_people):	
	for individual in all_people:
		print(individual, "\n")

def pet_owners(all_mammals, all_people):
	unavailable = []
	
	for individual in all_people:
		# Give a pet to an owner
		while individual.get_pet() == None:
			rng = random.randint(0, len(all_mammals) - 1)
			#print(rng, "(" + str(all_mammals[rng].get_ID()) + ")")
			
			if isinstance(all_mammals[rng], mammal.DomesticMammal) and hasattr(all_mammals[rng], "get_owner"):
				petID = all_mammals[rng].get_ID()
				if petID not in unavailable:
					pet = all_mammals[rng].get_name()
					owner = str(individual.get_first_name() + " " + individual.get_last_name())
					individual.set_pet(pet)
					all_mammals[rng].set_owner(owner)
					
					unavailable.append(petID)

					
		# Give a wild animal to a benefactor
		while individual.get_benefactee() == None:
			rng = random.randint(0, len(all_mammals) - 1)
			
			if isinstance(all_mammals[rng], mammal.WildMammal) and hasattr(all_mammals[rng], "get_benefactor"):
				wildID = all_mammals[rng].get_ID()
				if wildID not in unavailable:
					benefactee = str(all_mammals[rng].get_species() + " With ID: " + str(wildID))
					benefactor = str(individual.get_first_name() + " " + individual.get_last_name())
					
					individual.set_benefactee(benefactee)
					all_mammals[rng].set_benefactor(benefactor)
					
					unavailable.append(wildID)

	print("\n")
	for individual in all_people:
		print("Owner/benefactor:", str(individual.get_first_name() + " " + individual.get_last_name()), " | Pet: ", individual.get_pet(), "| Benefactee: ", individual.get_benefactee())
		
	print("\n")
	for pet in all_mammals:
		if isinstance(pet, mammal.DomesticMammal) and hasattr(pet, "get_owner"):
			print("Pet:", pet.get_name(), "| Owner:", pet.get_owner())
			
	print("\n")
	for benefactee in all_mammals:
		if isinstance(benefactee, mammal.WildMammal) and hasattr(benefactee, "get_benefactor"):
			bene = str(benefactee.get_species() + " With ID: " + str(benefactee.get_ID()))
			print("Benefactee:", bene, "| Benefactor:", benefactee.get_benefactor())
	

def multiple_pet_owners(all_mammals, all_people):
	pet_unavailable = []
	wild_unavailable = []
	unavailable = [pet_unavailable, wild_unavailable]
	
	pet_check = []
	benefactee_check = []

	# Create lists for domestic and wild mammals
	for check in all_mammals:
		if isinstance(check, mammal.DomesticMammal):
			pet_check.append(check.get_ID())
		elif isinstance(check, mammal.WildMammal):
			benefactee_check.append(check.get_ID())

	pet_check.sort()
	benefactee_check.sort()

	print(len(all_mammals))
	for individual in all_people: 
		
		pet_amount = random.randint(0, 2)
		wild_amount = random.randint(0, 2)
		pet_list = []
		wild_list = []

		# Give a random amount of pets to an owner
		while len(pet_list) < pet_amount:
			rng = random.randint(0, len(all_mammals) - 1)

			if isinstance(all_mammals[rng], mammal.DomesticMammal) and hasattr(all_mammals[rng], "get_owner"):
				petID = all_mammals[rng].get_ID()
				if petID not in pet_unavailable:
					pet = all_mammals[rng].get_name()
					owner = str(individual.get_first_name() + " " + individual.get_last_name())
					
					pet_list.append(pet)
					all_mammals[rng].set_owner(owner)

					pet_unavailable.append(petID)
					pet_unavailable.sort()
					print(pet_list, unavailable)


					if len(pet_list) == pet_amount:
						individual.set_pet(pet_list)
						print("final step", individual.get_first_name(), individual.get_pet())
					elif len(pet_list) < pet_amount and len(pet_unavailable) == len(pet_check):
						individual.set_pet(pet_list)
						print("test1")
						break

					#elif len(pet_list) < pet_amount and len(pet_unavailable) == len(all_mammals) - wild_amount:

		# Give a random amount of wild animals to a benefactor
		while len(wild_list) < wild_amount:
			rng = random.randint(0, len(all_mammals) - 1)
			
			if isinstance(all_mammals[rng], mammal.WildMammal) and hasattr(all_mammals[rng], "get_benefactor"):
				wildID = all_mammals[rng].get_ID()
				if wildID not in wild_unavailable:
					
					benefactee = str(all_mammals[rng].get_species() + " With ID: " + str(wildID))
					benefactor = str(individual.get_first_name() + " " + individual.get_last_name())
					
					wild_list.append(benefactee)
					all_mammals[rng].set_benefactor(benefactor)
					
					wild_unavailable.append(wildID)
					wild_unavailable.sort()
					if len(wild_list) == wild_amount:
						individual.set_benefactee(wild_list)
						print("Final step for", individual.get_first_name(), individual.get_benefactee())
					elif len(wild_list) < wild_amount and len(pet_unavailable) == len(benefactee_check):
						individual.set_benefactee(wild_list)
						print("test2")
						break

	print("\n")
	for individual in all_people:
		print("Owner/benefactor:", str(individual.get_first_name() + " " + individual.get_last_name()), " | Pet: ", individual.get_pet(), "| Benefactee: ", individual.get_benefactee())
		
	print("\n")
	for pet in all_mammals:
		if isinstance(pet, mammal.DomesticMammal) and hasattr(pet, "get_owner"):
			print("Pet:", pet.get_name(), "| Owner:", pet.get_owner())
			
	print("\n")
	for benefactee in all_mammals:
		if isinstance(benefactee, mammal.WildMammal) and hasattr(benefactee, "get_benefactor"):
			bene = str(benefactee.get_species() + " With ID: " + str(benefactee.get_ID()))
			print("Benefactee:", bene, "| Benefactor:", benefactee.get_benefactor())
			
def pcparttest():
	# External parts
	keyboard1 = computerparts.Keyboard(1, "Logitech", "G213 Prodigy", "USB", "1.8m", "Membrane", "Full-size", "US", "RGB")
	mouse1 = computerparts.Mouse(2, "Logitech", "G502 Hero", "USB", "1.8m", "Hero", 16000, 11, "RGB")
	display1 = computerparts.Display(3, "Dell", "P2419H", "DisplayPort, HDMI", "23.8in", "1920x1080", 60, "IPS")

	# Internal parts
	cpu1 = computerparts.CPU(4, "Intel", "Core i9-11900K", "LGA 1200", 125, 8, 3.5, 5.3, "16MB")
	gpu1 = computerparts.GPU(5, "Nvidia", "GeForce RTX 3080", "PCIe 4.0 x16", 320, 1440, 8704, "10GB GDDR6X")
	memory1 = computerparts.Memory(6, "Kingston", "KVR24N17S8/8", "DDR4", 65, "Unbuffered", "8GB", "1", "2400MHz")

	print(keyboard1, "\n\n", mouse1, "\n\n", display1, "\n\n", cpu1, "\n\n", gpu1, "\n\n", memory1)
main()
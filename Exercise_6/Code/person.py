# File name: person.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 6 of OOP course

class Person:
	def __init__(self, ID, first_name, last_name, age, gender, pet = None, benefactee = None):
		self.ID = ID
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		self.pet = pet
		self.benefactee = benefactee


	def set_ID(self, ID):
		self.ID = ID

	def get_ID(self):
		return self.ID


	def set_first_name(self, first_name):
		self.first_name = first_name

	def get_first_name(self):
		return self.first_name


	def set_last_name(self, last_name):
		self.last_name = last_name

	def get_last_name(self):
		return self.last_name


	def set_age(self, age):
		self.age = age

	def get_age(self):
		return self.age


	def set_gender(self, gender):
		self.gender = gender

	def get_gender(self):
		return self.gender


	def set_pet(self, pet):
		self.pet = pet

	def get_pet(self):
		return self.pet
	

	def set_benefactee(self, benefactee):
		self.benefactee = benefactee

	def get_benefactee(self):
		return self.benefactee
	
	

	def __str__(self):
		return f'ID: {self.ID}\nFirst name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age}\nGender: {self.gender}\nPet: {self.pet}\nBenefactee: {self.benefactee}'


class Student(Person):
	def __init__(self, ID, first_name, last_name, age, gender, major, avg_grade, pet = None, benefactee = None):
		super().__init__(ID, first_name, last_name, age, gender, pet, benefactee)
		self.major = major
		self.avg_grade = avg_grade


	def set_major(self, major):
		self.major = major

	def get_major(self):
		return self.major


	def set_avg_grade(self, avg_grade):
		self.avg_grade = avg_grade
	
	def get_avg_grade(self):
		return self.avg_grade

	
	def __str__(self):
		return f'{super().__str__()}\nMajor: {self.major}\nAverage grade: {self.avg_grade}'
	

class Teacher(Person):
	def __init__(self, ID, first_name, last_name, age, gender, subject, wage, pet = None, benefactee = None):
		super().__init__(ID, first_name, last_name, age, gender, pet, benefactee)
		self.subject = subject
		self.wage = wage


	def set_subject(self, subject):
		self.subject = subject

	def get_subject(self):
		return self.subject


	def set_wage(self, wage):
		self.wage = wage

	def get_wage(self):
		return self.wage
	
	
	def __str__(self):
		return f'{super().__str__()}\nSubject: {self.subject}\nWage: {self.wage}'

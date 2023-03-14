# File name: student.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 7 of OOP course

import pet

class Student:
	def __init__(self, first_name, last_name, student_ID, pets = None):
		self.first_name = first_name
		self.last_name = last_name
		self.student_ID = student_ID
		self.pets = pets if pets is not None else []


	def set_first_name(self, first_name):
		self.first_name = first_name

	def get_first_name(self):
		return self.first_name


	def set_last_name(self, last_name):
		self.last_name = last_name

	def get_last_name(self):
		return self.last_name
		
		
	def set_student_ID(self, student_ID):
		self.student_ID = student_ID

	def get_student_ID(self):
		return self.student_ID


	def add_pets(self, pets):
		self.pets.append(pets.get_name())
		
	def remove_pets(self):
		self.pets.clear()

	def get_pets(self):
		if not self.pets or self.pets == []:
			return f'No pets in list'
		return self.pets


	def __str__(self):
		if not self.pets or self.pets == []:
			return f'First name: {self.first_name}\nLast name: {self.last_name}\nStudent ID: {self.student_ID}\nPets: no pets in list'			
		return f'First name: {self.first_name}\nLast name: {self.last_name}\nStudent ID: {self.student_ID}\nPets: {self.pets}'

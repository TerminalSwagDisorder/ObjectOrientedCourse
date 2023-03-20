# File name: house.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 8 of OOP course

class House:
	def __init__(self, num_windows, num_rooms, windows_dirty=True, floors_dirty=True, bed_unmade=True, surfaces_dusty=True, fridge_empty=True, toilet_paper_running_out=True):
		self.num_windows = num_windows
		self.num_rooms = num_rooms
		self.windows_dirty = windows_dirty
		self.floors_dirty = floors_dirty
		self.bed_unmade = bed_unmade
		self.surfaces_dusty = surfaces_dusty
		self.fridge_empty = fridge_empty
		self.toilet_paper_running_out = toilet_paper_running_out
		self.state = 1

	def __str__(self):
		return f"State {self.state}: windows_dirty={self.windows_dirty}, floors_dirty={self.floors_dirty}, bed_unmade={self.bed_unmade}, surfaces_dusty={self.surfaces_dusty}, fridge_empty={self.fridge_empty}, toilet_paper_running_out={self.toilet_paper_running_out}"

	def set_windows_dirty(self, windows_dirty):
		self.windows_dirty = windows_dirty

	def get_windows_dirty(self):
		return self.windows_dirty

	def set_floors_dirty(self, floors_dirty):
		self.floors_dirty = floors_dirty

	def get_floors_dirty(self):
		return self.floors_dirty

	def set_bed_unmade(self, bed_unmade):
		self.bed_unmade = bed_unmade

	def get_bed_unmade(self):
		return self.bed_unmade

	def set_surfaces_dusty(self, surfaces_dusty):
		self.surfaces_dusty = surfaces_dusty

	def get_surfaces_dusty(self):
		return self.surfaces_dusty

	def set_fridge_empty(self, fridge_empty):
		self.fridge_empty = fridge_empty

	def get_fridge_empty(self):
		return self.fridge_empty

	def set_toilet_paper_running_out(self, toilet_paper_running_out):
		self.toilet_paper_running_out = toilet_paper_running_out

	def get_toilet_paper_running_out(self):
		return self.toilet_paper_running_out


	def set_state(self, state):
		self.state = state

	def get_state(self):
		return self.state
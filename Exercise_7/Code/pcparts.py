# File name: pcparts.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 7 of OOP course

class ComputerPart:
	def __init__(self, ID, manufact, model):
		self.ID = ID
		self.manufact = manufact
		self.model = model


	def set_ID(self, ID):
		self.ID = ID

	def get_ID(self):
		return self.ID


	def set_manufact(self, manufact):
		self.manufact = manufact

	def get_manufact(self):
		return self.manufact


	def set_model(self, model):
		self.model = model

	def get_model(self):
		return self.model


	def __str__(self):
		return f"ID: {self.ID} \nmanufact: {self.manufact}\nModel number: {self.model}"	
	

class Motherboard(ComputerPart):
	def __init__(self, ID, manufact, model, chipset, pcie_slots):
		super().__init__(ID, manufact, model)
		self.chipset = chipset
		self.pcie_slots = pcie_slots


	def set_chipset(self, chipset):
		self.chipset = chipset

	def get_chipset(self):
		return self.chipset


	def set_pcie_slots(self, pcie_slots):
		self.pcie_slots = pcie_slots

	def get_pcie_slots(self):
		return self.pcie_slots


	def __str__(self):
		return f"{super().__str__()}\nChipset: {self.chipset}\nPcie slots: {self.pcie_slots}"
	
	
class CPU(ComputerPart):
	def __init__(self, ID, manufact, model, socket, cores, clock):
		super().__init__(ID, manufact, model)
		self.socket = socket
		self.cores = cores
		self.clock = clock


	def set_socket(self, socket):
		self.socket = socket

	def get_socket(self):
		return self.socket


	def set_cores(self, cores):
		self.cores = cores
		
	def get_cores(self):
		return self.cores


	def set_clock(self, clock):
		self.clock = clock

	def get_clock(self):
		return self.clock


	def __str__(self):
		return f"{super().__str__()}\nsocket: {self.socket}\nCores: {self.cores}\nClock Speed: {self.clock}"


class GPU(ComputerPart):
	def __init__(self, ID, manufact, model, pcie_lanes, speed):
		super().__init__(ID, manufact, model)
		self.pcie_lanes = pcie_lanes
		self.speed = speed


	def set_pcie_lanes(self, pcie_lanes):
		self.pcie_lanes = pcie_lanes

	def get_pcie_lanes(self):
		return self.pcie_lanes

	def set_speed(self, speed):
		self.speed = speed

	def get_speed(self):
		return self.speed


	def __str__(self):
		return f"{super().__str__()}\nPcie lanes: {self.pcie_lanes}\nClock speed: {self.speed}"
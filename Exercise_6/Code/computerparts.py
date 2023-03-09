# File name: computerparts.py
# Auth: Benjamin Willför/TerminalSwagDisorder
# Desc: File containing classes for excercise 6 of OOP course

class ComputerPart:
	def __init__(self, ID, manufacturer, modelnum, connector):
		self.ID = ID
		self.manufacturer = manufacturer
		self.modelnum = modelnum
		self.connector = connector

	def __str__(self):
		return f"ID: {self.ID} \nManufacturer: {self.manufacturer}\nModel number: {self.modelnum}\nConnector: {self.connector}"	

	def set_ID(self, ID):
		self.ID = ID

	def get_ID(self):
		return self.ID

	def set_manufacturer(self, manufacturer):
		self.manufacturer = manufacturer

	def get_manufacturer(self):
		return self.manufacturer

	def set_modelnum(self, modelnum):
		self.modelnum = modelnum

	def get_modelnum(self):
		return self.modelnum

	def set_connector(self, connector):
		self.connector = connector

	def get_connector(self):
		return self.connector


class External(ComputerPart):
	def __init__(self, ID, manufacturer, modelnum, connector, cableLen):
		super().__init__(ID, manufacturer, modelnum, connector)
		self.cableLen = cableLen

	def __str__(self):
		return f"{super().__str__()}\nCable Length: {self.cableLen}"

	def set_cableLen(self, cableLen):
		self.cableLen = cableLen

	def get_cableLen(self):
		return self.cableLen


class Keyboard(External):
	def __init__(self, ID, manufacturer, modelnum, connector, cableLen, switches, tklSize, layout, lighting):
		super().__init__(ID, manufacturer, modelnum, connector, cableLen)
		self.switches = switches
		self.tklSize = tklSize
		self.layout = layout
		self.lighting = lighting

	def __str__(self):
		return f"{super().__str__()}\nSwitches: {self.switches}\nTenkeyless/size: {self.tklSize}\nLayout: {self.layout}\nLighting: {self.lighting}"

	def __str__(self):
		return f"{super().__str__()}\nSwitches: {self.switches}\nTenkeyless/size: {self.tklSize}"

	def set_switches(self, switches):
		self.switches = switches

	def get_switches(self):
		return self.switches

	def set_tklSize(self, tklSize):
		self.tklSize = tklSize

	def get_tklSize(self):
		return self.tklSize

	def set_layout(self, layout):
		self.layout = layout

	def get_layout(self):
		return self.layout

	def set_lighting(self, lighting):
		self.lighting = lighting

	def get_lighting(self):
		return self.lighting


class Mouse(External):
	def __init__(self, ID, manufacturer, modelnum, connector, cableLen, sensor, maxDPI, buttons, lighting):
		super().__init__(ID, manufacturer, modelnum, connector, cableLen)
		self.sensor = sensor
		self.maxDPI = maxDPI
		self.buttons = buttons
		self.lighting = lighting

	def __str__(self):
		return f"{super().__str__()}\nSensor: {self.sensor}\nMax DPI: {self.maxDPI}\nButtons: {self.buttons}\nLighting: {self.lighting}"

	def set_sensor(self, sensor):
		self.sensor = sensor

	def get_sensor(self):
		return self.sensor

	def set_maxDPI(self, maxDPI):
		self.maxDPI = maxDPI

	def get_maxDPI(self):
		return self.maxDPI

	def set_buttons(self, buttons):
		self.buttons = buttons

	def get_buttons(self):
		return self.buttons

	def set_lighting(self, lighting):
		self.lighting = lighting

	def get_lighting(self):
		return self.lighting


class Display(External):
	def __init__(self, ID, manufacturer, modelnum, connector, cableLen, resolution, frequency, panel):
		super().__init__(ID, manufacturer, modelnum, connector, cableLen)
		self.resolution = resolution
		self.frequency = frequency
		self.panel = panel

	def __str__(self):
		return f"{super().__str__()}\nResolution: {self.resolution}\nFrequency: {self.frequency}\nPanel Type: {self.panel}"

	def set_resolution(self, resolution):
		self.resolution = resolution

	def get_resolution(self):
		return self.resolution

	def set_frequency(self, frequency):
		self.frequency = frequency

	def get_frequency(self):
		return self.frequency

	def set_panel(self, panel):
		self.panel = panel

	def get_panel(self):
		return self.panel


class Internal(ComputerPart):
	def __init__(self, ID, manufacturer, modelnum, connector, TDP):
		super().__init__(ID, manufacturer, modelnum, connector)
		self.TDP = TDP

	def __str__(self):
		return f"{super().__str__()}\nTDP: {self.TDP}"

	def set_TDP(self, TDP):
		self.TDP = TDP

	def get_TDP(self):
		return self.TDP


class CPU(Internal):
	def __init__(self, ID, manufacturer, modelnum, connector, TDP, physCores, clock, turbo, cache):
		super().__init__(ID, manufacturer, modelnum, connector, TDP)
		self.physCores = physCores
		self.clock = clock
		self.turbo = turbo
		self.cache = cache

	def __str__(self):
		return f"{super().__str__()}\nPhysical Cores: {self.physCores}\nClock Speed: {self.clock}\nTurbo Speed: {self.turbo}\nCache: {self.cache}"

	def set_physCores(self, physCores):
		self.physCores = physCores

	def get_physCores(self):
		return self.physCores

	def set_clock(self, clock):
		self.clock = clock

	def get_clock(self):
		return self.clock

	def set_turbo(self, turbo):
		self.turbo = turbo

	def get_turbo(self):
		return self.turbo

	def set_cache(self, cache):
		self.cache = cache

	def get_cache(self):
		return self.cache


class GPU(Internal):
	def __init__(self, ID, manufacturer, modelnum, connector, TDP, clock, shaders, vram):
		super().__init__(ID, manufacturer, modelnum, connector, TDP)
		self.clock = clock
		self.shaders = shaders
		self.vram = vram

	def __str__(self):
		return f"{super().__str__()}\nClock: {self.clock} MHz\nShaders: {self.shaders}\nVRAM: {self.vram} GB"

	def set_clock(self, clock):
		self.clock = clock

	def get_clock(self):
		return self.clock

	def set_shaders(self, shaders):
		self.shaders = shaders

	def get_shaders(self):
		return self.shaders

	def set_vram(self, vram):
		self.vram = vram

	def get_vram(self):
		return self.vram


class Memory(Internal):
	def __init__(self, ID, manufacturer, modelnum, connector, TDP, type, capacity, dimms, speed):
		super().__init__(ID, manufacturer, modelnum, connector, TDP)
		self.type = type
		self.capacity = capacity
		self.dimms = dimms
		self.speed = speed

	def __str__(self):
		return f"{super().__str__()}\nType: {self.type}\nCapacity: {self.capacity} GB\nDIMMs: {self.dimms}\nSpeed: {self.speed} MHz"

	def set_type(self, type):
		self.type = type

	def get_type(self):
		return self.type

	def set_capacity(self, capacity):
		self.capacity = capacity

	def get_capacity(self):
		return self.capacity

	def set_dimms(self, dimms):
		self.dimms = dimms

	def get_dimms(self):
		return self.dimms

	def set_speed(self, speed):
		self.speed = speed

	def get_speed(self):
		return self.speed
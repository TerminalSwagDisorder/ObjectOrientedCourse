def pcparttest():
	memory1 = Memory(1, "Kingston", "KVR24N17S8/8", "DDR4", 65, "350W", "Unbuffered", "8GB", "1", "2400MHz")

	print(memory1.get_capacity())
	memory1.set_speed("2666MHz")
	print(memory1.get_speed())
class Math():

	def __init__(self):
		pass

	def addition(self, value1, value2):
		if not isinstance(value1, int) and not isinstance(value2, int):
			return 'Invalid input'
		else:
			return value1 + value2

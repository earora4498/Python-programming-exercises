class stuff:

	def __init__(self):
		self.string = ''

	def getString(self):
		self.string = input('Enter a string: ')

	def printString(self):
		print(self.string.upper())

s = stuff()
s.getString()
s.printString()
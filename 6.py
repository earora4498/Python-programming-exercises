import math

final = []

def formula(num):
	full = (100*num)/30
	return int(math.sqrt(full))

raw = input("Enter a csv sequence: ")

for i in raw.split(','):
	final.append(formula(int(i)))

print(final)
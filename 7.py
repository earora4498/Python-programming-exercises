raw = input("Enter the numbers: ")

a = int(raw.split(',')[0])
b = int(raw.split(',')[1])

final = [[0 for i in range(b)] for i in range(a)]

for i in range(0, a):
	for j in range(0, b):
		final[i][j] = i*j

print(final)
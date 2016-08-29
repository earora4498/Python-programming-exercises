final = [];

for i in range(2000, 3201):
	if (i % 7 == 0 and i % 5 != 0):
		final.append(i)

print(','.join(map(str,final)))

width_max = 9
for index in range(1,width_max +1 ,2):
	line = "*" * index
	line = line.center(width_max)
	print(line)
for index in range(width_max-2,0 ,-2):
	line = "*" * index
	line = line.center(width_max)
	print(line)
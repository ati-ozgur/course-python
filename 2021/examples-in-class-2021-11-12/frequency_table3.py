filename = "animals.csv"


table = {}

 	 	 	

f = open(filename)
f.readline()
for line in f.readlines():
    line = line.replace("\n","")
    number, animal = line.split(',')
    if animal in table.keys():
        table[animal] = table[animal] + 1
    else:
        table[animal] = 1 

print(table)
filename = "animals.csv"


table = {}
table["Dog"] = 0
table["Cat"] = 0
table["Bird"] = 0
table["Fish"] = 0
 	 	 	

f = open(filename)
f.readline()
for line in f.readlines():
    line = line.replace("\n","")
    number, animal = line.split(',')
    table[animal] = table[animal] + 1
        

print(table)
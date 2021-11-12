filename = "animals.csv"



Dog = 0
Cat = 0
Bird = 0
Fish = 0
 	 	 	

f = open(filename)
f.readline()
for line in f.readlines():
    line = line.replace("\n","")
    number, animal = line.split(',')
    if animal == "Dog":
        Dog = Dog + 1
    if animal == "Cat":
        Cat = Cat + 1
    if animal == "Bird":
        Bird = Bird + 1
    if animal == "Fish":
        Fish = Fish + 1
        

print("Dog",Dog)
print("Cat",Cat)
print("Bird",Bird)
print("Fish",Fish)

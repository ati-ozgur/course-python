def number_to_english(number):
	if number == 0:
		print("zero")
	elif number == 1:
		print("one")
	elif number == 2:
		print("two")
	elif number == 3:
		print("three")
	elif number == 4:
		print("four")
	elif number == 5:
		print("five")
	elif number == 6:
		print("six")
	elif number == 7:
		print("seven")
	elif number == 8:
		print("eight")
	elif number == 9:
		print("nine")
	elif number == 10:
		print("ten")
	else:
		print("Unknown INPUT")


number_to_english(5)
number_to_english(7)
number_to_english(8)


for i in range(12):
	number_to_english(i)
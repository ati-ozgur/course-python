print("please enter number1: ")
answer = input()
number1 = float(answer)
print("please enter number2: ")
answer = input()
number2 = float(answer)
print("please enter number3: ")
answer = input()
number3 = float(answer)


if number1 > number2 and number1 > number3:
	greatest = number1
elif number2 > number1 and number2 > number3:
	greatest = number2
else:
	greatest = number3

print(f"numbers are {number1}  {number2}  {number3} and greatest is {greatest}")


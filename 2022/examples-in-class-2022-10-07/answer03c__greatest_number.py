print("please enter 3 numbers with spaces between them: ")
answer = input()
numbers = answer.split(" ")
number1 = float(numbers[0])
number2 = float(numbers[1])
number3 = float(numbers[2])

greatest = max(max(number1,number2),number3)


print(f"numbers are {number1}  {number2}  {number3} and greatest is {greatest}")


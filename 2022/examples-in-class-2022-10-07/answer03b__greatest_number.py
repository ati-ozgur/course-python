print("please enter number1: ")
answer = input()
number1 = float(answer)
print("please enter number2: ")
answer = input()
number2 = float(answer)
print("please enter number3: ")
answer = input()
number3 = float(answer)

#greatest = max(max(number1,number2),number3)
greatest = max(number1,number2)
greatest = max(number3,greatest)

print(f"numbers are {number1}  {number2}  {number3} and greatest is {greatest}")


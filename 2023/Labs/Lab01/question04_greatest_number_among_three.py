print("please enter three numbers, program will find greatest among these three numbers")

str_num1 = input("please enter number 1: ")
str_num2 = input("please enter number 2: ")
str_num3 = input("please enter number 3: ")

num1 = float(str_num1)
num2 = float(str_num2)
num3 = float(str_num3)


greatest = num1

if num2 > greatest:
    greatest = num2

if num3 > greatest:
    greatest = num3


print(f"number 1: {num1} , number 2: {num2}, number 3: {num3} and greatest among the three is {greatest}")


# 12 integer , full number
# 12.5 # float, with points

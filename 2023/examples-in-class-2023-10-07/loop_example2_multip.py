str1 = input("please enter an integer number N")

n1 = int(str1)

factorial_result = 1

current_number = 1
while current_number <= n1:
    factorial_result = factorial_result * current_number
    current_number = current_number + 1

print(f"summation of 1..{n1} is {factorial_result}" )
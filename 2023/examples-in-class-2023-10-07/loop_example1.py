str1 = input("please enter an integer number N")

n1 = int(str1)

total = 0

current_number = 1
while current_number <= n1:
    total = total + current_number
    current_number = current_number + 1

print(f"summation of 1..{n1} is {total}" )
str_N = input("Please enter a number to find summation of 1..N: ")
N = int(str_N)
a = 1
total = 0
while a <= N:
    if a % 3 == 0:
        total = total + a
    a = a + 1

print(total)

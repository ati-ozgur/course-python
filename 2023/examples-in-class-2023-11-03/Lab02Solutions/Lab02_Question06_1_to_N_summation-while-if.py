str_N = input("please enter a number: ")
N = int(str_N)

x = 0
summation = 0
while x <= N: 
    if x % 3 == 0:
        print(x)
        summation = summation + x
    x = x + 1

print(f"summation of 1..{N} only divisible by 3 is {summation}")

# while
# for loop

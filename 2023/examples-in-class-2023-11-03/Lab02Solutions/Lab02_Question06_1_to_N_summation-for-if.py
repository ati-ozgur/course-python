str_N = input("please enter a number: ")
N = int(str_N)

summation = 0
for x in range(N+1):
    if x % 3 == 0:
        print(x)
        summation = summation + x

print(f"summation of 1..{N} only divisible by 3 is {summation}")

# while
# for loop

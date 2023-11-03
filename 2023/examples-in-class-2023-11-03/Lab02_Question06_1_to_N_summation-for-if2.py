str_N = input("please enter a number: ")
N = int(str_N)

summation = 0
for x in range(3,N+1,3):
    print(x)
    summation = summation + x

print(f"summation of 1..{N} only divisible by 3 is {summation}")

# while
# for loop

str_N = input("please enter a number: ")
N = int(str_N)

x = 3
summation = 0
while x <= N: 
    print(x)
    summation = summation + x
    x = x + 3

print(f"summation of 1..{N} only divisible by 3 is {summation}")

# while
# for loop

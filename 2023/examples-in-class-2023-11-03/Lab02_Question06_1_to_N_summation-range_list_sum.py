str_N = input("please enter a number: ")
N = int(str_N)

# create a range, start = 3, end = N+1 and step = 3
r1 = range(3,N+1,3)
# change this range to list
l1 = list(r1)
# built in function sum accepts list as input
summation = sum(l1)

print(f"summation of 1..{N} only divisible by 3 is {summation}")


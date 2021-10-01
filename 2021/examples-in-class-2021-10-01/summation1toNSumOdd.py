strN = input("Please enter a number:")
N = int(strN)

#N = 10
numbers_to_sum = list(range(1,N+1,2)) 
total = sum(numbers_to_sum)
print("summation 1..",N,"for odd numbers is",total)

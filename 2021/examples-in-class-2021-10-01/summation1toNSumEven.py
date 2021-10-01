strN = input("Please enter a number:")
N = int(strN)

#N = 10
numbers_to_sum = list(range(0,N+1,2)) 
total = sum(numbers_to_sum)
print("summation 1..",N,"for even numbers is",total)

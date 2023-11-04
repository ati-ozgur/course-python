str_dividend = input("Please enter a dividend number for division: ")
str_divisor = input("Please enter a divisor number for division: ")

dividend  = float(str_dividend)
divisor = float(str_divisor)
# if divisor is 0, below line gives error 
# and whole program crashes
result = dividend / divisor
print(f"division of {dividend}/{divisor}={result}")



print("hello")



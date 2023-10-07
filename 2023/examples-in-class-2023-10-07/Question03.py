str1 = input("please enter an integer number N")

n1 = int(str1)

total = n1 * (n1 + 1) / 2


# no need to change f-string works
print(f"total is {total}" )

# here with comma, print puts space between the outputs
print("total is", total)
# with +, we need to change number(float) total to string using str function
print("total is " + str(total))



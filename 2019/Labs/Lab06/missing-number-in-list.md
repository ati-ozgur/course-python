
# Question: One number is missing, find it

You have a list of number between 1-100 in a list of size 99. 
One number is missing in this list.
How can you find it.
Start with following code.


    from random import sample 
    numbers = sample(range(1,101),99)
    print(numbers)


## One number in a list is missing, find it

You have a list of number between 1-100 in a list of size 99. 
One number is missing in this list.
How can you find it.
Start with following code.


    from random import sample 
    numbers = sample(range(1,101),99)
    print(numbers)

### Extra functionality 

Generalize above function so that it takes supposed min and max values in the list.
For example, it should work with list of numbers with minimum and maximum values as below.

- 50-100
- 1000-2000
- 10-20

Always input list size is the (maximum-minimum-1).


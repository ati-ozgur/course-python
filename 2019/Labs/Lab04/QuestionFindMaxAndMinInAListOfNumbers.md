## Find Max and Min in a List of Numbers

You will ask the users a list of numbers that are separated by spaces.

For example:

    str_list_of_numbers = input("please enter a list of numbers")

Please write a code that find max and min of these numbers and print them out.
String function split should be useful for you.

    In [98]: str_list_of_numbers = "1 12 15 21 -3 45 999 0 23"
    In [100]: str_list_of_numbers
    Out[100]: '1 12 15 21 -3 45 999 0 23'
    In [101]: str_list_of_numbers.split(" ")
    Out[101]: ['1', '12', '15', '21', '-3', '45', '999', '0', '23']


Example output: 

    str_list_of_numbers = input("please enter a list of numbers")
    1 12 15 21 -3 45 999 0 23
    min number: -3
    max number: 999


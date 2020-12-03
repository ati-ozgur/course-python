## Conditionals Statements (if-elif-else)


Python uses if, elif and else statements for branching operations

Only if

	if condition1:
		block-if

if-else block

	if condition1:
		block-if
	else:
		block-else


if-elif-else block. This block also used similar to switch statements in other languages.

	if condition1:
		block-if
	elif condition2:
		block-elif
	else:
		block-else




### Short example


    n = int(input("Please enter an integer: "))
    if x < 0:
        print('A negative number is entered')
    elif x == 0:
        print('Zero is entered')
    else:
        print('A positive number is entered')



### Sample Question 1

Following function, is_negative should return True for negative numbers. 
Fill the blanks

	def is_negative(x):
		.....
	    return ___


### Sample Question 2

Following function, greeting should return German greeting according to 24 hours.
Normally, before 12, you say Guten Morgen, between 12 and 18 you use Guten Tag, after 18 but before 22 you use Guten Abend, then you use Gute Nacht.

Fill the blanks

	def greeting_in_german(hour):
		.....
	    return ___

### Sample Question 3

A complex password should satisfy following conditions

	- At least 9 characters long
	- At least contains 1 upper case and 1 lower case character
	- At least contains 1 number
	- At least contains 1 character from following special character list "!#$%&()*+,-./:;<=>?@[\]^_{|}"

please write following function.

	def is_password_complex(password):
		.....
	    return ___


### Sample Question 4

What is the output of following code:

	number = 100
	if number > 110: 
	  print("block if")
	elif number != 110:
	  print("block elif1")
	elif number >= 90 or number < 120:
	  print("block elif2")
	else:
	  print("block else")



### Other tutorials

- [if-elif-else in python tutorial](https://docs.python.org/3/tutorial/controlflow.html#if-statements)


- [W3C Schools python conditions](https://www.w3schools.com/python/python_conditions.asp)

- [Python If ... Else in w3schools.com](https://www.w3schools.com/python/python_conditions.asp)

- [Non-Programmer's Tutorial for Python 3/Decisions](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Decisions)

- [Conditional Statements in Python 101](https://python101.pythonlibrary.org/chapter4_conditionals.html)


### Video tutorials

1. [Video If, Then, Else in Python](https://www.youtube.com/watch?v=f4KOjWS_KZs).

Note: On this video, raw_input (Python 2) is used. For python 3, you need to use input().




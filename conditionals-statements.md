## Conditionals Statements (if-elif-else)


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



### Other tutorials

1. See [if-elif-else in python tutorial](https://docs.python.org/3/tutorial/controlflow.html#if-statements)


2. [W3C Schools python conditions](https://www.w3schools.com/python/python_conditions.asp)



### Video tutorials

[Video 1](https://www.youtube.com/watch?v=f4KOjWS_KZs).

Note: On this video, raw_input (Python 2) is used. For python 3, you need to use input().




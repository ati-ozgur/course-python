# Example Questions 2020-11-12


1. Write a function that give title case for an input.
For example given full names below, output will be capitalized as only first char.


- atilla ozgur --> Atilla Ozgur 
- atiLLa ozgur --> Atilla Ozgur 
- Atilla Ozgur --> Atilla Ozgur 
- ATILLA OZGUR --> Atilla Ozgur 
- AtiLLA OZGur --> Atilla Ozgur 


2. Write a code that checks if a given number is prime number.


3. Write a number guess game. 
At the start of your program, you will choose a random integer between 0-100. 
Your user will try to find this number.
You will answer guesses from your user as:
	- too low
	- too high
	- you have found the number


4. write a function that finds the missing number from a list that contains number between 1 to 100. Your list size is 99 therefore one number is missing find it.

you can use following code to create example lists for your self.

	import random
	l1 = random.sample(range(1,101),99)


5. generalize above function so that it takes supposed min and max values in the list.
For example, it should work with list of numbers with minimum and maximum values as below.

- 50-100
- 1000-2000
- 10-20

Always input list size is the (maximum-minimum-1).



6. Write a function get_first_digit that finds a first digit of a number without using string functions. You should use only math library or mathematical normal operations.
your function should give true on the following asserts

	assert get_first_digit(12021) == 1
	assert get_first_digit(92021) == 9
	assert get_first_digit(72003443) == 7


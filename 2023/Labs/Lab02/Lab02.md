# Lab01 2023-10-21

Questions goes from simpler to harder.

## Question 01: Input and Print 1

Ask the use following inputs in different lines.
	
	- Their name
	- Their birth year
	- Their country

An example input

	- Atilla
	- 1977
	- Türkiye

Then calculate their age and output to screen (print) following.

	Hello Atilla, you are 46 years of old and you are from Türkiye.


## Question 02: Input and Print 2

Please write a simple Celsius to Fahrenheit and Fahrenheit  to  Celsius converter.
Ask user first which unit they want to convert, C or F.
Then ask the value. 

Conversion formulas are below.

	C = (F - 32) * 5/9

	
	F = (C * 9/5) + 32


An example run:


Which unit you want to convert, C or F: F
Value of Fahrenheit: 50

50 Fahrenheit equals to 10 Celsius


## Question 03: simple error 1

please look at [wrong_code1.py](wrong_code1.py). Fix its errors so that it runs correctly.


## Question 04: simple error 2

please look at [wrong_code2.py](wrong_code2.py). Fix its errors so that it runs correctly. 
There are logical errors on this code.



## Question 05: Palindrome

**Palindrome** from wikipedia.

    A palindrome is a word, number, phrase, or other sequence of characters 
    which reads the same backward as forward, such as taco cat or madam or racecar or the number 10801. 


Please write a code that finds if given input is a palindrome. 
For example: efe,  hannah, ava, anna are palindromes.
Test your code with above examples and test with at least 3 different non-Palindrome examples.
nixon, example, xxxzz
For our purposes space and whitespace characters are distinct characters; therefore, "taco cat" is not a palindrome.

Example output: 

    Please enter a input to test for palindrome: 123
    Input text 123 is not a Palindrome.

    Please enter a input to test for palindrome: 1221
    Input text 1221 is a Palindrome.

    Please enter a input to test for palindrome: madam
    Input text madam is a Palindrome.



## Question 06 1..N Summation - ( 10 points)

Write a python code that gets an input number N from user and finds summation 1..N only divisible by 3 numbers.
For example, N = 10, then summation is 3+6+9 = 18.



## Question 07 (3 5 15) (three five fifteen) 

Write a program which prints the numbers up to 100.
For every number, your program should write normal number, but numbers divisible by three it should print out English word three, for numbers divisible by 5, it should print out English word five and for numbers divisible by 15, it should print out fifteen.
An example output is below:

	1
	2
	three
	4
	five
	three
	7
	8
	three
	five
	11
	three
	13
	14
	fifteen
	16
	17



## Question 08:  Write a number guess game. 

At the start of your program, you will choose a random integer between 0-100. 
Your user will try to find this number.
You will answer guesses from your user as:
	- too low
	- too high
	- you have found the number


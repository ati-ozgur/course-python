# Lab01 2023-10-07 

Questions goes from simpler to harder.

## Question 01: Simple Hello World

Please write a simple hello world example with saying your full name and your country of origin.

## Question 02: Print

Ask user for their name, birthday and country information and print this information in the screen.

## Question 03: summation

 write a code that find summation of 1..N, where N is an integer given by a user.
You should use standard summation formula in the calculation
You do not need loop.

## Question 04: Greatest among 3 numbers

Please write a program which find the greatest number among three numbers.
You will ask the user for these three numbers and print greatest of them in the screen.


## Question 05: simple error 1

please look at [wrong_code1.py](wrong_code1.py). Fix its errors so that it runs correctly.


## Question 06: simple error 2

please look at [wrong_code2.py](wrong_code2.py). Fix its errors so that it runs correctly. There are logical errors on this code.

## Question 07: simple random password

Create simple program which will print out random password of length 8 in the screen.
You do not need loops for simple solution of this question.

following code snippets are useful:

	import string
	print(string.printable)
	print(string.printable[25])
	print(string.ascii_letters)
	print(string.ascii_letters[20])


Python [random module](https://docs.python.org/3/library/random.html) is also necessary.

We can use following code to get [random integers](https://www.w3schools.com/python/ref_random_randint.asp):

	import random
	print(random.randint(3, 9)) 


## Question 08: generation nickname

Ask user for their birth year and print out generation nickname.


| Generation nickname     |  years            |
|-------------------------|-------------------|
| The Greatest Generation | born 1901 to 1924 |
| The Silent Generation   | born 1928 to 1945 |
| Baby Boomers            | born 1946 to 1964 |
| Generation Jones        | born 1955 to 1965 |
| Generation X            | born 1965 to 1980 |
| Xennials                | born 1977 to 1983 |
| Millennials             | born 1981 to 1996 |
| Generation Z            | born 1997 to 2010 |
| Generation Alpha        | born after 2011   |

For example Baby Boomers: Baby boomers were born between 1946 and 1964; therefore, for a birth year of 1960, you will print out. 

You have born in 1960. You are a baby boomer.


## Question 09: Palindrome

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

## Question 10:  Write a number guess game. 

At the start of your program, you will choose a random integer between 0-100. 
Your user will try to find this number.
You will answer guesses from your user as:
	- too low
	- too high
	- you have found the number


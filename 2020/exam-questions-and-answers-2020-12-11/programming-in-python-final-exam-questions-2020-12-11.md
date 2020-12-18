# Programming in Python Exam 2020-12-11

## Instructor Atilla Özgür

- Student Name: 
- Student LastName
- Student No:

## Summary

Make a backup copy of the exam-questions folder before starting the exam.
If you make a mistake, it will be easier to return back to your backup copy.
Every question is worth 10 points.
Question difficulty increases with question numbers.


## Question 01 wrong arguments

Look at the question_wrong_arguments.py file.
Make a copy  of this file as answer_wrong_arguments.py.
Fix the compile problems of this program.

## Question 02 compile problems

Look at the question_tree_command.py file.
Make a copy  of this file as answer_tree_command.py.
Fix the compile problems of this program.
There are only simple (most of them one char) problems in this program.
A necessary character is missing or need to replaced.

## Question 03 compile and logical problems

Look at the question_born_year.py file.
Make a copy  of this file as answer_born_year.py.
Fix the compile and logical bugs of this program.
When the code fixed, it should give an output similar to following.


	please enter your age:
	43
	hello, you were born in 1977

## Question 04 compile and logical problems

Look at the question_print_division.py file.
Make a copy  of this file as answer_print_division.py.
Fix the compile and logical problems of this program.
When the code fixed, it should give an output similar to following.
Look at errors and exception handling topics in your references, if you do not know these problems.

	Types are not compatible <class 'str'> and <class 'str'>, check your inputs
	Zero division error occurred, check your inputs
	result: 2.0
	else part:no error
	result: 5.0
	else part:no error


## Question 05 printing stars

Please write a code so that you will see the following output on the screen.
Name your python file as printing_stars.py

### star rectangle with edge 5 

	*
	**
	***
	****
	*****


## Question 06 list comprehension

Look at the question_summation_with_list_comprehension.py file.
Make a copy  of this file as answer_summation_with_list_comprehension.py.
Write a **one line list comprehension** so that list l1 filtered and only numbers divisible by 7 in the new_list.


	l1 = list(range(100))
	new_list = # list comprehension is here filter numbers divisible by 7
	print(sum(new_list))


When your code is working, output of this code should be 735.




## Question 07 (2 5 10) (two five ten)

Write a program that prints the numbers from 1 to 100. 
But for multiples of 2 print "two" instead of the number and for the multiples of 5 print "five". 
For numbers which are multiples of both 2 and 10 print "ten".
Name your python file as two_five_ten.py




## Question 08 is number a prime number

Write a function named is_prime. This function should return True or False according to given input number.
Name your python file as answer_is_prime.py
Test your function is_prime with the numbers between 1-20.


## Question 09 find digits of number
Write a function named find_digits which returns digits of a given number as an list of integers.
You should either use string functions/indexing for this question or mathematical operators of \\ integer division or % modulus.
Name your python file as answer_find_digits.py


Example run

	print(find_digits(100))
	print(find_digits(987))
	print(find_digits(121))
	print(find_digits(34543))
	print(find_digits(4567))

Example code

	[1, 0, 0]
	[9, 8, 7]
	[1, 2, 1]
	[3, 4, 5, 4, 3]
	[4, 5, 6, 7]



## Question 10 Palindrome

Definition of **Palindrome** from wikipedia.

    A palindrome is a word, number, phrase, or other sequence of characters 
    which reads the same backward as forward, 
    such as taco cat or madam or racecar or the number 10801. 

If we give some palindrome number examples:

- 121
- 3443 
- 34543

Some not palindrome numbers

- 321
- 4567 
- 123421

Please write a code that finds if given input number is palindrome?


**Note** Please do not use string library functions.
Use the function you have written in the find_digits question.
It is not a problem if you have used string functions in the find_digits.

Example output: 

	Please enter a number to test: 123
	Number 123 is not a Palindrome.
	Please enter a number to test: 1221
	Number 1221 is a Palindrome.


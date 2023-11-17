---
title: Programming in Python Exam
date: 2022-12-20
---

# Programming in Python Exam 2022-12-20

## Instructor Atilla Özgür

- Student Name: 
- Student LastName
- Student No:

## Summary

Make a backup copy of the exam-questions folder before starting the exam.
If you make a mistake, it will be easier to return back to your backup copy.
Every question has information how many points it is worth.
Question difficulty increases with question numbers.


In the folder reference books, you have access to following two books and python docs

- Non-Programmer's Tutorial for Python 3
- Python101
- python-docs


## Question 01 wrong arguments (10 points)

Look at the [question_wrong_arguments.py](question_wrong_arguments.py) file.
Make a copy  of this file as answer_wrong_arguments.py.
Fix the compile problems of this program.
You should be able to run this python file from command line.



## Question 02 compile problems (10 points)

Look at the [question_classtree.py](question_classtree.py) file.
Make a copy  of this file as answer_classtree.py.
Fix the compile problems of this program.
There are only simple (most of them one char) problems in this program.
A necessary character is missing or need to replaced.


## Question 03 simple temperature conversion functions (10 points)

Look at the [question_temperature_conversion.py](question_temperature_conversion.py)
Make a copy  of this file as answer_temperature_conversion.py.
In this file, you will write two functions that will convert Celsius to Fahrenheit and Fahrenheit to Celsius.
Your functions should return converted values.
When you run temperature_conversion.py file, asserts should run correctly.
Use below formulas for conversion:


- Fahrenheit = (Celsius * 9/5) + 32
- Celsius = (Fahrenheit - 32) * 5/9




## Question 04 ASCII Table for English Alphabet - ( 10 points)

Look at the [question_ascii_alphabet.py](question_temperature_conversion.py) file for starting.
Make a backup copy of this file as answer_ascii_alphabet.py
You should write your answer in this answer_ascii_alphabet.py.

Write a python code that outputs ASCII characters for English Alphabet both for lower and upper case characters.
Your code should output total of 52 (26 upper case + 26 lower case characters)
You can use standard python ord and chr functions.



## Question 05 (3 4 12) (three four twelve) (10 points)

Write a function that returns a list.
Look at the code of [question_three_four_twelve.py](question_three_four_twelve.py).
Make a backup copy as answer_three_four_twelve.py.
You should write your answer in this answer_three_four_twelve.py.

You need to fill empty function,create_list_three_four_twelve, with your code.
The lists returned from this function will consists of numbers from 1 to max_number (included) but for multiples of 3  "three" instead of the number; and for the multiples of 4, "four"; and for numbers which are multiples of both 3 and 4, "twelve".
If you write your function correctly, both asserts should not give you any error.


## Question 06 find min max (10 points)

Look at the file [question_find_min_max.py](question_find_min_max.py).
Save as this file answer_find_min_max.py.
Without using python max and min functions, you need to write two functions which finds minimum and maximum number in a given list.
Your functions find_min and find_max, should return minimum and maximum number respectively in a given input list.
If your written code is correct, asserts should not give you any error.

## Question 07 random passwords (10 points)

Create a answer_random_password.py file.
In this new file, please write a function that creates a random password for a user.
Password length should be a parameter for this function and should be 12.
Use that function to create random passwords for 1000 users.
Following code snippets are useful for this question.

	import string
	print(string.ascii_uppercase)
	Out: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	import random as rnd
	print(rnd.randint(1,10))
	Out: 7




# Question 08 digit total of 21 but all 3 digits are different (10 points)

You are asked to find 3-digit numbers which have a digit summation of 21.
But all of their digits should be different from each other.
For example, 498, 786, 948 fit this definition.

According to this definition, how many different natural numbers can be written?

# Question 09 Recursive Fibonacci numbers

Look at the [question_fibonacci.py](question_fibonacci.py). 
You need to fill empty function definition of fibonacci with correct recursive python code.
Do not forget that fibonacci definition is as follows:

F0 = 1, F1 = 1
Fn = Fn-1 + Fn-2

For example:
F6 = F5 + F6

If your written code is correct, asserts should not give you any error.

## Question 10 list comprehension

Look at the [question_summation_with_list_comprehension.py](question_summation_with_list_comprehension.py) file.
Make a copy  of this file as answer_summation_with_list_comprehension.py.
Write a function that will filter numbers according to given input list and  number. 
Your function will consists of a **one line list comprehension** so that given filtered and only numbers divisible by given input number are in the new_list.

If your written code is correct, asserts should not give you any error.
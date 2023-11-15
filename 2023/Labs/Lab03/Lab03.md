# Lab03 2023-11-04

Questions goes from simpler to harder.

## Question 01:  Simple hello function

Please write a simple hello function with three arguments, name, birth_day and country.
Call this function two times

	- your information 
 	- one of your friend's information

possible output

	Hello Atilla, you have born 1977 and you are from Türkiye.
	Hello Duru, you have born 2012 and you are from Türkiye.


## Question 02:  Is Number odd or even function

Write two functions which checks a given number if the number is odd or even.
Write your code using [run_is_odd_or_even.py](run_is_odd_or_even.py)
Asserts in the above should work if your function works correctly


## Question 03: simple error 1

please look at [wrong_code1.py](wrong_code1.py). 
Fix its errors so that it runs correctly.

## Question 04: 
Please try to solve [Find first digit without string functions](../../../course-content/questions/find-first-digit.md)


## Question 05: 
Please try to solve [Stars pyramid](../../../course-content/questions/star-pyramid-1.md)

## Question 06 (3 4 12) (three four twelve)

Write a program which prints the numbers up to 100.
For every number, your program should write normal number, but numbers divisible by three it should print out English word three, for numbers divisible by 4, it should print out English word four and for numbers divisible by 12, it should print out twelve.
An example output is below:

	1
	2
	three
	four
	5
	three
	7
	four
	three
	10
	11
	twelve
	13
	14
	three
	four
	17


## Question 07: 
Please try to solve [prime number](../../../course-content/questions/prime-number.md)

## Question 08: 
Please try to solve [prime number recursion](../../../course-content/questions/prime-number_recursion.md)

## Question 09:  Sentence in a frame

Write a function that takes two input, sentence and frame character. 
This function should return a multiline string which surrounds every word in the sentence with a frame character. 
For example

```python
sentence_in_frame("Jacobs University 2023 Class", "+")
```

Then output would be following

	++++++++++++++
	+ Jacobs     +
	+ University +
	+ 2023       +
	+ Class      +
	++++++++++++++

## Question 10 list comprehension

Look at the [question_summation_with_list_comprehension.py](question_summation_with_list_comprehension.py) file.
Make a copy  of this file as answer_summation_with_list_comprehension.py.
Write a function that will filter numbers according to given input list and  number. 
Your function will consists of a **one line list comprehension** so that given filtered and only numbers divisible by given input number are in the new_list.

If your written code is correct, asserts should not give you any error.
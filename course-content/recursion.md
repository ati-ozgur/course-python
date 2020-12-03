# recursion


## Real life example 1

Russian dolls are good example for recursion.

![wikipedia-Russian-Matroshka](images/wikipedia-Russian-Matroshka.jpg)


## First example

Recursive functions calls itself.


	def recursive(x):
		# do something
		x = x - 1
		print(x)
		recursive(x)


But this way without any exit condition will lead to error.
See below.


	In [1]: def recursive(x):
	   ...: ^I# do something
	   ...: ^Ix = x - 1
	   ...: ^Irecursive(x)
	   ...:

	In [2]: recursive(10)
	10
	9
	..
	-2968
	-2969
	-2970
	-2971
	-2972
	-2973
	-2974
	-2975
	-2976
	---------------------------------------------------------------------------
	RecursionError                            Traceback (most recent call last)
	<ipython-input-2-88ae67f210a8> in <module>
	----> 1 recursive(5)

	<ipython-input-1-c9aaee61b136> in recursive(x)
	      3         x = x - 1
	      4         print(x)
	----> 5         recursive(x)

	... last 1 frames repeated, from the frame below ...

	<ipython-input-1-c9aaee61b136> in recursive(x)
	      3         x = x - 1
	      4         print(x)
	----> 5         recursive(x)

	RecursionError: maximum recursion depth exceeded while calling a Python object



We need to add an exit condition to our function.
This is sometimes called base case, function returns no value or return a default value effectively exiting.



	def recursive(x):
		# do something
		x = x - 1
		print(x)
		if (x > 0):
			recursive(x)
		# else do nothing, exit from function


Then, a recursive function will have following structure.

	def recursive(parameters):
	    if check parameters:
	    	# exit or return
	        return base_case_value
	    # modify parameters here and call itself again
	    recursive(modified_parameters)



## Recursive Function structure

A recursive function is a function that calls itself.

1. we have function that call itself
2. we have an exit condition
3. we should somehow change our input variables so that exit condition will eventually be TRUE.


## pseudo code 1

	if exit_condition_true:
		exit function
	else:
	  change input variable
		call itself again

## pseudo code 2

	if not exit_condition_true:
	  change input variable
		call itself again
	else:
		exit function


See following [stackoverflow question](https://softwareengineering.stackexchange.com/questions/25052/in-plain-english-what-is-recursion)


## Examples

### Factorial 

Factorial example used widely for recursion but it is not a good example in my opinion since it could be easily solved with loops also.

### Fibonacci

### Tree structures

- Most tree structures. For example going through a family tree and searching files in operating system.

### Files in a folder

1. getting list of files and directories in a given directory and going deeper in existing directories to search for a given text or filename.
Consider a folder in operating system. 
Starting from a this base folder, print names of all files in this folder. 
If this folder contains sub folder, you need also print file names in sub folder too.
This should go recursively.

This is a better example for recursion since it is not easily solved with loops.
In general, any tree structure are more easily solved using recursion.



### More reading for recursion


- [google search for recursion](https://www.google.com/search?q=recursion)

- [wikipedia recursion](https://en.wikipedia.org/wiki/Recursion)


## Links in our references

- [Non-Programmer's Tutorial for Python 3/Recursion](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Recursion)



## Video Tutorials


- [Recursion video 1](https://www.youtube.com/watch?v=zbfRgC3kukk)

- [Recursion video 2](https://www.youtube.com/watch?v=seUpFY_m-us)

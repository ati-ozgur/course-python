# recursion

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


### Files in a folder

Consider a folder in operating system. 
Starting from a this base folder, print names of all files in this folder. 
If this folder contains sub folder, you need also print file names in sub folder too.
This should go recursively.

This is a better example for recursion since it is not easily solved with loops.
In general, any tree structure are more easily solved using recursion.


## Links References

- [Non-Programmer's Tutorial for Python 3/Recursion](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Recursion)



## Video Tutorials


- [Recursion video 1](https://www.youtube.com/watch?v=zbfRgC3kukk)

- [Recursion video 2](https://www.youtube.com/watch?v=seUpFY_m-us)

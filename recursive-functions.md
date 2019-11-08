# recursive functions



Russian dolls are good example for recursion.

![wikipedia-Russian-Matroshka](images/wikipedia-Russian-Matroshka.jpg)



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


A recursive function will have following structure.

	def recursive(parameters):
	    if check parameters:
	    	# exit or return
	        return base_case_value
	    # modify parameters here and call itself again
	    recursive(modified_parameters)



### Example of Recursion

- getting list of files and directories in a given directory and going deeper in existing directories to search for a given text or filename.

- Most tree structures. For example going through a family tree and searching


- [google search for recursion](https://www.google.com/search?q=recursion)

- [wikipedia recursion](https://en.wikipedia.org/wiki/Recursion)
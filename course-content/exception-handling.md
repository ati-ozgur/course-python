# Exception Handling


Try following code


	print(1/0)


You should see following error

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero


This example seems meaningless why should we knowingly divide a number by zero.
But, consider that we get this values from end user.


	a = 1 # from user input
	b = 0 # from user input


Or, we need to read a file from system and this filename is again given by user.



	filename = "a.txt" # from user input
	# try to read content with wrong file name


We will again get an error.


Solution is to surround would be problematic lines with try...except statements
See below examples

## Examples

- [Exception example: file reading 1](Examples/exception_handling/exception_example3_file1.py)
- [Exception example: file reading 2](Examples/exception_handling/exception_example3_file2.py)
- [Exception example: file reading 3](Examples/exception_handling/exception_example3_file3.py)



## try..except


## try..except..else

Else part runs if there is no error.

## try..except..else..finally

finally part **always** runs.

## exception handling hierarchy

- see [exception hierarchy in python document](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
- see [following code for generating Python error classes hierarchy](Examples/exception_handling/print_exception_hierarchy.py)
- see this article about [this topic too](https://airbrake.io/blog/python/class-hierarchy)

## Links in our references

- [Python 101: Exception Handling](https://python101.pythonlibrary.org/chapter7_exception_handling.html)

- [Non-Programmer's Tutorial for Python 3/Dealing with the imperfect](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Dealing_with_the_imperfect)



## other references

- [exceptions in real python](https://realpython.com/python-exceptions/)
- [Python Try Except in w3schools.com](https://www.w3schools.com/python/python_try_except.asp)


## Video Tutorials





# comparisons boolean variables


	In [1]: print( 5 > 2)
	True

	In [2]: print( 5 < 2)
	False

	In [3]: print( 2 == 2)
	True

	In [4]: print( "2" == 2)
	False

	In [5]: print( 1 != 2)
	True

	In [6]: print( 1 < "1")
	---------------------------------------------------------------------------
	TypeError                                 Traceback (most recent call last)
	<ipython-input-6-eef05bdfaefd> in <module>
	----> 1 print( 1 < "1")

	TypeError: '<' not supported between instances of 'int' and 'str'




## Question what is the result of following code execution? Why?

	print("Bremen" > "bremen")


See [Ascii table](https://www.asciitable.com/) for answer to this question.



### Logical operators and, or, not

- and operator returns true if both sides are true
- or operator return trues if one of the sides are true
- not reverse the boolean, False -> True, True -> False


	In [1]: birth_year = 1999

	In [2]: birth_year < 2000 and birth_year < 2019
	Out[2]: True

	In [3]: birth_year < 1900 or birth_year > 1950
	Out[3]: True

	In [4]: not (birth_year < 1900 or birth_year > 1950 )
	Out[4]: False


## Links in our references


- [boolean-operations](https://python101.pythonlibrary.org/chapter4_conditionals.html#boolean-operations)
- [Non-Programmer's Tutorial for Python 3/Boolean Expressions](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Boolean_Expressions)
- [Python Booleans in w3schools.com](https://www.w3schools.com/python/python_booleans.asp)


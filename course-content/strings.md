# strings


Strings are defined using either double quotes "" or single quotes. ''


    name1 = "Atilla"
    name2 = 'Atilla'


If we need to use single quote inside a string enclosed by single quotes, we need to escape it using backslash \ character.
Like below:

    name2 = 'Atilla\'s Car'

To avoid using escape characters, it is recommended that:

- use double quote for enclosing your string, if you need to use single quote in your string, 

    ex1 = "Atilla's Car"

- use single quote for enclosing your string, if you need to use double quote in your string, 

    ex2 = 'Atilla said that "please open your notebooks"'




Multiline string are defined using 3 quotes.

    multi_line_string1 = """ Hello
        this is multi line string
    """

    multi_line_string2 = ''' Hello
        this is another multi line string
    '''

To change other variable to string, we use **str** function


    a = 5
    print("number is " + str(a))


#### String Formatting

Python 3.6 introduced [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) for easy string formatting.
We will use them in our classes.
Variable name is enclosed between curly braces in the string.


    age = 42
    print(f"Age is {age}")


output is

    Age is 42





#### Common string methods

    since strings are immutable in python, all of the methods returns a modified string and do not modify original string.

    - lower()  lowercase
    - upper()  lowercase
    - strip()  strips whitespace from both sides of string
    - lstrip  strips whitespace from left side of string
    - rstrip  strips whitespace from right side of string

    count(substring) how many time substring occurs
    isnumeric()
    isalpha() True if only alphabetic characters exists
    split(), split(delimiter)   return list of substrings, splited by whitespace/delimiter

#### Common string operations/functions


    len(string)
        Returns the length of the string
    for character in string:
        # do something

        iterates over character in string

    substring in string  return True if substring in string

    string[i] we can use list indexing with string.

    see [all string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)



In [1]: name = "atilla"

In [2]: len(name)
Out[2]: 6

In [3]: for ch in name:
   ...:     print(ch)
   ...:
a
t
i
l
l
a

In [4]: "t" in name
Out[4]: True

In [5]: "x" in name
Out[5]: False

In [6]: name[0]
Out[6]: 'a'

In [7]: name[-1]
Out[7]: 'a'

In [8]: name[2:4]
Out[8]: 'il'

In [9]: name[2:5]
Out[9]: 'ill'

In [10]: name[2:6]
Out[10]: 'illa'



## More

- [python f-strings](https://realpython.com/python-f-strings/)





## Links in our references


- [Python Strings in python101](https://python101.pythonlibrary.org/chapter2_strings.html)

- [Python Strings in w3schools.com](https://www.w3schools.com/python/python_strings.asp)

- [Non-Programmer's Tutorial for Python 3/Who Goes There?](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Who_Goes_There%3F)

- [Non-Programmer's Tutorial for Python 3/Revenge of the Strings](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Revenge_of_the_Strings)

## Video Tutorials

- [Video Tutorial Strings](https://www.youtube.com/watch?v=UsCQXe1OHZk)

- [Python Single vs. Double Quotes - Which Should You Use And Why? | Better Data Science](https://www.youtube.com/watch?v=yR384WW0kOg&t=3s)

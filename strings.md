## strings


Strings are defined using either double quotes "" or single quotes. ''


    name1 = "atilla"
    name2 = 'atilla'


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

Python 3.6 introduced f-strings for easy string formatting.
We will use them in our classes.
Variable name is enclosed between curly braces in the string.


    age = 42
    print(f"Age is {age}")


output is

    Age is 42


- [W3C Schools Python string](https://www.w3schools.com/python/python_strings.asp)
- [Video Tutorial Strings](https://www.youtube.com/watch?v=UsCQXe1OHZk)
- [python f-strings](https://realpython.com/python-f-strings/)



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



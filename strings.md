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


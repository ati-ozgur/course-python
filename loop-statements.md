## Loop Statements


### While

    while condition_is_true:
        do_something



When you use while loops, you need to first initialize your loop variable, and you need to also modify that variable so that loop will finish at some time.

no initialization example:

    while x < 10: 
        print(x) 

Output will be like below.


    In [1]:     while x < 10:
       ...:         print(x)
       ...:
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-1-c956f313d152> in <module>
    ----> 1 while x < 10:
          2     print(x)

    NameError: name 'x' is not defined

Not modifying condition variable. Following code will be infinite loops of 1 until you close the program or use CTRL-c.

    x = 1
    while x < 10: 
        print(x) 


correct solution should be.


    x = 1
    while x < 10: 
        print(x) 
        x = x +1



- [W3C Schools python While Loop](https://www.w3schools.com/python/python_while_loops.asp)
- [Video Tutorial While Loop 1](https://www.youtube.com/watch?v=jSs58VZVLw8)



### For

For statement in python iterates over any sequence.
This sequence can be a list, range or any iterable.
Below, we iterate over a name list

    >>> name_list = ["Atilla","Funda","Duru"]
    >>> for name in name_list:
    ...    print(name)
    ...
    Atilla
    Funda
    Duru
    >>>


for statement mostly used with [range](range.md).


    >>> for i in range(10):
    ...    print(i)
    ...
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    >>>





- break
- continue 
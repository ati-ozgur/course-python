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


## Links References


- [Python wiki while](https://wiki.python.org/moin/WhileLoop)
- [W3C Schools python While Loop](https://www.w3schools.com/python/python_while_loops.asp)
- [while loop in Non-Programmer's Tutorial for Python 3](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Count_to_10)

 - [while loop in Python 101](https://python101.pythonlibrary.org/chapter5_loops.html#the-while-loop)


## Video Tutorials

- [Video Tutorial While Loop 1](https://www.youtube.com/watch?v=jSs58VZVLw8)





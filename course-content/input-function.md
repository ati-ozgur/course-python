# input function

We use input function to get user input from user.
Input function always gives string input.
If we need to change it to other types, we need to cast them.



See following examples:

## input example 1

```python
print("Please give me your Name")
name = input()
print("Hello",name)
print(f"Hello {name}, I am from XX")
print("Where are you from?")
country = input()
print(f"Hello {name} from {country}")

```


[Download above code example](Examples/input_example.py)


## input example 2 changing data type


```python
print("Please give your name")
name = input()
print("hello",name)
print("please enter your birth year")
birth_year_str = input()
birth_year = int(birth_year_str)
age = 2023-birth_year
print(f"hello {name}, you are {age} years old")
```


[Download above code example input code 2 - changing type from string](Examples/input_example_type_change.py)



## Links in our references

- [input in Non-Programmer's Tutorial for Python 3](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Who_Goes_There%3F)

- [Python User Input in w3schools.com](https://www.w3schools.com/python/python_user_input.asp)



## Video Tutorials


- [Video 1: input function](https://youtu.be/8m6oyM2sFts)
- [Video 2: input function](https://youtu.be/ArL54Nmx9oU)

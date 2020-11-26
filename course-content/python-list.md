## Lists


Strings are defined using [] or list() construction.


    empty_list = []
    list_of_numbers = [1,3,5]


Adding new members to list

    new_list = [1,3]
    new_list = new_list + [2,4]
    print(new_list)
    # Or
    a_list = [1,3]
    a_list.append(2)
    a_list.append(4)


Indexing list is done via [index]

    new_list[0]
    # negative indexing start from end
    new_list[-1]

Slicing of lists. We can get slices from list using following notation.

    a_list[start_index:end_index]

important part here, end_index item is not included in the slicing.


    >>> a_list = list(range(10))
    >>> a_list
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> a_list[2:5]
    [2, 3, 4]


length of list is found using **len** function


    print(len(new_list))

we can use item in list to find if a item in the list.

    a_list = ["Jacobs","university","is","in","Germany"]
    "Germany" in a_list


## List specific methods

    list[index] = new_item
    list.append(item)
    list.insert(index, item)
    list.pop(index)
    list.remove(item)
    list.sort()
    list.reverse()
    list.clear()
    list.copy()
    list.extend(another_list) appends all elements of another_list to list


## list comprehension

See [python comprehension](python-comprehensions.md)



## Links References

- [Non-Programmer's Tutorial for Python 3/Lists](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Lists)
- [W3C Schools Python lists](https://www.w3schools.com/python/python_lists.asp)

- [Non-Programmer's Tutorial for Python 3/More on Lists](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/More_on_Lists)

- [Lists in Python 101](https://python101.pythonlibrary.org/chapter3_lists_dicts.html)

- [Python Lists in w3schools.com](https://www.w3schools.com/python/python_lists.asp)

- [using lists as array in w3schools.com](https://www.w3schools.com/python/python_arrays.asp)

## Video Tutorials


- [Video Tutorial Lists 1](https://youtu.be/tw7ror9x32s)
- [Video Tutorial Lists 2](https://youtu.be/ohCDWZgNIU0)



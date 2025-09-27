# Using other modules and packages

## Python modules

As we have seen before, if a module is in standard library, simple import is enough.


```python
import math
```


## Directory/files

As we have talked before, we can use our own modules very easily, if they are in the same directory or sub-directories.


```python
import example
```




## use package manager (PIP)

If we use a package manager like PIP to install a package. We can easily use it.

	python -m pip install emoji

then



```python
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
```

see longer [PIP](PIP-en.md) explanation in course notes.


## Where this modules are stored?


```python
import sys
print(sys.path)

```

## You can add sys.path 

If you add to sys.path any directory, you will be able to import it anywhere in your computer.



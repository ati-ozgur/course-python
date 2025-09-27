# importing modules

Apart from [built-in-functions](python-built-in-functions), most functions are stored in python modules.
For example, we can not use floor function by itself.
First we need to import math module like below

```python
import math
```


otherwise we will get an error saying floor is not defined.

```python
a = 1.7
floor(a)
#Traceback (most recent call last):
#  File "<pyshell>", line 1, in <module>
#NameError: name 'floor' is not defined
import math
math.floor(a)

from math import floor
floor(a)

```


# Random Passwords

Please write a code that creates a random password for 1000 users.


Following codes should be helpful for you.

- [List of ascii and printable chars for python](https://stackoverflow.com/questions/5891453/is-there-a-python-library-that-contains-a-list-of-all-the-ascii-characters)

    
    >>> import string
    >>> string.ascii_uppercase
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> string.printable
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ \t\n\r\x0b\x0c'


- Random number example

    In [41]: import random as rnd
    In [42]: rnd.randint(1,10)
    Out[42]: 7

    In [43]: rnd.randint(1,10)
    Out[43]: 10

    In [44]: rnd.randint(1,10)
    Out[44]: 2


**Note** for password generation normally cryptographic random generation should be used. This example is learning example and should not be used for real password generation.

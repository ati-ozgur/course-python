RandomPasswords.md

Please write a code that creates a random password for 1000 users.


Following codes should be helpful for you.

- [List of ascii and printable chars for python](https://stackoverflow.com/questions/5891453/is-there-a-python-library-that-contains-a-list-of-all-the-ascii-characters)

    
    >>> import string
    >>> string.ascii_uppercase
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> string.printable
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ \t\n\r\x0b\x0c'


- Random number example




**Note** for password generation normally cryptographic random generation should be used. This example is learning example and should not be used for real password generation.

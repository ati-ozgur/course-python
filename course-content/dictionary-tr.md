# python Sözlük (Dictionary)


Sözlük tanımlama

```python

d = {}
# veya
dict = {anahtar1:deger1, anahtar2:deger2} 
```

Sözlük operasyonları

```python
len(dict) 

for anahtar in dict:
    print(anahtar)

for anahtar,deger in dict.items():
    print(anahtar,deger)


anahtar in dict # a


dict[anahtar] 

dict[anahtar] = deger

del dict[anahtar]

dict.keys() # anahtar listesini liste olarak al
dict.values() # değer listesini liste olarak al
dict.items() # anahtar, değer listesini al
dict.clear() # sözlükteki tüm öğeleri siler

```

Sözlük içinde anahtar kontrolü

```python
d = {}
d["a"] = 10
"a" in d
#True
"b" in d
#False
```

## Referanslarımızda bu konu

 - [official documentation for dictionary](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

 - [Non-Programmer's Tutorial for Python 3/Dictionaries](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Dictionaries)

 - [Dictionaries in Python 101](https://python101.pythonlibrary.org/chapter3_lists_dicts.html)

 - [Python Dictionaries in w3schools.com](https://www.w3schools.com/python/python_dictionaries.asp)

## Vidyo Öğreticiler








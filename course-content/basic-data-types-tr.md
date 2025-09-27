# Python Temel Veri tipleri

- Sayılar
    - tam sayılar
    - kayan noktalı sayılar
    - karmaşık sayılar
- betikler (string)
- Boole (doğru/yanlış)

## Değişken sınıf adını veya türünü bulma

**type** fonksiyonunu kullanın.

```python
a = 5
type(a)
# int
```



## Tiper Arası Dönüştürme/Dönüştürme

Farklı tipler geçmek için nesne fonksiyonlarını kullanın.

    int
    float
    bool
    str
    complex






## + operatör aynı tiplerle çalışır

```python
print("hello" + " world")
#hello world

print(10+1)
#11

print(10 + "8")

print("hello" + 10)

```

```
-----------------------------------------------------
TypeError Traceback (most recent call last)
<ipython-input-10-38035139b14a> in <module>
----> 1 print(10 + "8")

TypeError: unsupported operand type(s) for +: 'int' and 'str'

In [11]: 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-11-9d2092f62421> in <module>
----> 1 print("hello" + 10)

TypeError: can only concatenate str (not "int") to str

```

Bu sorunu nasıl çözebiliriz? 
Nesne değiştirme fonksiyonlarını kullanarak türlerini değiştirebilirim.


```python
print(10 + int("8"))
#18

print("hello" + str(10))
#hello10
```


## Diğer Öğreticiler 


- [Python Data Types in w3schools.com](https://www.w3schools.com/python/python_datatypes.asp)

- [casting in w3schools.com](https://www.w3schools.com/python/python_casting.asp)


## Vidyo Öğreticiler

- [Data Types in Python](https://youtu.be/gCCVsvgR2KU)


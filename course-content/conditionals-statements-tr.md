# Koşullu İfadeler (if-elif-else)

Python, koşullu işlemler için if (eğer), elif ve else (yoksa) ifadelerini kullanır


## Sadece if

```python
if condition1:
	block-if

```

```python
a = 10
if a > 0:
    print("positif sayı")
```

Burada a (10 değeri) 0'dan büyük olduğundan ekrana "pozitif sayı" yazdırılır.

```python
a = 0
if a > 0:
    print("positif sayı")
```

Burada a (0 değeri), 0'dan büyük değildir, ekrana **hiçbir** şey yazdırılmaz.



## if-else bloku

```python
if koşul1:
	blok-if
else:
	blok-else
```


```python
a = 10
if a > 0:
    print("positif sayı")
else:
    print("negatif sayı")
```

Here since a is 10 and it is greater than 0, "positive number" is printed in the screen.
else block does not run since if block is already run.


```python
a = -10
if a > 0:
    print("positif sayı")
else:
    print("negatif sayı")
```

Burada a -10 olduğundan ve 0'dan büyük olmadığından, ekrana "pozitif sayı" yazılmaz.
Aksi takdirde blok çalışır ve ekrana "negatif sayı" yazdırılır.



## if-elif-else blok 

Bu blok diğer dillerdeki switch ifadelerine benzer şekilde kullanılır.

```python
if condition1:
	block-if
elif condition2:
	block-elif
else:
	block-else
```


```python
a = 10
if a > 0:
    print("positif sayı")
elif a == 0:
    print("sıfır")
else:
    print("negatif sayı")
```



## Kısa Örnek


```python
x = int(input("Please enter an integer: "))
if x < 0:
    print('A negative number is entered')
elif x == 0:
    print('Zero is entered')
else:
    print('A positive number is entered')
```


```python
str_input = input("Enter years of experience of python")
x = int(str_input)
#Please enter an integer: 1
if x < 0:
        x = 0
        print('Negative experience is not possible')
        print('changed to zero')
    elif x == 0:
        print('Ah, you are just beginning')
        print("welcome to class")
    elif x == 1:
        print('A Junior Programmer')
        print('May be you will learn some things')
    else:
        print('A python expert in our class')

```

### Örnek Soru 2

Aşağıdaki fonksiyon, **is_negative** negatif sayılar için True değerini döndürmelidir.
Boşlukları doldurun

```python
def is_negative(x):
	.....
    return ___
```


### Örnek Soru 3

Aşağıdaki fonksiyonda, greeting_in_german 24 saate göre Almanca selamlama döndürmelidir.

Normalde:

- saat 12'den önce "Guten Morgen" denir.
- 12 ile 18 arasında "Guten Tag" kullanılır.
- 18'den sonra, ancak 22'den önce "Guten Abend" kullanılır
- ardından "Gute Nacht" kullanılır.

Boşlukları doldurun.

```python
def greeting_in_german(hour):
	.....
    return ___
```

### Örnek Soru 4

Karmaşık bir parola aşağıdaki koşulları karşılamalıdır.

- En az 9 karakter uzunluğunda olmalıdır.
- En az 1 büyük harf ve 1 küçük harf içermelidir.
- En az 1 rakam içermelidir.
- "!#$%&()\*+,-.\/:;<=>\?\@\[\]\^\_\{\}" özel karakter listesinden en az 1 karakter içermelidir.


Lütfen aşağıdaki fonksiyonu yazın.


```python

def parola_karmasik_mi(parola):
	.....
    return ___
```


### Örnek Soru 5

Aşağıdaki kodun çıktısı nedir?


```python
number = 100
if number > 110: 
  print("block if")
elif number != 110:
  print("block elif1")
elif number >= 90 or number < 120:
  print("block elif2")
else:
  print("block else")
```



## Referanslarımızda bu konu

- [if-elif-else in python tutorial](https://docs.python.org/3/tutorial/controlflow.html#if-statements)


- [W3C Schools python conditions](https://www.w3schools.com/python/python_conditions.asp)

- [Python If ... Else in w3schools.com](https://www.w3schools.com/python/python_conditions.asp)

- [Non-Programmer's Tutorial for Python 3/Decisions](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Decisions)

- [Conditional Statements in Python 101](https://python101.pythonlibrary.org/chapter4_conditionals.html)


### Vidyo öğreticiler





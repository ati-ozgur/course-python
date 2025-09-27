# While

## İlk örnek

```python
while koşul_doğru:
    bir_şeyler_yap
```



```python
a = 0            
while a < 10:
    a = a + 1
    print(a)
```

While döngülerini kullandığınızda, önce döngü değişkeninizi belirlememiz ve arkasından döngünün sonlanması için bu değişkeni değiştirmeniz gerekir.



## Başlatma olmayan örnek

```python
while x < 10: 
    print(x) 
```


Çıktı aşağıdaki gibi olacaktır.

```
NameError                                 Traceback (most recent call last)
<ipython-input-1-c956f313d152> in <module>
----> 1 while x < 10:
      2     print(x)

NameError: name 'x' is not defined
```

## Sonsuz döngü

Koşul değişkenini değiştirmezsek sonsuz döngü olacaktır.
Aşağıdaki kod, programı kapatana veya CTRL-c kullanana kadar 1'li sonsuz döngü halinde olacaktır.


```python
x = 1
while x < 10: 
    print(x) 
```

Doğru çözüm şu şekilde olmalıdır.


```python
x = 1
while x < 10: 
    print(x) 
    x = x +1
```


## Referanslarımızda bu konu


- [Python wiki while](https://wiki.python.org/moin/WhileLoop)
- [while Loop in w3schools.com](https://www.w3schools.com/python/python_while_loops.asp)
- [while loop in Non-Programmer's Tutorial for Python 3](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Count_to_10)

 - [while loop in Python 101](https://python101.pythonlibrary.org/chapter5_loops.html#the-while-loop)


## Vidyo Öğreticiler

- [Video Tutorial While Loop 1](https://www.youtube.com/watch?v=jSs58VZVLw8)





# İstisnalar ile çalışma (exception handling)

Aşağıdaki kodu deneyin


```python
print(1/0)
```



Aşağıdaki hatayı görmelisiniz

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

```


Bu örnek anlamsız görünüyor.
Neden bilerek bir sayıyı sıfıra bölelim ki?
Ancak, bu değerleri son kullanıcıdan aldığımızı düşünün.


```python
a = 1 # from user input
b = 0 # from user input
```


Ya da sistemden bir dosya okumamız gerekiyor ve bu dosyanın adı yine kullanıcı tarafından verilmiş olsun.


```python
dosya_adı = "a.txt" # kullanıcı girdisinden
# yanlış dosya adına sahip içeriği okumayı deneyin
```


Tekrar bir hata alacağız.

Çözüm, sorunlu olabilecek satırları try...except ifadeleriyle çevrelemektir.
Aşağıdaki örneklere bakın.


## Örnekler

- [Exception example: file reading 1](Examples/exception_handling/exception_example3_file1.py)
- [Exception example: file reading 2](Examples/exception_handling/exception_example3_file2.py)
- [Exception example: file reading 3](Examples/exception_handling/exception_example3_file3.py)



## try..except


## try..except..else

Hata yoksa else kısmı çalışır.

## try..except..else..finally

finally kısmı **her zaman** çalışır.

## exception handling hierarchy

- see [exception hierarchy in python document](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
- see [following code for generating Python error classes hierarchy](Examples/exception_handling/print_exception_hierarchy.py)
- see this article about [this topic too](https://airbrake.io/blog/python/class-hierarchy)

## Referanslarımızda bu konu

- [Python 101: Exception Handling](https://python101.pythonlibrary.org/chapter7_exception_handling.html)

- [Non-Programmer's Tutorial for Python 3/Dealing with the imperfect](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Dealing_with_the_imperfect)



## Diğer Referanslar

- [exceptions in real python](https://realpython.com/python-exceptions/)
- [Python Try Except in w3schools.com](https://www.w3schools.com/python/python_try_except.asp)


## Vidyo Öğreticiler







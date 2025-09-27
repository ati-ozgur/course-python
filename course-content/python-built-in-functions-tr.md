# Python Dahili (built-in) fonksiyonları

Python'un birçok dahili fonksiyonu vardır.
Bu fonksiyonları herhangi bir kütüphaneyi içe aktarmadan (import) kullanabilirsiniz.
[Tam listeyi buradan](https://docs.python.org/3/library/functions.html) görebilirsiniz.

Kursumuzda aşağıdaki fonksiyonları öğreneceğiz.
Merak ediyorsanız, açıklamalarını [Python dokümanlarından](https://docs.python.org/3/library/functions.html) okuyabilirsiniz.

- abs
- dir
- id
- input
- int
- isinstance
- issubclass
- len
- list
- map
- min
- open
- print
- range
- set
- sorted
- str
- sum
- super
- type


Bu fonksiyonları kendi tanımlarınızla ezebilirsiz ancak bu önerilmez.
Aşağıdaki örneğe bakalım.


```python
abs(-2.0)                   
abs = 2             

abs(-2.0)                
```

```python
# result
TypeError Traceback (most recent call last)
<ipython-input-4-8449d55e35d8> in <module>
----> 1 abs(-2.0)
TypeError: 'int' object is not callable
```


## Dahili fonksiyon adlarını nasıl hatırlarsınız?

Dahili fonksiyonların adlarını hatırlamak zorunda değilsiniz, bunlara Python dokümanlarından veya doğrudan Python çalıştırken bakabilirsiniz.
Etkileşimli kabukta aşağıdakileri yazarsak, büyük bir liste görmeliyiz.
Bu listedeki tüm küçük harfli isimler dahili fonksiyonlardır.
Deneyin ve görün.


```python
dir(__builtins__)
```


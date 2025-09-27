# importing modules


[Dahili fonksiyonlar](python-yerleşik-fonksiyonları) dışında çoğu fonksiyon Python modüllerinde saklanır.
Örneğin, floor fonksiyonunu tek başına kullanamayız.
Öncelikle aşağıdaki gibi math modülünü içe aktarmamız (import) gerekiyor.


```python
import math
```



Aksi takdirde 'floor' is not defined (tanımlanmadı) hatası alırız.

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


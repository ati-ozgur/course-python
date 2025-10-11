#  Python Anlamalar (Comprehensions)


## Liste anlamaları (Comprehensions)


Döngüler olmadan liste oluşturmanın bir yoludur.
Döngüler yerine anlamalar daha okunabilir bir çözüm olabilir.
Herhangi bir liste anlaması normal döngü olarak yazılabilir.

Aşağıdaki Python döngüsü ile başlayalım.
Bu döngü 0'dan 9'a kadar sayıların karelerini oluşturur.
Elde edilen sayılar 0,1,4,9,...81 olmalıdır.



```python
l2 = []
for x in range(10):
    l2.append(x*x)
print(l2)
```

Liste anlama kodu şu şekilde olurdu:

```python
l1 = [x*x for x in range(10)]
print(l1)
```

Basit liste anlama şablonu:

[ifade **for** parça **in** yinelenebilir]

Bir başka örnek.
Betiklerden oluşan bir listeyi tam sayılardan oluşan bir listeye dönüştürme


```python
str_list = ["1", "2", "3", "4", "5"]
int_list = [int(x) for x in str_list]
```


Yukarıdaki örnekte görüldüğü gibi, anlamaların içerisinde fonksiyon kullanabiliriz.

```python
name_list = ["atilla","aydın","duru"]

l2 = []
for name in name_list:
    l2 = l2 + [name.capitalize()]
print(l2)

l1 = [name.capitalize() for name in name_list]
print(l1)
```


### Filtreleme

Listeyi filtrelemek yaygın bir işlemdir.
Döngü sürümü:
	
```python
l2 = []
for x in range(10):
	if x % 3 == 1:
	    l2.append(x*x)
print(l2)
```

Liste anlamada, yinelemedeki öğeleri isteğe bağlı if ile de filtreleyebiliriz

```python
l2 = [x*x for x in range(10) if x % 3 == 1]
print(l2)
```




## Çift döngü örneği

Aşağıdaki kod for döngüsünü kullanarak çiftler oluşturur:

```python
ciftler2 = []
for i in range(3):
    for c in ["a","b","c"]:
        ciftler.append((i, c))

print(ciftler2)
```

Anlama versiyonu daha kısadır.

```python
ciftler1 = [(i, c) for i in range(3) for c in ["a","b","c"]]

print(ciftler1)
```



### Liste anlamlara yönelik öğreticiler/vidyolar

- [Güzel blog yazısı](https://towardsdatascience.com/11-examples-to-master-python-list-comprehensions-33c681b56212)
- [real python list comprehension tutorial](https://realpython.com/list-comprehension-python/)
- İyi bir vidyo öğreticisi: [Python Tutorial: List Comprehensions Step-By-Step
](https://youtu.be/1HlyKKiGg-4)


## Sözlük Anlamaları (Comprehensions)

Sözlük Anlama, liste anlama ile oldukça benzerdir.
[] yerine sözlük sembolü {} kullanılır.
Aşağıdaki kod, sözlük ve for döngüsü kullanarak kareler versiyonunu oluşturur.


```python
kareler = {}
for x in range(5):
    kareler[x] = x * x

print(kareler)
```

Sözlük Anlama daha kısadır.


```python
kareler = {x: x * x for x in range(5)}

print(kareler)
```


## Küme Anlamaları (Set Comprehensions)

Küme anlamaları, liste anlamalarına çok benzer; kümeler oluşturmak için [] yerine {} kullanın.
Kümeler oluşturduğumuz için **hiçbir yineleme** yoktur yani tekrar edilen eleman yoktur.
Çıktı sırasız olabilir.

Aşağıdakiler liste oluşturur:

```python
sayi_listesi = [x % 3 for x in range(10)]
print(sayi_listesi)
```
Aşağıdaki kod küme oluşturur

```python
sayi_kumesi = {x % 3 for x in range(10)}
print(sayi_kumesi)
```

Çıktı farklı olacaktır.

- sayi_listesi:  [0, 1, 2, 0, 1, 2, 0, 1, 2, 0] 
- sayi_kumesi:  {0, 1, 2}

Küme versiyonunda mükerrer (tekrar eden) eleman yoktur.

## Referans kitaplarımız da bu konu

- [Python 101 book: Python Comprehensions](https://python101.pythonlibrary.org/chapter6_comprehensions.html)
- [Python tutorial: list-comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)






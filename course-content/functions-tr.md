# Fonksiyonlar

Python'da str, print ve input gibi dahili fonksiyonlar bulunur.
Ancak aşağıdaki gibi kendi fonksiyonlarımızı da tanımlayabiliriz.


```python
def merhaba_de(isim):
	print("merhaba " + isim)
```




Burada **def** anahtar sözcüğü, fonksiyonu tanımlamak için kullanılır.
Parantezlerin arasında fonksiyon argümanlarını tanımlarız.
Burada yalnızca bir argüman vardır: isim.
Parantezleri kapattıktan sonra, fonksiyon satırını tanımlamayı tamamlamak için çift nokta : kullanırız.
Python'da boşluk önemlidir; bu nedenle, çift noktadan sonra fonksiyon kod satırları için biraz boşluk bırakmamız gerekir.

Tanımladığımız fonksiyonları normal şekilde kullanabiliriz.

```python
def merhaba_de(isim):
	print("merhaba " + isim)


merhaba_de("Atilla")
#merhaba Atilla

merhaba_de("Duru")
#merhaba Duru

```



## Daha fazla parametre içeren örnek

## Varsayılan parametreler içeren örnek

## Değer döndüren fonksiyonlar


Bir fonksiyon hiçbir şey döndürmüyorsa (return kullanmıyorsa), varsayılan olarak hiçbir şey (None) döndürür.
Örneğin:

```python
def merhaba_de2(name):
   print("hello " + name)

ret = merhaba_de2("atilla")
print(ret)
#hello atilla
#None
```


merhaba_de2 fonksiyonu return anahtar kelimesini kullanmadığından, Python'un özel türü olan None'u döndürür.


## Değiştirme örneği

```python
a = 2
b = 4

def swap(a, b):
    temp = a
    a = b
    b = temp
swap(a, b)
print(a, b)

```



## Referanslarımızda bu konu

- [Non-Programmer's Tutorial for Python 3/Defining Functions](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Defining_Functions)

- [Non-Programmer's Tutorial for Python 3/Advanced Functions Example](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Advanced_Functions_Example)

- [Functions in Python 101](https://python101.pythonlibrary.org/chapter10_functions.html)

- [Python Functions in w3schools.com](https://www.w3schools.com/python/python_functions.asp)

## Vidyo Öğreticiler




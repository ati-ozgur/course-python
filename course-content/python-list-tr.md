# Listeler


Python listeleri [] veya list() yapısı kullanılarak tanımlanır.



```python
bos_list = []
sayi_listesi = [1,3,5]
```


**Listeler yeni üye ekleme**

Listeye yeni üyelere eklemek için, append veya + kullanılır.


```python
yeni_list = [1,3]
yeni_list = yeni_list + [2,4]
print(yeni_list)
# veya
a_list = [1,3]
a_list.append(2)
a_list.append(4)
```



**liste indeksleme**

Liste içindeki elemanlara ulaşmak için [index] kullanılır.

```python
yeni_list[0]
# negatif değerler ile sondan üyelere ulaşılır.
yeni_list[-1]
```


**liste dilimleme**

Aşağıdaki yapıyı kullanarak listelerden bir başka listeyi dilim kesme mantığında elde edebiliriz.
İndeksleme sonucunda eleman elde edilir.
Dilimleme sonucunda başka bir liste elde edilir.


```python
a_liste[başlangıc:bitiş:adım]
```


Dikkat edilmesi gereken nokta bitiş dilimlemeye dahil edilmez.
Buradaki mantık, range kullanımı ile aynıdır.

```python
bir_liste = list(range(10))
print(bir_liste)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l1 = bir_liste[2:5]
print(l1)
#[2, 3, 4]
l2 = bir_liste[:5:2]
print(l2)
#[0, 2, 4]
l_cift = bir_liste[::2]
print(l_cift)
#[0, 2, 4, 6, 8]
l_tek = bir_liste[1::2]
print(l_tek)
#[1, 3, 6, 7, 9]
```


Örneğin bu yapıyı kullanarak listenin tersini bulabiliriz.


```python
bir_liste = list(range(10))
print(bir_liste)
ters_liste = bir_liste[::-1]
print(ters_liste)
```



**liste içindeki eleman kontrolü**

**in** kullanarak bir elemanın liste içinde olup olmadığını kontrol edebiliriz.

```python
l1 = ["Jacobs","university","is","in","Germany"]
if "Germany" in l1:
    print("liste içinde")
```

## List fonksiyonları


Liste uzunluğunu bulmak için **len** fonksiyonu kullanılır.
```python
print(len(yeni_liste))

list[indeks] = yeni_öğe
list.append(öğe)
list.insert(indeks, öğe)
list.pop(indeks)
list.remove(öğe)
list.sort()
list.reverse()
list.clear()
list.copy()
list.extend(başka_liste) 
#appends all elements of başka_liste to list
```

## python liste anlamaları (comprehensions)

Bakınız [python anlamaları](python-comprehensions-tr.md):

## Kurs vidyo

- [Python listeler](https://www.youtube.com/watch?v=7-iQhIoSXak)


## Referans kitaplarımız da bu konu

- [Non-Programmer's Tutorial for Python 3/Lists](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Lists)
- [W3C Schools Python lists](https://www.w3schools.com/python/python_lists.asp)

- [Non-Programmer's Tutorial for Python 3/More on Lists](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/More_on_Lists)

- [Lists in Python 101](https://python101.pythonlibrary.org/chapter3_lists_dicts.html)

- [Python Lists in w3schools.com](https://www.w3schools.com/python/python_lists.asp)

- [using lists as array in w3schools.com](https://www.w3schools.com/python/python_arrays.asp)

## Vidyo Öğreticiler


- [İngilizce Öğretici List 1](https://youtu.be/tw7ror9x32s)
- [İngilizce Öğretici List 2](https://youtu.be/ohCDWZgNIU0)



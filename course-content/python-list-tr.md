# Listeler


Python listeleri [] veya list() yapısı kullanılarak tanımlanır.


    bos_list = []
    sayi_listesi = [1,3,5]

**Listeler yeni üye ekleme**

Listeye yeni üyelere eklemek için, append veya + kullanılır.

    yeni_list = [1,3]
    yeni_list = yeni_list + [2,4]
    print(yeni_list)
    # veya
    a_list = [1,3]
    a_list.append(2)
    a_list.append(4)


**liste indeksleme**

Liste içindeki elemanlara ulaşmak için [index] kullanılır.

    yeni_list[0]
    # negatif değerler ile sondan üyelere ulaşılır.
    yeni_list[-1]


**liste dilimleme**

Aşağıdaki yapıyı kullanarak listelerden bir başka listeyi dilim kesme mantığında elde edebiliriz.
İndeksleme sonucunda eleman elde edilir.
Dilimleme sonucunda başka bir liste elde edilir.


    a_liste[başlangıc_indeks:bitis_indeks]


Dikkat edilmesi gereken nokta bitis_indeks dilimlemeye dahil edilmez.
Buradaki mantık, range kullanımı ile aynıdır.


    >>> bir_liste = list(range(10))
    >>> bir_liste
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> bir_liste[2:5]
    [2, 3, 4]


Liste uzunluğunu bulmak için **len** fonksiyonu kullanılır.



    print(len(yeni_liste))

**liste içindeki eleman kontrolü**

**in** kullanarak bir elemanın liste içinde olup olmadığını kontrol edebiliriz.


    bir_liste = ["Jacobs","university","is","in","Germany"]
    if "Germany" in bir_liste:
        print("liste içinde")


## List fonksiyonları

    list[index] = new_item
    list.append(item)
    list.insert(index, item)
    list.pop(index)
    list.remove(item)
    list.sort()
    list.reverse()
    list.clear()
    list.copy()
    list.extend(another_list) appends all elements of another_list to list


## python liste kavrayışları (comprehensions)

Bakınız [python comprehensions](python-comprehensions-tr.md):



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



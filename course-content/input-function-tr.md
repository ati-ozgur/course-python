# Girdi (input) fonksiyonu

Kullanıcıdan girdi almak için **input** fonksiyonunu kullanılır.

## input örnek 1

```python
print("İsminizi yazınız")
name = input()
print("Merhaba",name)

```
## input örnek 2

input fonksiyonuna bir string argümanı da verebiliriz.

```python
name = input("İsminizi yazınız")
print("Merhaba",name)
```

## input örnek 3


```python
print("İsminizi yazınız")
isim = input()
print("Merhaba",isim)
print(f"Merhaba {isim},Ben XX'ten geliyorum")
print("Hangi ülkeden geliyorsunuz?")
ulke = input()
print(f"Merhaba {isim} {ulke}'ten gelen")

```

[Download above code example](Ornekler/input_ornek.py)


Giriş fonksiyonu her zaman string sonucu verir.
Eğer onu başka tiplere çevirmemiz gerekirse,  dönüştürme fonksiyonlarını kullanmamız gerekir.


## input örnek 4: Veri tipini değiştir


```python
print("İsminizi yazınız")
isim = input()
print("Merhaba",isim)
print("lütfen doğum yılınızı girin")
dogum_yili_str = input()
dogum_yili = int(dogum_yili_str)
yas = 2023-dogum_yili
print(f"Merhaba {isim}, {yaş} yaşındasın")
```


[Download above code example input code - changing type from string](Ornekler/input_ornek_tip_degistir.py)



## Referans kitaplarımız da bu konu

- [input in Non-Programmer's Tutorial for Python 3](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Who_Goes_There%3F)

- [Python User Input in w3schools.com](https://www.w3schools.com/python/python_user_input.asp)



## Vidyo Öğreticiler


- [Video 1: input function](https://youtu.be/8m6oyM2sFts)
- [Video 2: input function](https://youtu.be/ArL54Nmx9oU)

# döngü sezgisi

## bir şeyi tekrarlamak

Bir şeyi tekrarlamak en kolay döngüdür.
Örneğin, adınızı ekrana 4 kez yazmak.

	Atilla
	Atilla
	Atilla
	Atilla

Yukarıdakileri Python'da while veya for döngüleriyle başarabiliriz.
Nasıl çalıştıklarını göreceğiz.

## Sayıları artırma

Bu da yine çok yaygın bir döngü türüdür.
Örneğin, 1'den 10'a kadar sayıları yazdırmak.
Bu gereksinim yine while veya for döngüleriyle karşılanabilir.

```python
1
2
3
4
5
6 
7
8
9 
10
```
Bunu Python kodu olarak yazarsak.


```python
index = 1
while index <= 10:
	print(index)
	index = index + 1
```

## toplam sayısı 1..N

1..10'un toplamını bulmak istiyoruz.


```python
1 = 1
1+2 = 3
1+2+3 = 6
1+2+3+4 = 10
1+2+3+4+5 = 15
1+2+3+4+5+6  = 21
1+2+3+4+5+6+7 = 28
1+2+3+4+5+6+7+8 = 36
1+2+3+4+5+6+7+8+9  = 45
1+2+3+4+5+6+7+8+9+10 = 55
```



```python
 1       = 1
(1)  + 2 = 3
(3)  + 3 = 6
(6)  + 4 = 10
(10) + 5 = 15
(15) + 6 = 21
(21) + 7 = 28
(28) + 8 = 36
(36) + 9 = 45
(45) +10 = 55

```


Bunu Python kodu olarak yazarsak.


```python
index = 1
total = 0
while index <= 10:
	total = total + index
	index = index + 1

print(total)
```

1..N ile çalışacak şekilde değiştirin


```python
index = 1
last_number = 10
total = 0
while index <= last_number:
	total = total + index
	index = index + 1

print(total)
```
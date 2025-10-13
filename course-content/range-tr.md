# range fonksiyonu

range fonksiyonunun 3 çeşidi vardır.

	range(bitiş)
	range(başlangıç,bitiş)
	range(başlangıç,bitiş,adım)


Eğer başlangıç değeri verilmez ise varsayılan olarak 0 düşünülür.
Eğer adım değeri verilmez ise varsayılan olarak 1 alınır.
Bundan dolayı 

	range(5)
	0,1,2,3,4

değerlerini üretir.
Üretilen değerleri görmenin 2 yolu vardır.

1. For döngüsü kullanarak 
2. listeye çevirerek


```python
for x in range(5):
	print(x)
```

veya

```python
l1 = list(range(5))
print(l1)
```



range fonksiyonu matematikteki [başlangıç,bitiş) kavramına yakındır.
Bundan dolayı bitiş degeri sonuçlarda yoktur.


- range(n) --> [0,n) 
- range(n+1) --> [0,n]
- range(başlangıç,n) --> [bitiş,n) 


Örneğin aşağıdaki kodların çıktısına bakalım:

```python
baslangıc = 5
bitis = 10
adim = 2
for x in range(bitis):
	print(x)

for x in range(baslangıc,bitis):
	print(x)



for x in range(baslangıc,bitis,adim):
	print(x)
```


Başlangıç, bitiş ve adım değerleri ayarlanarak tersten sayma yapılabilir.

```python
baslangıc = 20
bitis = 3
adim = -1
for x in range(baslangıc,bitis,adim):
	print(x)
```


## Kurs vidyo

- [python range](https://www.youtube.com/watch?v=FVQ_ZfUlD1o)

## Diğer öğreticiler

- [https://realpython.com/python-range/](python-range)
# Özyineleme (recursion)


## Gerçek hayattan örnek 1

Rus Matruşka bebekleri özyineleme için iyi bir örnektir.

![wikipedia-Russian-Matroshka](images/wikipedia-Russian-Matroshka.jpg)


## İlk örnek

Özyinelemeli fonksiyonlar kendini çağırır.

```python
def recursive(x):
	# do something
	x = x - 1
	print(x)
	recursive(x)

```

Ancak herhangi bir çıkış koşulu olmadan bu şekilde devam etmek hataya yol açacaktır.
Aşağıya bakınız.


```python
def recursive(x):
	# do something
	x = x - 1
	recursive(x)

recursive(10)
```

Çıktı: 

```
10
9
..
-2968
-2969
-2970
-2971
-2972
-2973
-2974
-2975
-2976
---------------------------------------------------------------------------
RecursionError                            Traceback (most recent call last)
<ipython-input-2-88ae67f210a8> in <module>
----> 1 recursive(5)

<ipython-input-1-c9aaee61b136> in recursive(x)
      3         x = x - 1
      4         print(x)
----> 5         recursive(x)

... last 1 frames repeated, from the frame below ...

<ipython-input-1-c9aaee61b136> in recursive(x)
      3         x = x - 1
      4         print(x)
----> 5         recursive(x)

RecursionError: maximum recursion depth exceeded while calling a Python object
```

Fonksiyonumuza bir çıkış koşulu eklememiz gerekiyor.
Buna bazen temel durum denir; fonksiyon hiçbir değer döndürmez veya varsayılan bir değer döndürerek çıkış yapar.


```python
def recursive(x):
	# do something
	x = x - 1
	print(x)
	if (x > 0):
		recursive(x)
	# else do nothing, exit from function

```


O zaman, özyineleme fonksiyon aşağıdaki yapıya sahip olacaktır.

```python
def recursive(parameters):
    if check parameters:
    	# exit or return
        return base_case_value
    # modify parameters here and call itself again
    recursive(modified_parameters)
```





## Özyinelemeli Fonksiyon Yapısı

Özyinelemeli fonksiyon, kendini çağıran bir fonksiyondur.

1. Kendini çağıran bir fonksiyonumuz var
2. Bir çıkış koşulumuz var
3. Çıkış koşulunun sonunda DOĞRU olması için giriş değişkenlerimizi bir şekilde değiştirmeliyiz.


## sözde kod 1

```python
if exit_condition_true:
	exit function
else:
  change input variable
	call itself again
```



## sözde kod 2

```python
if not exit_condition_true:
  change input variable
	call itself again
else:
	exit function
```



Bu soruya [stackoverflow question](https://softwareengineering.stackexchange.com/questions/25052/in-plain-english-what-is-recursion) bakın.


## Özyinelemeli Örnekler
### Faktöriyel

Faktöriyel örneği, özyineleme için yaygın olarak kullanılır, ancak döngülerle de kolayca çözülebileceği için bence iyi bir örnek değildir.

### Fibonacci

### Ağaç yapıları

- Çoğu ağaç yapısı. Örneğin, bir aile ağacını incelemek ve işletim sistemindeki dosyaları aramak.
### Klasördeki Dosyalar

1. Belirli bir dizindeki dosya ve dizinlerin listesini alma ve belirli bir metni veya dosya adını aramak için mevcut dizinlerde daha derine inme.
İşletim sisteminde bir klasörü ele alalım.
Bu temel klasörden başlayarak, bu klasördeki tüm dosyaların adlarını yazdırın.
Bu klasör alt klasörler içeriyorsa, alt klasördeki dosya adlarını da yazdırmanız gerekir.
Bu, özyinelemeli olarak yapılmalıdır.

Bu iş yapısı, döngülerle kolayca çözülemediği için özyineleme için daha iyi bir örnektir.
Genellikle, herhangi bir ağaç yapısı içeren sorular özyineleme kullanılarak daha kolay çözülür.

## Özyineleme için daha fazla okuma


- [google search for recursion](https://www.google.com/search?q=recursion)

- [wikipedia recursion](https://en.wikipedia.org/wiki/Recursion)


## Referanslarımızda bu konu

- [Non-Programmer's Tutorial for Python 3/Recursion](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Recursion)



## Vidyo Öğreticiler


- [Recursion video 1](https://www.youtube.com/watch?v=zbfRgC3kukk)

- [Recursion video 2](https://www.youtube.com/watch?v=seUpFY_m-us)

- [Recursion video 3](https://youtu.be/TO4-Px3T9Zs)
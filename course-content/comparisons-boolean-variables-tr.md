# comparisons boolean variables


```python
print( 5 > 2)
#True

print( 5 < 2)
#False

print( 2 == 2)
#True

print( "2" == 2)
#False

print( 1 != 2)
#True

print( 1 < "1")
```


Son komut, iki farklı türü (burada int ve str) karşılaştıramadığımız için aşağıdaki hatayı vermektedir.

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-eef05bdfaefd> in <module>
----> 1 print( 1 < "1")

TypeError: '<' not supported between instances of 'int' and 'str'
```






## Aşağıdaki kod çalıştırıldığında sonuç ne olur? Neden?

	print("Bremen" > "bremen")


Bu sorunun cevabı için [Ascii tablosuna](https://www.asciitable.com/) bakın.



### Mantıksal operatörler and,or,not (ve,veya,değil)

- and (ve) operatörü her iki taraf da doğruysa doğruyu döndürür

|       |       | AND   |
|-------|-------|-------|
| True  | True  | True  |
| True  | False | False |
| False | True  | False |
| False | False | False |

- or (veya) operatörü, taraflardan biri doğruysa doğruyu döndürür

|       |       | OR    |
|-------|-------|-------|
| True  | True  | True  |
| True  | False | True |
| False | True  | True |
| False | False | False |

- Not operatörü Boole değerini tersine çevirir.

	False -> True, True -> False

```python


birth_year = 1999

birth_year < 2000 and birth_year < 2019
#True

birth_year < 1900 or birth_year > 1950
#True

not (birth_year < 1900 or birth_year > 1950 )
#False
```

## Referans kitaplarımız da bu konu


- [boolean-operations](https://python101.pythonlibrary.org/chapter4_conditionals.html#boolean-operations)
- [Non-Programmer's Tutorial for Python 3/Boolean Expressions](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Boolean_Expressions)
- [Python Booleans in w3schools.com](https://www.w3schools.com/python/python_booleans.asp)



### karşılaştırma operatörleri zincirleme


TODO


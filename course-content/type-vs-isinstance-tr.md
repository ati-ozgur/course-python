# type vs isinstance

isinstance, belirli bir nesnenin bir sınıfın örneği olup olmadığını kontrol eder.
Ayrıca kalıtım olup olmadığını da kontrol eder.

type, yalnızca türlerin eşitliğini kontrol eder.

İyi bir örnek.


```python
type(True)  # bool
type(True) == int # False 
isinstance(True, int)  # True
isinstance(False, int) # True
```

Yukarıdaki örnekte boole değerleri (True,False) sayı olarak görülür çünkü True 1 ve False 0 değerine sahiptir.

```python
int(True)
# 1	
int(False)
# 0
```

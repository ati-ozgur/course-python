# Faydalı Python kod parçacıkları

## Kullanıcıdan sayı girişi alma

Yerleşik **input** fonksiyonu, komut satırında kullanıcıdan girdi almak için kullanılabilir.

**input** fonksiyonunun dönüş değeri "qerwrrqrr" gibi herhangi bir şey olabilir; kullanıcı klavyeden herhangi bir tuşa basarak girdi alabilir.
Dönüş değerini sayı olarak kullanmak istiyorsak, onu dize değerinden diğer sayılara, ondalıklı sayıya veya tam sayıya dönüştürmemiz gerekir.
Aşağıdaki kod parçacığına bakın.


```python
str_n = input("please enter a number")
N = int(str_N)
```


## herhangi bir sayıya bölünme köntrölü

"%" kalan operatörü, herhangi bir sayının başka bir sayıya bölünebilir olup olmadığını bulmak için kullanılabilir.
Aşağıdaki örneğe bakın.



```python
if n % 3 == 0: # 3'e bölünebilir
    # burada bir şey yap
    
a = 1
total = 0
while a <= 10:
    total = total + a
    a = a + 1
print(total)
N = int(str_n)
if n % 3 == 0: # 3'e bölünebilir
    # burada bir şey yap

```



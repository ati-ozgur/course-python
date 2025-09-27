# Diğer modülleri ve paketleri kullanma

## Python modülleri

Daha önce de gördüğümüz gibi, bir modül standart kütüphanedeyse, basitçe içe aktarmak yeterlidir.


```python
import math
```


## Dizin/dosyalar

Daha önce de belirttiğimiz gibi, aynı dizinde veya alt dizinlerde olmaları durumunda kendi modüllerimizi çok kolay bir şekilde kullanabiliriz.

```python
import example
```



## Paket yöneticisini (PIP) kullanın

Bir paketi yüklemek için PIP gibi bir paket yöneticisi kullanırsak, bunu kolayca kullanabiliriz.

	pip install emoji

veya

	python -m pip install emoji



sonra



```python
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
```

Ders notlarında daha uzun [PIP](PIP-tr.md) açıklamasını görün.


## Bu modüller nerede saklanıyor?


```python
import sys
print(sys.path)

```

## sys.path ekleyebilirsiniz

**sys.path**'e herhangi bir dizin eklerseniz, onu bilgisayarınızın herhangi bir yerinden kullanabilirsiniz.

TODO

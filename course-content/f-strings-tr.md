# f-strings

Python 3.6+ sürümünden sonra çalışırlar.
Kullanım olarak dizgi tanımı içinde 2 süslü parentez arasında değişken adı verilir.

	f"{degisken_adi} "


## Örnek Kodu

```python
isim = "Atilla Özgür"
ulke = "Türkiye"
ciktı = f"Benim ismim {isim} ve ben {ulke}'den geliyorum."
print(ciktı)

```


## Sabit rakamlar örneği

```python
ondalik_sayi = 1.454554
print(f"{ondalik_sayi:.2f}")
```

Elbette tarih, saat ve diğer nesneler için de biçimlendirme seçenekleri mevcuttur.

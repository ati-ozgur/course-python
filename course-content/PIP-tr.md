# PIP (Package installer for python, Python için paket yükleyici)


[PIP](https://pip.pypa.io/en/stable/), Python için paket yükleyicisidir.
Diğer paketleri yüklemek için varsayılan ve en çok kullanılan araçtır.


Aşağıdaki komutu 

	pip install paket_adi

kullanarak, paketleri [Python Paket Dizini](https://pypi.org/) adresinden yüklersiniz.
Aynı zamanda bu adreste paketleri arayabilirsiniz.
Python paket dizininde 2022-11'de 400_000'den fazla proje, 2025-11'de ise 680_000'den fazla project bulunmaktadır.
Bu python'un populerliğini göstermektedir.



Ancak aşağıdaki diğer şekillerde de kurulum yapabilirsiniz.

- proje dosyasından 
	
	python -m pip install projectfiles-1.0.zip

- git sitelerinde mesela github

	python -m pip install git+https://github.com/ati-ozgur/Pyevolve3.git@main

- Dağıtım dosyalarının kendisinden  (Özellikle proxy arkasında çalışılan firmalar için güzeldir)
	
	- Kaynak kod

	python -m pip install projectfiles-1.0.zip

	- wheel dağıtımı 	

	python -m pip install projectfiles-1.0.py3-none-any.whl



Ayrıca requirements.txt dosyalarını kullanarak birden fazla paket kurabilirsiniz

	python -m pip install -r requirements.txt


pip list ile bilgisayarınızda hangi paketlerin yüklü olduğunu görebilirsiniz.

	python -m pip list

İsterseniz herhangi bir paketi kaldırabilirsiniz


	python -m pip uninstall projectfiles
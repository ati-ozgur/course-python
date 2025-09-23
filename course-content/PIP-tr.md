# PIP (Package installer for python, Python için paket yükleyici)


[PIP](https://pip.pypa.io/en/stable/) is the package installer for python.
It is the default and most used tool for installing other packages.

Normally, you install packages from [Python Package Index](https://pypi.org/).
You can search for packages in its own web site.
As of 2022-11, python package index had more than 400_000 projects.


But you can also install from



- project files itself
	
	python -m pip install projectfiles-1.0.zip

- git repositories like github

	python -m pip install git+https://github.com/ati-ozgur/Pyevolve3.git@main

- distribution files (especially useful behind proxies)
	
	- source distribution 

	python -m pip install projectfiles-1.0.zip

	- wheel distribution 	

	python -m pip install projectfiles-1.0.py3-none-any.whl

Also you can install multiple packages using requirements.txt files

	python -m pip install -r requirements.txt


with pip list, you can see which packages are installed in your computer.

	python -m pip list

If you want, you can uninstall any package


	python -m pip uninstall projectfiles
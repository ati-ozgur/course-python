# numpy

	import numpy as np

	z = np.array([10,20]) # ndarray from python list
	z.shape

	l1 = [[1,2,3,7,8,19],[5,6,7,10,-8,19]]

	z = np.array(l1)
	z.shape

## Functions to learn


zeros
ones
empty
linspace
shape
astype
dtype
tolist
savetxt
loadtxt





	z1 = np.ones(3)
	type(z1)
	type(z1[0])


	z2 = np.linspace(1,100,20) # from 1 to 100, with 20 elements


## Broadcasting


	l1 = [[1,2,3,7,8,19],[5,6,7,10,-8,19]]

	a = np.array(l1)

	b = a1 / 2

	c = a1 * 2

	d = np.sin(a)

	e = a + b


other operations also exists, subtraction, division, addition, exponentiation ....



## Subsetting, Slicing, Indexing

Works very similar to python list indexing.

	l1 = [[1,2,3,7,8,19],[5,6,7,10,-8,19]]
	a1 = np.array(l1)
	a1[0]
	a1[1]
	a1[1,0]
	a1[1,0:4]
	a1[1,-3:-1]

see other examples in the cheat sheet

### Numpy cheat sheets

1. [Cheat Sheet 1](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
2. [Cheat Sheet 2](https://s3.amazonaws.com/dq-blog-files/numpy-cheat-sheet.pdf)


### Video tutorials

[Video Tutorial Numpy 1](https://youtu.be/xECXZ3tyONo)




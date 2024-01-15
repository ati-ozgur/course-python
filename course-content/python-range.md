# range function

range function is similar to mathematical notation [start,end). 
Therefore upper limit is not included.

- range(n) --> [0,n) 
- range(n+1) --> [0,n]
- range(start,n) --> [start,n) 


see output of following code examples:

	n = 5
	for x in range(n):
		print(x)

	for x in range(1,n):
		print(x)


	for x in range(3,n):
		print(x)

## Other Tutorials

https://realpython.com/python-range/
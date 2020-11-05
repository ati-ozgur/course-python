

def func1(a):
	pass

#func1() # TypeError: func1() missing 1 required positional argument: 'a'

func1(5) # positional calling
#func1(5,6) # TypeError: func1() takes 1 positional argument but 2 were given
func1(a=10) # name calling

def func2(a,b):
	pass


#func2(5) # TypeError: func2() missing 1 required positional argument: 'b'

func2(5,10)
func2(b=7,a=5) # if I am using named argument, I can mix the positions


def func3(a=5):
	pass

#def func4(a=5,b): #SyntaxError: non-default argument follows default argument
#	pass

func3() # has default value, works

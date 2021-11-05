# below line will give an error
# NameError: name 'ceil' is not defined
#ceil(9.6)

# Either I should import WHOLE module
import math
# then call the function as module.function_name
result = math.ceil(9.7)
print(result)
# here since math module is in standart library it works

# Second option
# from module import function_name
from math import ceil
# then I can directly use function

result2 = ceil(9.7)
print(result2)

a = math.exp(10)
from math import ceil,exp
b = exp(10)



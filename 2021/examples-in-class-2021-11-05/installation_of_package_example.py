# if the package we want to use is not in standard library
# we need to install it
# pip is standard package for this purpose
# if I get error
# ModuleNotFoundError: No module named 'pandas'
# in our shell pip install module_name
# here pip install pandas

import pandas as pd
print(pd.__version__)
#

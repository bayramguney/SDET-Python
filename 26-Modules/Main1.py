# Modules is a python file containing a set of functions you want to include in your app

# Approach 1
import Operations

Operations.add(10, 20)
Operations.mul(10, 20)

# Approach 2
from Operations import add, mul

add(10, 20)
mul(10, 20)


# Approach 3
from Operations import *

add(10, 20)
mul(10, 20)

import sys
sys.path.append("/27-Packages1-1")

#Approach1
import Module1
import Module2

Module1.display()   # This is display function from Module1
Module2.show()      # This is show function from Module2

# Approach 2
from Module1 import *
from Module2 import *

display()    # This is display function from Module1
show()       # This is show function from Module2
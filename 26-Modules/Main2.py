# Approach 1
import Animals
import Bird

Animals.fly()
Animals.color()
Bird.fly()
Bird.color()

# Approach 2
from Animals import *
fly()
color()
from Bird import *
fly()
color()
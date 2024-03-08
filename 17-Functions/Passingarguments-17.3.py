## passing arguments with default values(positional)
def func(i,j=100):
    print(i,j)
func(50)    # 50 100
func(50,250)    # 50 250

#####
def name_args(name,greeting):
    print(greeting+"  "+name)
name_args("John","Hi")  # Hi  John    positional arguments
name_args(name="John",greeting="Hi")  # Hi  John    keyword arguments
name_args(greeting="Hi",name="John")  # Hi  John    keyword arguments

def myfunc(a,b,c):
    print(a,b,c)
myfunc(10,20,30)  # 10 20 30  positional
myfunc(10,b=20,c=30)    # 10 20 30    mix arguments
myfunc(10,c=30,b=20)    # 10 20 30    mix arguments
# myfunc(12,b=20,30)    after keyword we can not continue with positional
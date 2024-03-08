i, j = 15, 25     # global variables
class MyClass:
    a, b = 12, 20   # class variables

    def add(self,x,y):   # local variables
        print(x+y)   # accessing local variables     300
        print(self.a+self.b)    # accessing class variables     32
        print(i+j)     # accessing global variables    40

mc = MyClass()
mc.add(100,200)
i, j = 15, 25  # global variables
class MyClass:
    i, j = 12, 20  # class variables

    def add(self, i, j):  # local variables
        print(i + j)  # accessing local variables     300
        print(self.i + self.j)  # accessing class variables     32
        print(globals()['i'] + globals()['j'])  # accessing global variables    40   if the local and global name are same


mc = MyClass()
mc.add(100, 200)

# 36 min

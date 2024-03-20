class A:
    x, y = 10, 20

    def m1(self):
        print("This is m1 method from class A ", self.x + self.y)


class B(A):
    a,b = 100,200
    def m2(self):
        print("This is m2 method from class B",self.a+self.b)


aobj = A()
aobj.m1()      # This is m1 method from class A  30

bobj = B()
bobj.m1()  # A  This is m1 method from class A  30
bobj.m2()  # B  This is m2 method from class B 300

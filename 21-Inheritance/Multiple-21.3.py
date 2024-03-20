class A:
    x, y = 10, 20

    def m1(self):
        print("This is m1 method from class A ", self.x + self.y)


class B:
    a,b = 100,200
    def m2(self):
        print("This is m2 method from class B",self.a+self.b)

class C(A,B):
    i,j = 1000,2000
    def m3(self):
        print("This is m3 method from class C",self.i+self.j)




aobj = A()
aobj.m1()      # This is m1 method from class A  30

bobj = B()
bobj.m2()  # B  This is m2 method from class B 300

cobj  = C()
cobj.m1()   # This is m1 method from class A  30
cobj.m2()   # This is m2 method from class B 300
cobj.m3()   # This is m3 method from class C 3000

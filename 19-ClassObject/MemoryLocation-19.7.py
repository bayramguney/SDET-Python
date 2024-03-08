class MyClass():
    def m1(self):
        pass

c1 = MyClass()
c2 = MyClass()
c3 = c1

print(id(c1))   # 1828728918848
print(id(c2))   # 1828728918704
print(id(c3))   # 1828728918848

print(c1 is c2)    # False
print(c1 is c3)    # True

# private variable can be access only within the method

class A:
    __a = 100      # private variable
    def disp(self):
        print(self.__a)

obj1 = A()
obj1.disp()     # 100
print(A.__a)    # can not access it is private

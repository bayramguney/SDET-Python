# private methods can be access only within the method

class A:
    def __disp1(self):     # private method
        print("disp1 method")

    def disp2(self):     # public method
        print("disp2 method")
        print(self.__disp1())

obj1 = A()
obj1.disp2()     # disp2 method      disp1 method
obj1.__disp1()     #  can not access it is private


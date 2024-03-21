# we can access private variable outside of class indirectly using methods

class A:
    __empId = 101

    def setempId(self,eid):
        self.__empId=eid

    def dispempId(self):
        print(self.__empId)

obj = A()
obj.dispempId()      # 101

obj.setempId(102)
obj.dispempId()    # 102

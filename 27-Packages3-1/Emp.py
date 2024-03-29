class Employee:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal

    def display(self):
        print("empId:{} empname:{} empsal:{}".format(self.eid,self.ename,self.sal))

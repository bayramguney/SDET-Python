class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def __str__(self):
        return "EmpId:{} EmpName:{} EmpSal:{}".format(self.eid, self.ename, self.sal)


e1 = Emp(1234, "Rahul", 5000)
print(e1)      # reference variable

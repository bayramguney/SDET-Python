class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def display(self):
        print("EmpId:{} EmpName:{} EmpSal:{}".format(self.eid,self.ename,self.sal))
        print("EmpId:%d EmpName:%s EmpSal:%g" %(self.eid, self.ename, self.sal))


mc = Emp(1234,"Rahul",5000)
mc.display()
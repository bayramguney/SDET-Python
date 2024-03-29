import sys

sys.path.append("C:/sdet/Phyton/27-Packages3-1")
from Emp import Employee

e=Employee(101,"Scott",4000)
e.display()         # empId:101 empname:Scott empsal:4000

sys.path.append("C:/sdet/Phyton/27-Packages3-2")
from Stu import Student

s=Student(102,"Eric",45)
s.display()      # stuId:102 stuname:Eric stugrad:45

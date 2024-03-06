"""
%d  int
%s  string
%f or %g   float
"""
name = "John"
age = 25
sal = 100.25
# approach 1
print(name, age, sal)
# approach 2
print("Name is:", name)
print("Age is:", age)
print("Salary is:", sal)
# approach 3   using %
print("Name:%s Age:%d Salary:%f" % (name, age, sal))
# approach 4
print("Name:{} Age:{} Salary:{}".format(name, age, sal))
# approach 3
print("Name:{0} Age:{1} Salary:{2}".format(name, age, sal))


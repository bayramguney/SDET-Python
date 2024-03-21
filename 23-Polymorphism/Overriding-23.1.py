class Parent:
    name = "Scott"

class Child(Parent):
    name = "David"

obj = Child()
print(obj.name)   # David   it is overriding of parent name

class Bank:
    def rateInterest(self):
        return 0

class Chase(Bank):
    def rateInterest(self):
        return 1.5

c = Chase()
print(c.rateInterest())    # 1.5    overriding the parent method

b = Bank()
print(b.rateInterest())    # 0
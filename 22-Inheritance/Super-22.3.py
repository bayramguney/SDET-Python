# invoke from constructor
class A:
    def __init__(self):
        print("constructor from class A")

class B(A):
    def __init__(self):
        print("constructor from class B")
        super().__init__()   # calls parent class constructor
        A.__init__(self)     # calls parent class constructor

bobj = B()   # constructor from class B    constructor from class A

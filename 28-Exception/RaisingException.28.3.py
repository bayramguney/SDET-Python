def enterage(age):
    if age < 0:
        raise ValueError("Only positive number")
    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")
try:
    num = -5
    enterage(num)
except ValueError:
    print("only positive number")
except:
    print("something is wrong")

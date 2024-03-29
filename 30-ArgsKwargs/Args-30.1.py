# args allow us to pass variable number of arguments to the function
def sum(*args):
    s = 0
    for i in args:
        s += i
    print(s)
sum(1, 2, 3)     # 6

def mu_three(a,b,c):
    print(a,b,c)
args = [1,2,3]   # list
mu_three(*args)           # 1 2 3

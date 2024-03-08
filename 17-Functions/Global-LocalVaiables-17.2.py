global_var = 12  # global var


def fun():
    local_var = 100  # local var
    print(global_var)  # we can access global var inside the method


# print(local_var)   we can not access local var outside the method
fun()  # 12

xy = 100
def cool():
    xy = 200
    print(xy)
cool()    # 200
print(xy) # 100

####
t =1
def increment():
    # global t = 10    incorrect
    global t
    t = 10
    print(t)

increment()   # 10
print(t)      # 10







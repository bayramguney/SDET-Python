def myfun():
    pass  # to omit the body


myfun()  # we do not get anything


def sum(start, end):
    result = 0
    for i in range(start, end + 1):
        result = result + i
    print(result)
    return result


s = sum(1, 5)  # 15
print(s)


####
def sum1(start, end):
    if start > end:
        print("start should be less than end")
        return    # no return value then will be None
    result = 0
    for i in range(start, end + 1):
        result = result + i
    return result


s1 = sum1(10, 5)
print(s1)  # None

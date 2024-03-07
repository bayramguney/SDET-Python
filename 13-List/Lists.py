# creating list
list1 = list()  # create empty list
print(list1)  # []

list2 = list([22,31,45])
print(list2)   # [22, 31, 45]

list3 = list(["tom","jerry","spy"])
print(list3)  # ['tom', 'jerry', 'spy']

list4 = list("python")
print(list4)  # ['p', 'y', 't', 'h', 'o', 'n']

# accessing list element
list5 = [1,2,3,4,5]
print(list5[1])   # 2

# common operators
print(2 in list5)   # True
print(33 not in list5)  # True
print(len(list5))  # 5
print(max(list5))  # 5
print(min(list5))  # 1

# slicing
list6 = [11,33,44,55,66,1]
print(list6[0:5])    # [11, 33, 44, 55, 66]
print(list6[:3])    # [11, 33, 44]
print(list6[2:])    # [44, 55, 66, 1]

# +   * operator
list7 = [11,33]
list8 = [22,44]
list9 = list7+list8
list10 = list7*3
print(list9)   # [11, 33, 22, 44]
print(list10)  # [11, 33, 11, 33, 11, 33]

# in   not in operator
list11 = [1,2,3,4,5]
print(2 in list11)    # True
print(7 not in list11)  # True

for i in list11:
    print(i)   # 1 2 3 4 5

# list methods
list12 = [2, 3, 4, 1, 32, 4, 56, 19]
print(list12)    # [2, 3, 4, 1, 32, 56, 19]

print(list12.count(4))   # 2   number of 4 element in the list
list13 = [33,44]

list12.extend(list13)
print(list12)  # [2, 3, 4, 1, 32, 4, 56, 19, 33, 44]

print(list12.index(4))   # 2   first index of number 4

list12.insert(1,25)
print(list12)   # [2, 25, 3, 4, 1, 32, 4, 56, 19, 33, 44]    insert 25 in 1 index

print(list12.pop(2))     # 3
print(list12)    # [2, 25, 4, 1, 32, 4, 56, 19, 33, 44]      remove the index value  2

list12.remove(56)
print(list12)     # [2, 25, 4, 1, 32, 4, 19, 33, 44]    remove the value 56

list12.reverse()
print(list12)   # [44, 33, 19, 4, 32, 1, 4, 25, 2]

list12.sort()
print(list12)    # [1, 2, 4, 4, 19, 25, 32, 33, 44]    sorted order

# list comprehension
list14 = [x for x in range(10)]
print(list14)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list14 = [x+1 for x in range(10)]
print(list14)    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list14 =[x for x in range(10) if x%2 == 0]
print(list14)   # [0, 2, 4, 6, 8]
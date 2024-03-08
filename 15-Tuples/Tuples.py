# Tuples are immutable
t1 = ()
t2 = (11, 34, 56)
t3 = ([11, 23, 45])
t4 = tuple("abc")
print(t1)  # ()
print(t2)  # (11, 34, 56)
print(t3)  # [11, 23, 45]
print(t4)  # ('a', 'b', 'c')

# methods
t5 = (1, 12, 55, 34, 78, 5)
print(len(t5))  # 6
print(min(t5))  # 5
print(max(t5))  # 78
print(sum(t5))  # 185

# iterating tuples
for i in t5:
    print(i, end=" ")  # 1 12 55 34 78 5   end is used to print at the same line

# slicing
t6 = (1, 12, 55, 34, 78, 5)
print(t6[0:4])    # (1, 12, 55, 34)
print(t6[:3])     # (1, 12, 55)
print(t6[0:])     # (1, 12, 55, 34, 78, 5)

# in   not in  operator
print(3 in t6)    # False
print(3 not in t6)  # True

# A function which has no name
# other name is anonymous function
# can take any number of args but only have one expression

x = lambda a: a + 10
print(x(5))  # 15

x = lambda a, b: a * b
print(x(5, 4))  # 20

x = lambda a, b, c: a * b * c
print(x(5, 4, 3))  # 60

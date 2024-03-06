a = 10
b = 10.5
name1 = "Pavan"
name2 = 'Pavan2'
x = True

print(a)
print(b)
print(x)
print(name1)
print(name2)

# this statement assign 100 to a, 10.5 to b and Pagana to name1. Multiple values to multiple variables
a, b, name1 = 100, 10.5, "Pagana"
print(a, b, name1)

# a, b, c = 10, 10, 10   same with below
a = b = c = 10
print(a, b, c)

######
x = 1
y = 2
y, x = x, y    # x assign y , y assign x
print(x,y)

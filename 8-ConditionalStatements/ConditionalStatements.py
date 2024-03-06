# Example 1
a = 10
if a > 20:
    print("True condition")
else:
    print("False condition")

# Example 2
if False:
    print("True condition")
else:
    print("False condition")

# Example 3
if 1:
    print("True condition")
else:
    print("False condition")

b = 10
if b % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Example 4
if True:
    print("statement 1")
    print("statement 2")
    print("statement 3")
else:
    print("statement 4")
    print("statement 5")
print("statement 6")    # this is not part for if or else condition

# Example 5
# single statement in single line
print("Welcome") if True else print("Python")
print("Welcome") if 10 > 20 else print("Python")

# Example 6
# multiple statement in single line
{print("Welcome1"),print("welcome2")} if True else {print("Python1"),print("Python2")}

# Example 7
# elif command
a = 10

if a == 30:
    print("Ten")
elif a == 20:
    print("Twenty")
elif a == 30:
    print("Thirty")
else:
    print("Not listed")
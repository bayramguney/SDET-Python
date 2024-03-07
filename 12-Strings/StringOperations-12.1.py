name1 = "John"
name2 = 'John'
print(name2)

name3 = str("Tom")
print(name3)

#  +   *
str1 = "Welcome"
print(str1 + " to python")     # Welcome to python
print(str1 * 3)    # WelcomeWelcomeWelcome

# Slicing string
str2 = "welcome"
print(str2[1:3])     # el
print(str2[:6])     # welcom
print(str2[4:])     # ome

# ord and chr    convert ascii to char versa
print(ord('z'))     # 122
print(chr(122))     # z

# len max min
print(len("hello"))     # 5
print(max("hello"))     # o     # as ascii
print(min("hello"))     # e     # as ascii

# in and not in operators
str3 = "Welcome"
print("come" in str3)          # True
print("come" not in str3)      # False

# String comparison
print("tim" == "tom")   # False
print("free" != "freedom")  # True
print("arrow" > "aron")  # True
print("right" >= "left")  # True
print("teeth" < "tee")  # False
print("yellow" <= "fellow")  # False
print("abc" > " ")  # True

# iterating string with loop
str4 = "python"
for i in str4:
    print(i)   # p y t h o n
for i in str4:
    print(str4)  # python python python python python python

# Testing string
s = "welcome to python"
print(s.isalnum())    # False
print("Tim".isalpha())    # True
print("2012".isdigit())  # True
print("first number".isidentifier())  # False
print(s.islower())   # True
print("TOM".isupper())  # True
print(" ".isspace())  # True

# searching string
s1 = "welcome to python"
print(s1.endswith("thon"))   # true
print(s1.startswith("good"))  # False
print(s.find("come"))   # 3
print(s.find("become"))  # -1
print(s.rfind("o"))   # 15    highest index found
print(s.count("o"))     # 3

# Converting string
s2 = "String in PYTHON"
print(s2.capitalize())   # String in python
print(s2.title())       # String In Python
print(s2.lower())       # string in python
print(s2.upper())     # STRING IN PYTHON
print(s2.swapcase())  # sTRING IN python
print(s2.replace("in", "on"))   # Strong on PYTHON

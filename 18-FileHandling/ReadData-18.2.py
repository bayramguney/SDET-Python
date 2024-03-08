"""
read[number]    return specific number of char from file if omitted real all file
readline()    return next line of the file
readlines()  read all lines as string
"""
file = open('C://sdet//Phyton//mytext.txt',"r")
print(file.read())      # all files
file.close()

file = open('C://sdet//Phyton//mytext.txt',"r")
print(file.read(4))
file.close()     # This

file = open('C://sdet//Phyton//mytext.txt',"r")
print(file.readlines())   # ['This is my first line\n', 'This is my second line\n']
file.close()

file = open('C://sdet//Phyton//mytext.txt',"r")
print(file.readline())  # This is my first line      read first line
file.close()

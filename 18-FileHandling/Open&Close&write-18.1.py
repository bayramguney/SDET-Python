"""
r   read only
w   writing only . if file exist it will clear the file not new file created
a   appending
"""
file = open('C://sdet//Phyton//mytext.txt', 'w')  # open file for writing
file.write('This is my first line\n')
file.write('This is my second line\n')
file.close()


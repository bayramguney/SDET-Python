file = open('C://sdet//Phyton//mytext.txt',"a")
file.write("this is third line\n")
file.close()     # This


# read all data at once
file = open('C://sdet//Phyton//mytext.txt',"r")

for l in file:
    print(l)
file.close()

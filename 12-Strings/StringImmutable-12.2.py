str1 = "Welcome"     # string is immutable can not be modified
str2 = "Welcome"
print(id(str1),id(str2))    # 2687330079040   2687330079040    pointing same location

str2 = str2+" to python"
print(id(str1),id(str2))    # 2761238861200 2761239085360    str2 location changed
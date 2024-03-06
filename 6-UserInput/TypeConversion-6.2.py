num1 = input("Enter first decimal number:")  # 10.5
num2 = input("enter second decimal number:")  # 10.5
print(float(num1) + float(num2))  # 21.0

num1 = input("Enter first decimal number:")  # 10.5
num2 = input("enter second decimal number:")  # 10.5
print(float(num1) + int(num2))  # invalid literal because num2 is float  integer can not hold float

num1 = input("Enter first decimal number:")  # 10.5
num2 = input("enter second integer number:")  # 10
print(float(num1) + float(num2))  # 20.5   float can hold int

print("Program is started")
try:
    print(10 / 0)  # ZeroDivisionError: division by zero
except ZeroDivisionError:
    print("Error occurred")

try:
    print(10 / 2)  # ZeroDivisionError: division by zero
    print("No error")
except ZeroDivisionError:
    print("Error occurred")

try:
    print(10 / 0)  # ZeroDivisionError: division by zero
except TypeError:    # will not catch the error
    print("Error occurred")
except ZeroDivisionError:
    print("Error occurred and handled")



print("Program is completed")

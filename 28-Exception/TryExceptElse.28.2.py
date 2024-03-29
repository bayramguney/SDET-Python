try:
    print(10 / 0)  # ZeroDivisionError: division by zero
except TypeError:    # will not catch the error
    print("Error occurred")
except ZeroDivisionError:
    print("Error occurred and handled")
else:
    print("Inside the else block")  # it will run the condition no execution raised
finally:
    print("Finally block")    # always executed





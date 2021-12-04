def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print("Division by zero!")
except Exception as err:
    print("Caught an exception")
finally:
    print("In finnaly block for cleanup")
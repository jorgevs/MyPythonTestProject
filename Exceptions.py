# Handle exceptions =================================================================
x = [1, 2, 3, 4, 5];
try:
    item = x[10]
except IndexError:
    # this will print only on a IndexError exception
    print("Exception: list index out of range")
except TypeError:
    # this will print only on a TypeError exception
    print("Exception: x isn't a list!")
else:
    # executes if the code in the "try" does NOT
    # raise an exception
    print("You didn't raise an exception!")
finally:
    # this will always print
    print("processing complete")

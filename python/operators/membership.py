# In Python, in and not in are the membership operators that are used to test whether a value or variable is in a sequence.

# in            True if value is found in the sequence
# not in        True if value is not found in the sequence 



x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
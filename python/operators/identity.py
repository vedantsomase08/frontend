# In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 

# is          True if the operands are identical 
# is not      True if the operands are not identical 


a = 10
b = 20
c = a

print(a is not b)
print(a is c)
# This is a comment
# written in
# more than just one line
""""
This is a comment
written in
more than just one line
"""

# 1. Creating variable
x = 5
y = "Hello, World!"
print(x)
print(y)

# 2. Assisgning to multiple variables
x1, y1, z1 = "Orange", "Banana", "Cherry"
print(x1)
print(y1)
print(z1)

# Assigning the same value to multiple variables in one line:
x2 = y2 = z2 = "Orange"
print(x2)
print(y2)
print(z2)

# Output Variables
x3 = "awesome"
print("Python is " + x3)

# You can use the + character to add the variable
x4 = "Python is "
y4 = "awesome"
print(x4 + y4)

# Error
# x5=5
# y5="John"
# print(x5+y5)

# Global Variable
x6 = "awesome"


def myfunc():
    print("Python is " + x6)


myfunc()

# Create a variable inside a function, with the same name as the global variable
x7 = "awesome"


def myfunc1():
    x7 = "fantastic"
    print("Python is " + x7)


myfunc1()
print("Python is " + x7)


# If you use the global keyword , the variable belongs to the global scope:
def myfunc2():
    global x8
    x8 = "fantastic"
    print("\nPython is " + x8)


myfunc2()
print("Python is " + x8)

# To Change the value of a global variable inside a function, refer to the variable
# by using the global keyword
x9 = "awesome"


def myfunc3():
    global x9
    x9 = "fantastic"
    print("\nPython is " + x9)


myfunc3()
print("Python is " + x9)

"""https://arcade-book.readthedocs.io/en/latest/chapters/08_functions/functions.html"""


# Example 1
def a():
    print("A")


def b():
    print("B")


def c():
    print("C")

print("Example 1")
a()


# Example 2
def a():
    b()
    print("A")


def b():
    c()
    print("B")


def c():
    print("C")

print("Example 2")
a()


# Example 3
def a():
    print("A")
    b()


def b():
    print("B")
    c()


def c():
    print("C")

print("example 3")
a()

# Example 4
def a():
    print("A start")
    b()
    print("A end")


def b():
    print("B start")
    c()
    print("B end")


def c():
    print("C start and end")

print("example 4")
a()

# Example 5
def a(x):
    print("A start, x =", x)
    b(x + 1)
    print("A end, x =", x)


def b(x):
    print("B start, x =", x)
    c(x + 1)
    print("B end, x =", x)


def c(x):
    print("C start and end, x =", x)

print("example 5")
a(5)

# Example 6
def a(x):
    x = x + 1


x = 3
a(x)

print("example 6")
print(x)

# Example 7
def a(x):
    x = x + 1
    return x


x = 3
a(x)

print("example 7")
print(x)

# Example 8
def a(x):
    x = x + 1
    return x


x = 3
x = a(x)

print("example 8")
print(x)

# Example 9
def a(x, y):
    x = x + 1
    y = y + 1
    print(x, y)


x = 10
y = 20
print("example 9")
a(y, x)

# Example 12
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y


x = 10
y = 20
x2, y2 = a(x, y) # Most computer languages don't support this

print("example 12")
print(x2)
print(y2)

# Example 14
def a(my_list):
    print("function a, list =  ", my_list)
    my_list = [10, 20, 30]
    print("function a, list =  ", my_list)


my_list = [5, 2, 4]

print("example 14")
print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)


# Example 15
# New concept!
# Covered in more detail in a later chapter
def a(my_list):
    print("function a, list =  ", my_list)
    my_list[0] = 1000
    print("function a, list =  ", my_list)


my_list = [5, 2, 4]

print("example 15")
print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)
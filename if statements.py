"""https://arcade-book.readthedocs.io/en/latest/chapters/10_if_statements/if_statements.html"""

a = 4
b = 5
c = 9

if a <= b:
    print("a is less than or equal to b")

if a >= b:
    print("a is greater than or equal to b")

print("Done")

# Equal
if a == b:
    print("a is equal to b")

# Not equal
if a != b:
    print("a and b are not equal")

print("Done")

# And

# both conditions must be true
if a < b and a < c:
    print("a is less than b and c")


# Non-exclusive or
# only one condition must be true
if a < b or a < c:
    print("a is less than either b or c (or both)")

print("Done")


# Boolean data type. This is legal!
a = True
if a:
    print("a is true")

print("Done.")


# How to use the not function
# this fails because the NOT flips the boolean
if not a:
    print("a is false")

print("NOT Done")

a = True
b = False

# this fails because b is not TRUE
if a and b:
    print("a and b are both true")

print("AND Done")

#assigning values to Bool data types
a = 3
b = 4

# This next line is strange-looking, but legal.
# c will be true or false, depending if
# a and b are equal.
c = a == b

# Prints value of c, in this case False
print(c)

print("done...")

# input function asks for user input.  Anything saves is a STR not a INT, e.g. you cannot evaluate it
temp = input("input function:   What is the temp in F? ")
print("You said the temp was " + temp + ".")
print("Done......")

# to convert the input into an integer use int()
# note: it will not work if you input a string
temp = input("INT FUNCTION:  What is the temp in F? ")
# magic below
temp = int(temp)

#Do comparison
if temp > 90:
    print("It is hot.")
else:
    print("It is NOT not.")
print("DONE.......")


# Else If chain

temp = int(input("ELIF: What is the temperature? "))

if temp > 90:
    print("The temp is greater than 90.")
elif temp < 30:
    print("The temp is less than 30.")
else:
    print("The temp is between 90 and 30.")
print("Done ELIF.")

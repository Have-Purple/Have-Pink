print("Pink")
print("Octopus")

print("Pink", end=" ")
print("Octopus")

i = 0
print(i, end=" ")
i = 1
print(i, end=" ")

print("DONE")

for i in range(10):
    print("*", end=" ")
print()
for j in range(5):
    print("*", end=" ")
print()
for k in range(20):
    print("*", end=" ")
print()
print("DONE")

## print 10x10 matrix
count = 1
while count < 11:
    for i in range(10):
        print("*", end=" ")
    print()
    count += 1
print("DONE")

# print 10x10 matrix
for row in range(10):
    for column in range(10):
        print("*", end=" ")
    print()
print("DONE")


#print 5x10 matrix
for row in range(10):
    for column in range(5):
        print("*", end=" ")
    print()
print("DONE.")

#print 20x5 matrix
for row in range(5):
    for column in range(20):
        print("*", end=" ")
    print()
print("DONE.")

#print 0123456789 X 10 matrix
for r in range(10):
    for i in range(10):
        print(i, end=" ")
    print()
print("DONE")

#print 0,1,2,3 X 10 matrix
for r in range(10):
    for i in range(10):
        print(r, end=" ")
    print()
print("DONE")

#print 0,0 1, 0 1 2, 0 1 2 3 X 10 matrix
for r in range(10):
    for i in range(r + 1):
        print(i, end=" ")
    print()
print("DONE")

#print saw tooth matrix
print("START Problem 9")

for row in range(10):
    for column in range(row):
        print(" ", end=" ")
    for column in range(10 - row):
            print(column + 1, end=" ")
    print()
print("DONE Problem 9")

## problem 10
print("START Problem 10")

for i in range(1, 10):
    for j in range(1, 10):
        # Extra space?
        if i * j < 10:
            print(" ", end="")

        print(i * j, end=" ")
    print()

print("DONE Problem 10")



## problem 11
print("START Problem 11")

for row in range(1, 11):
    for i in range(10 - row):        # leading triangle of *
        print("*", end=" ")
    for i in range(1, row, 1):       # first triangle of numbers
        print(i, end=" ")
    for i in range(row, 0, -1):      # second triangle of numbers
        print(i, end=" ")
    for i in range(10 - row):        # trailing triangle of *
        print("*", end=" ")
    print()

print("DONE Problem 11")


## problem 12
print("START Problem 12")

for row in range(1, 9, 1):
    for i in range(9 - row):        # leading triangle of 'spaces'
        print(" ", end=" ")
    for i in range(1, row, 1):       # first triangle of numbers
        print(i, end=" ")
    for i in range(row, 0, -1):      # second triangle of numbers
        print(i, end=" ")
    print()
for row in range(9):
    for column in range(row):
        print(" ", end=" ")
    for column in range(9 - row):
            print(column + 1, end=" ")
    print()

print()

print("DONE Problem 12")


## problem 13
print("START Problem 13")

for row in range(1, 9, 1):
    for i in range(9 - row):        # leading triangle of 'spaces'
        print(" ", end=" ")
    for i in range(1, row, 1):       # first triangle of numbers
        print(i, end=" ")
    for i in range(row, 0, -1):      # second triangle of numbers
        print(i, end=" ")
    print()
for row in range(9):
    for column in range(row):             # leading riangle of spaces
        print(" ", end=" ")
    for column in range(9 - row):          # third triangle of numbers
        print(column + 1, end=" ")
    for column in range(8 - row, 0, -1):    # fourth triangle of numbers
        print(column, end=" ")
    print()

print("DONE Problem 13")

# What does this print? Why?
for i in range(3):
    print("a")
    for j in range(3):
        print("b")

print("Done")

# What is the value of sum?
total = 0
for i in range(1, 101):
    total = total + i
print(total)

# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)

# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)

for i in range(5):
    print("I will not chew gum in class.")

for i in range(5):
    print("Please, ")
    print("Can I go to the mall?")

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

# Two ways to print the even numbers 2 to 10
for i in range(2,12,2):
    print(i)

for i in range(5):
    print((i + 1) * 2)

# count down, use negative step
for i in range(10, 0, -1):
    print(i)

# print numbers from a list
for i in [2,6,4,2,4,6,7,4]:
    print(i)

print("Done....")

# What does this print? Why?
for i in range(3):
    print("a")
for j in range(3):
    print("b")
print("1st")

# What does this print? Why?
for i in range(3):
    print("a")
    for j in range(3):
        print("b")
print("2nd")

def running_total(iteration):
    total = 0
    for i in range(iteration):
        new_number = int(input("Enter a number: "))
        total = total + new_number
    print("The total is:", total)
    print("RUNNING TOTAL DONE.")

#running_total(2)

def summation(iteration):
    total = 0
    # must use iteration + 1 otherwise it will only add 1+2+3...98+99
    for i in range(iteration + 1):
        total = total + i
    print("The summation function total is: ", total)

summation(100)

# What is the value of sum?
total = 0
for i in range(1, 101):
    total = total + i
print("The summation #2 total is: ", total)

def zero_count(iteration):
    # Enter a list [size iteration] of numbers and count the number of "0" entered and return that count
    total = 0
    for i in range(iteration):
        new_number = int(input( "Enter a number: "))
        if new_number == 0:
            total = total + 1
    print("You entered a total of", total, "zeros.")

#zero_count(5)

# What is the value of a?
a = 0
for i in range(10):
    a = a + 1
print(a)

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
    print("outer:    ", a)
    for j in range(10):
        a = a + 1
        print("INNER: ", a)
print("total a: ", a)


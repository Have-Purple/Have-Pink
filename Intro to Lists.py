# https://arcade-book.readthedocs.io/en/latest/chapters/13_lists/lists.html

# for item_variable in list_name:

my_list = [101, 20, 10, 50, 60]
for item in my_list:
    print(item)

my_list = ["Spoon", "Fork", "Knife"]
for item in my_list:
    print(item)

my_list = [[2, 3], [4, 3], [6, 7]]
for item in my_list:
    print(item)

# index variable for direct access
# use len() to discover number of items in list

my_list = [101, 20, 10, 43, 54, 77, 37, 111]
for index in range(len(my_list)):
    print(index, my_list[index])
    # print(my_list[index])

for index, value in enumerate(my_list):
    print(index, value)

print("13.4 DONE")

# 13.5 adding to a list

my_list = [2, 4, 5, 6, 7]
print(my_list)
my_list.append(9)
print(my_list)

print("13.5 Done")

my_list = []  # empty list
'''for i in range(5):
    user_input = input( "Enter and integer: ")
    user_input = int(user_input)  # make sure it's and integer
    my_list.append(user_input)
    print(my_list)

print("DONE")'''

# Create an array with 100 zeros.
my_list = [0] * 100
print(my_list)

print("list with 100 zeros, DONE")

# 13.6 summing a list

# Copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

list_total = 0
for i in range(len(my_list)):
    list_total += my_list[i]

print("Summing list V1", list_total)

# Copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Initial sum should be zero
list_total = 0

for item in my_list:
    list_total += item

print("Summing list V2", list_total)

# doubling all numbers in a list

my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

for i in range(len(my_list)):
    my_list[i] *= 2

print("Doubling all numbers in a list", my_list)

# accessing a string

x = "This is a sample string"
# x = "0123456789"

print("x=", x)

# Accessing a single character
print("x[0]=", x[0])
print("x[1]=", x[1])

# Accessing from the right side
print("x[-1]=", x[-1])

# Access 0-5
print("x[:6]=", x[:6])
# Access 6
print("x[6:]=", x[6:])
# Access 6-8
print("x[6:9]=", x[6:9])

a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 4) + (b * 2))

print("Done")

a = "Hi There"
print(len(a))

b = [3, 4, 5, 6, 76, 4, 3, 3]
print(len(b))

for character in "This is a test.":
    print(character)

''''#excercise

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# abs() ensures postive
# int() ensures integer
n = abs(int(input("Enter a month number: ")))

#https://www.djm.org.uk/posts/python-multiple-line-conditions-and-all-builtin/
rules = [n>0, n<=12]

if all(rules):
    print(months[((n-1)*3):(n*3)])
else:
    print("input outside the range of 0-12")
print("Done with excercise")'''

# this below is ugly
'''
if n == 1:
    print(months[0:3])
elif n == 2:
    print(months[3:6])
elif n == 3:
    print(months[6:9])
elif n == 4:
    print(months[9:12])
elif n == 5:
    print(months[12:15])
'''

plain_text = "This is a test."

for c in plain_text:
    print(c, end=" ")

# ord() converts string to unicode utf-8 value  the opposite is chr(): chr(97) = 'a'
for c in plain_text:
    print(ord(c), end=" ")
print("End")
print(" ")

# convert string to utf-8, add 1 to utf-8 value, print new string
text = "This is only a test. A test of the Emergency Broadcast System."
print(text)


# encrypted_text = ""

def encrypt(plain_text):
    encrypted_text = ""
    for c in plain_text:
        x = ord(c)
        x += 1
        c2 = chr(x)
        encrypted_text += c2
    return (encrypted_text)


# plain_text_2 = ""


def decrypt(encrypted_text):
    plain_text_2 = ""
    for d in encrypted_text:
        y = ord(d)
        y -= 1
        d2 = chr(y)
        plain_text_2 += d2
    return (plain_text_2)


a = encrypt(text)
print(a)

b = decrypt(a)
print(b)
print(" END ")

# Create an empty associative array
# (Note the curly braces.)
x = {}

# Add some stuff to it
x["fred"] = 2
x["scooby"] = 8
x["wilma"] = 1

# Fetch and print an item
print(x["fred"])

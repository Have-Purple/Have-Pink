"""https://arcade-book.readthedocs.io/en/latest/chapters/11_loops_and_random_numbers/loops_and_random_numbers.html"""

# print hi 10 times
for i in range(10):
    print("#", i, "Hi")

# print hello 5 times and there once
for i in range(5):
    print("#", i, "Hello")
print("There")

# print hellow there 5 times
for i in range(5):
    print("#", i,"Hello")
    print("#", i,"There")

#etc etc etc

for i in range(10):
    print(i)

i = 0
while i < 10:
    print(i)
    i = i + 1


# while i is less than 2**32 multiply I times 2
i = 1
while i <= 2 ** 32:
    print(i)
    i *= 2

# while value less than .99999 value = value + increment
#increment = increment * .5
value = 0
increment = 0.5
while value < 0.9:
    value += increment
    increment *= 0.5
    print(value)

i = 10
while i != 0:
    print(i)
    i -= 1

#break statement
while True: # Loop forever
    quit = input("Do you want to quit? ")
    if quit == "y":
        break

    attack = input("Does your elf attack the dragon? ")
    if attack == "y":
        print("Bad choice, you died.")
        break
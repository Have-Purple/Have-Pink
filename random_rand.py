import random

# prints random number between 0 and 49
my_number = random.randrange(50)
# alternative for random between 1,50
my_number = random.randrange(1,51)

# random between 0 and 100 with a step of 10
my_number = random.randrange(0,100,10)

#random item out of a list
my_list = ["rock", "paper", "scissors"]
my_item = random.choice(my_list)
print(my_item)

print(my_number)


#random floating point number between 0 and 1
my_number = random.random()
print(my_number)

#random float between 1 and 10
my_number = random.random() * 10 + 1
print(my_number)

#random float between 10 and 15
my_number = random.random() * 5 + 10
print(my_number)

# random chance of something happening
for i in range(10):
    if random.randrange(5) == 0:
        print("DRAGON!!")
    else:
        print("No dragon.")




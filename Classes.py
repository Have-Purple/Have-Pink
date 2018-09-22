'''https://arcade-book.readthedocs.io/en/latest/chapters/14_classes/classes.html'''
import arcade


def give_money2(person):
    person.money += 100


class Person():
    def __init__(self):
        self.name = ""
        self.money = 0


class Ball():
    def __init__(self):
        # Ball position
        self.x = 0
        self.y = 0

        # Ball vector
        self.change_x = 0
        self.change_y = 0

        # Ball size and color
        self.size = 0
        self.color = [255, 255, 255]

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)


class Address():
    def __init__(self):
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""


class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):
        print(self.name, "says WOOF!!!")
        print(self.name, "weighs", self.weight, "pounds")
        print(self.name, "is", self.age, "years old")


# Print an address to the screen
def print_address(address):
    print(address.name)
    # If there is a line1 in the address, print it
    if len(address.line1) > 0:
        print(address.line1)
    # If there is a line2 in the address, print it
    if len(address.line2) > 0:
        print(address.line2)
    print(address.city + ", " + address.state + " " + address.zip)


def main():
    # Create an address
    home_address = Address()

    # Set the fields in the address
    home_address.name = "John Smith"
    home_address.line1 = "701 N. C Street"
    home_address.line2 = "Carver Science Building"
    home_address.city = "Indianola"
    home_address.state = "IA"
    home_address.zip = "50125"

    # Create another address
    vacation_home_address = Address()

    # Set the fields in the address
    vacation_home_address.name = "John Smith"
    vacation_home_address.line1 = "1122 Main Street"
    vacation_home_address.line2 = ""
    vacation_home_address.city = "Panama City Beach"
    vacation_home_address.state = "FL"
    vacation_home_address.zip = "32407"

    print("The client's main home is in " + home_address.city)
    print("His vacation home is in " + vacation_home_address.city)

    print_address(home_address)
    print()
    print_address(vacation_home_address)

    # Dog Stuff
    my_dog = Dog()
    my_dog.name = "Chaos"
    my_dog.weight = 110
    my_dog.age = 1

    print()
    my_dog.bark()

    # Ball stuff
    the_ball = Ball()
    the_ball.x = 100
    the_ball.y = 100
    the_ball.change_x = 2
    the_ball.change_y = 1
    the_ball.color = [255, 0, 0]

    the_ball.move()
    the_ball.draw()

    # Person stuff
    bob = Person()
    bob.name = "Bob"
    bob.money = 100

    # nancy = Person()
    # or alternative below
    nancy = bob
    nancy.name = "Nancy"

    print()
    print(bob.name, "has", bob.money, "dollars")
    print(nancy.name, "has", nancy.money, "dollars")

    print(bob.money)
    give_money2(bob)
    print(bob.money)


main()

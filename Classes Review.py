# https://arcade-book.readthedocs.io/en/latest/chapters/14_classes/classes.html

class Star():
    def __init__(self):
        print("A star is born!")


class Cat():
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = 0

    def meow(self):
        print(self.name, "says meow!!")


class Monster():
    def __init__(self, new_name, new_health):
        self.name = new_name
        self.health = new_health

    def decrease_health(self, amount):
        # create two new variables to do tests against
        # health is initial health
        health = self.health
        # damage is positive integer ensuring that "amount" is good to go
        damage = abs(int(amount))

        self.health -= damage
        if self.health <= 0:
            print(self.name, "has died!")
        else:
            print(self.name, "has", health - damage, "health left.")


def main():
    whiskers = Cat()

    whiskers.name = "whiskers"
    whiskers.color = "yellow"
    whiskers.weight = 12

    whiskers.meow()

    # Monster stuff

    puff = Monster("Puff", 50)

    puff.decrease_health(88)

    # Star stuff
    dipper = Star()


main()

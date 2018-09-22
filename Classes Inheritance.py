'''https://arcade-book.readthedocs.io/en/latest/chapters/14_classes/classes.html'''


class Boat():
    def __init__(self):
        self.tonnage = 0
        self.name = ""
        self.is_docked = True

    def dock(self):
        if self.is_docked:
            print("You are already docked.")
        else:
            self.is_docked = True
            print("Docking...")

    def undock(self):
        if not self.is_docked:
            print("You are not docked.")
        else:
            self.is_docked = False
            print("Undocking...")


class Submarine(Boat):
    def submerge(self):
        print("Submerge!!!")


class Person():
    def __init__(self):
        self.name = ""

    def report(self):
        print("Report for", self.name)


class Employee(Person):
    def __init__(self):
        # call the parent class constructor first
        super().__init__()

        # set up variables
        self.job_title = ""

    def report(self):
        # Override parent report method and do our own thing
        print("Employee report for", self.name)


class Customer(Person):
    def __init__(self):
        super().__init__()
        self.email = ""

    def report(self):
        # run the parent report
        super().report()

        # now add our own stuff
        print("Customer email", self.email)


def main():
    b = Boat()

    b.dock()
    b.undock()
    b.undock()
    b.dock()
    b.dock()

    # Submarine stuff
    s = Submarine()
    s.submerge()
    s.dock()
    s.dock()
    s.undock()
    s.undock()

    # Person stuff
    john_smith = Person()
    john_smith.name = "John Smith"

    jane_employee = Employee()
    jane_employee.name = "Jane Employee"
    jane_employee.job_title = "Web Developer"

    bob_customer = Customer()
    bob_customer.name = "Bob Customer"
    bob_customer.email = "bob@internet.com"

    john_smith.report()
    jane_employee.report()
    bob_customer.report()


main()

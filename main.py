class Ticket:
    def __init__(self, name="", age=0, student="", film_num=0):
        self.name = name
        self.age = age
        self.student = student
        self.film_num = film_num
        self.price = 0
        self.ticket = True
        self.film_name = ""
        self.film_rating = ""

    def check_price(self):
        """ Set price of movie ticket based on age; student and seniority discount. """
        if 10 <= self.age < 18 and (self.student == "Y" or self.student == "y"):
            self.price = 7 * 85 / 100  # 15% discount
        elif 18 <= self.age <= 25 and (self.student == "Y" or self.student == "y"):
            self.price = 10 * 85 / 100  # 15% discount
        elif self.age > 25 and (self.student == "Y" or self.student == "y"):
            self.price = 10 * 90 / 100  # 10% discount
        elif 18 <= self.age <= 64:
            self.price = 10
        elif self.age < 18:
            self.price = 7
        elif self.age > 64:
            self.price = 10 * 93 / 100  # 7% discount

    def check_film(self):
        """ Determine movie number, name and rating accordingly. """
        if self.film_num == 1:
            self.film_name = "Ant-man"
            self.film_rating = "P"
        elif self.film_num == 2:
            self.film_name = "Minions"
            self.film_rating = "P"
        elif self.film_num == 3:
            self.film_name = "Jurassic World"
            self.film_rating = "M"
        elif self.film_num == 4:
            self.film_name = "Inside Out"
            self.film_rating = "G"

    def check_age(self):
        """ Determine eligibility of movie entry based on age and movie rating. """
        if self.film_rating == "M" and self.age <= 16:
            self.ticket = False
        elif self.film_rating == "P" and self.age <= 12:
            self.ticket = False

class studentException(Exception):
    """ Student verification input exception. """
    pass

def main():
    """ Main class to run program. """
    print()
    print("Welcome to the Cinema Ticket Purchasing System")
    name = input("Please enter your name: ")
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid age value. Please try again.")
            continue
    while True:
        try:
            student = input("Are you a student? (Y/N) ")
            if student == "Y" or student == "y" or student == "N" or student == "n":
                break
            else:
                raise studentException
        except studentException:
            print("Invalid student verification. Please try again.")
            continue

    print("Which film would you like to watch?")
    print("1 Ant-man rating: (P)")
    print("2 Minions rating: (P)")
    print("3 Jurassic World rating: (M)")
    print("4 Inside Out rating: (G)")

    while True:
        try:
            film_num = int(input("Enter film number: "))
            if 0 < film_num < 5:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid film number. Please try again.")
            continue

    buyer = Ticket(name, age, student, film_num)
    buyer.check_price()
    buyer.check_film()
    buyer.check_age()

    if buyer.ticket is True:
        print()
        print("Your ticket is ready to be collected")
        print("-------------------------------------------")
        print("FILM TICKET for: {} : {}".format(buyer.film_name, buyer.film_rating))
        print("CUSTOMER DETAILS: {} age: {} Student? {}".format(buyer.name, buyer.age, buyer.student))
        print("TOTAL COST: {}".format(buyer.price))
        print("-------------------------------------------")
        print()
    else:
        print()
        print("Sorry, cannot issue ticket for age restricted film")


while True:
    main()
    print("Do you want another ticket? (Y/N)")
    restart = input()
    if restart == "N" or restart == "n":
        break
    else:
        continue

import random


def yes_no(question):
    valid = False
    while not valid:

        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer yes / no")


show_instructions = yes_no("Have you played this game before?")

print("you chose {}".format(show_instructions))
print()
having_fun = yes_no("Are you having fun?")
print("you said {} to having fun".format(having_fun))


def statement_generator(statement, decoration):
    sides = decoration * 1

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()

def num_check(question, low, high) -> object:
    error = "Please enter an whole number between 1 and 10\n"
    valid = False
    while not valid:
        try:
            response = int(input(question))

            if low < response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


how_much = num_check("How much would you like to play with", 0, 10)

print("You will be spending ${}".format(how_much))
error = "Please enter an whole number between 1 and 10\n"
valid = False
while not valid:
    try:
        response = int(input("How much would you like to play with "))

        if 0 < response <= 10:
            print("you have asked to play with ${}".format(response))

        else:
            print(error)

    except ValueError:
        print(error)

balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again != "xxx":
    rounds_played += 1

    print()
    print(rounds_played)
    print("*** Round #{} ***".format(rounds_played))

    token = ["unicorn", "horse", "horse", "horse",
             "zebra", "zebra", "zebra",
             "donkey" "donkey" "donkey"]
    STARTING_BALANCE = 10

    balance = STARTING_BALANCE

    for item in range(0, 10):
        chosen = random.choice(token)

        if chosen == "unicorn":
            balance += 4
        elif chosen == "donkey":
            balance -= 1
        else:
            balance -= 0.5

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have ruined out of money")
    else:
        play_again = input("Press enter to play again "
                           "or xxx to quit")

    print()
    print("Final balance", balance)

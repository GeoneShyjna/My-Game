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


# Integer checking function
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Please enter an number between {} " \
                "and {}\n".format(low, high)
        try:
            response = int(input(question.format(low, high)))
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


print("**** Welcome to the Lucky Unicorn Game ****")
print()
print("To play, enter an amount of money between $1 and $10 (whole dollars only).")
print()
print("Each round costs $1")
print()
print("Payouts:")
print("\tUnicorn: $5.00")
print("\tHorse or Zebra: $0.50")
print("\tDonkey: $0.00")
print()


UNICORN_PAYOUT = 5
HORSE_ZEBRA_PAYOUT = 0.5
GAME_FEE = 1
MAX_AMOUNT = 10

user_balance = intcheck("How much money would you like to play with? ", GAME_FEE, MAX_AMOUNT)

keep_playing = ""
while not keep_playing:

    tokens = ["horse", "horse", "horse",
              "zebra", "zebra", "zebra",
              "donkey", "donkey", "donkey",
              "unicorn"]

    token = random.choice(tokens)
    print("--------------------------------")
    print("You got a {}".format(token))
    print("--------------------------------")

    # Adjust user_balance correctly for given token
    if token == "unicorn":
        user_balance += UNICORN_PAYOUT - GAME_FEE  # Wins $5 less $1 playing fee
        print("Congratulations. You won ${:.2f}".format(UNICORN_PAYOUT))
    elif token == "horse" or token == "zebra":
        user_balance += HORSE_ZEBRA_PAYOUT - GAME_FEE  # Wins $0.50c less $1 playing fee
        print("Congratulations. You won ${:.2f}".format(HORSE_ZEBRA_PAYOUT))
    else:
        user_balance -= GAME_FEE
        print("Sorry, you did not win anything this round")

    if user_balance >= GAME_FEE:
        print("You have ${:.2f} left to play with".format(user_balance))
        keep_playing = input("Press <enter> to play another round or 'xxx' to quit: ")
    else:
        print("You ran out of money")
        keep_playing = "xxx"


print("\nYou are leaving with a balance of ${:.2f}\nThanks for playing. Goodbye".format(user_balance))

import random

token = ["unicorn", "horse", "horse", "horse",
         "zebra", "zebra", "zebra",
         "donkey" "donkey" "donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE

for item in range(0, 500):
    chosen = random.choice(token)

    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

print()

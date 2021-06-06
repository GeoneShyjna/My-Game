import random
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again =="":
    rounds_played += 1

    print()
    print(rounds_played)
    print("*** Round #{} ***".format(rounds_played))

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

  if balance < 1:
      play_again = "xxx"
      print("Sorry you have ruined out of money")
  else:
      play_again = input("Press enter to play again "
                         "or xxx to quit")

print()
print("Final balance", balance)

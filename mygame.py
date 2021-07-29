
name = input("What is your name? ")
# Here the user is asked to enter the name first
print("Hi", name, "you are stuck in a maze, there is multiple doors in the maze but you can only choose one door")

Level_1 = ""
while Level_1.lower() != "xxx":

    Level_1 = input("This is the level 1 \n"
                    "**DOOR 1**\n**DOOR 2**\n**DOOR 3**\n")

    if Level_1 == "DOOR1" or Level_1 == "1":
        print("You passed this level on to the next level!")

    elif Level_1 == "DOOR2 " or Level_1 == "2":
        print("\n***YOU DIED***")
        quit()

    elif Level_1 == "DOOR3 " or Level_1 == "3":
        print("\n***YOU DIED***")
        quit()

    else:
        print("Please answer the question"
              "\n**ANSWER HAVE TO BE IN CAPITAL AND NO SPACE OR JUST THE NUMBER**")

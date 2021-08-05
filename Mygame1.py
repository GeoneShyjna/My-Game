l1 = 2
while l1 == 2:
    Level_1 = input("Level 1\n"
                    "Choose a door\n"
                    "**DOOR 1**\t**DOOR 2**\t**DOOR 3**\n")

    if Level_1 == "DOOR1" or Level_1 == "1":
        print("You passed this level on to the next level!\n")
        l1 = 1
    elif Level_1 == "DOOR2 " or Level_1 == "2":
        print("\n***YOU DIED***")
        quit()

    elif Level_1 == "DOOR3 " or Level_1 == "3":
        print("\n***YOU DIED***")
        quit()

    else:
        print("Please answer the question {}!\n"
              "\n**ANSWER HAVE TO BE IN CAPITALS AND NO SPACE \nOR JUST THE NUMBER**")

l2 = 2
while l2 == 2:
    Level_2 = input("level 2 \n"
                    "Choose a door\n"
                    "**DOOR 1**\t**DOOR 2**\t**DOOR 3**\n")
    if Level_2 == "DOOR3" or Level_2 == "3":
        print("You passes this level on to the next level!")
        l2 = 1
    elif Level_2 == "DOOR2 " or Level_2 == "2":
        print("\n***YOU DIED***")
        quit()

    elif Level_2 == "DOOR1 " or Level_2 == "1":
        print("\n***YOU DIED***")
        quit()

    else:
        print("Please answer the question {}!"
              "\n**ANSWER HAVE TO BE IN CAPITAL AND NO SPACE \nOR JUST THE NUMBER**")

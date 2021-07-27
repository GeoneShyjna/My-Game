Level_1 = ""
while Level_1.lower() != "xxx":

    Level_1 = input("This is the level 1 \n"
                    "**Door 1**\n**Door 2**\n**Door 3**\n").lower()

    if Level_1 == "Door1" or Level_1 == "1":
        print("You passed this level on to the next level!")

    elif Level_1 == "Door2" or Level_1 == "2":
        print("\n***YOU DIED***")
        quit()

    elif Level_1 == "Door3" or Level_1 == "3":
        print("\n***YOU DIED***")
        quit()

    else:
        print("Please answer the question"
              "\n**ANSWER LIKE Door4 or 4")

Level_2 = ""
while Level_2.lower() != "xxx":
    Level_2 = input("This is the level 1 \n"
                    "**Door 1**\n**Door 2**\n**Door 3**").lower()

    if Level_2 == "Door1" or Level_2 == "1":
        print("You passed this level on to the next level!")

    elif Level_2 == "Door2" or Level_2 == "2":
        print("\n***YOU DIED***")
        quit()

    elif Level_2 == "Door3" or Level_2 == "3":
        print("\n***YOU DIED***")
        quit()

    else:
        print("Please answer the question"
              "\n**ANSWER LIKE Door4 or 4")

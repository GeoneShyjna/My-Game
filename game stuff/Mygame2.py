Level_2 = ""
while Level_2.lower() != "xxx":

    Level_2 = input("This is the level 2 \n"
                    "**DOOR 1**\n**DOOR 2**\n**DOOR 3**\n")

    if Level_2 == "DOOR1" or Level_2 == "1":
        print("\n***YOU DIED***")
        quit()

    elif Level_2 == "DOOR2 " or Level_2 == "2":
        print("\n***YOU DIED***")
        quit()

    elif Level_2 == "DOOR3 " or Level_2 == "3":
        print("You passed this level on to the next level!")


    else:
        print("Please answer the question"
              "\n**ANSWER HAVE TO BE IN CAPITAL AND NO SPACE** OR JUST THE NUMBER")

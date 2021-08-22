import os


def dead():
    print("You Died\n"
          "**Adios Muchachos**\n"
          "GUESS YOU WILL JOIN THOSE DEAD BODY'S. WAIT HOLD ON!\n")


def wrong():
    print("Please answer the question {}!\n"
          "\n**ANSWER HAVE TO BE IN CAPITALS AND NO SPACE "
          "\nOR JUST THE NUMBER**\n".format(name))


name = input("What is your name?\n")

print()
print("HI", name, "I'M YOUR VIRTUAL BOT, YOU CAN CALL ME A BOT, IN A NICE WAY (¬_¬ ).\n"
                  "I WILL HELP YOU WITH YOUR JOURNEY IN THE MAZE.\n"
                  "INSTRUCTION WILL BE SEEN BELOW THIS.\n")
print()
print("So", name, "you are stuck in a maze,\n"
                  "there are multiple doors in the maze\n"
                  "but you can only choose one door\n"
                  "**ANSWERS HAVE TO BE IN CAPITALS AND NO SPACE\n"
                  "OR JUST THE NUMBER**\n")
l1 = 2
while l1 == 2:
    Level_1 = input("Level 1\n"
                    "Choose a Door to survive\n"
                    "*Behind Door 1 there is a lion who is hungry since 3 years*\n"
                    "*Behind Door 2 there is a raging fire*\n"
                    "*Behind Door 3 there is psycho waiting to kill you*\n"
                    "So,{} choose a door\n".format(name))

    if Level_1 == "DOOR1" or Level_1 == "1":
        print("**YOU ARE LUCKY THE LION HASN'T EATEN SINCE 3 YEARS**\n"
              "WAIT WHY THERE IS A LION HERE? WHO MADE THIS MAZE! OH YEAH, RIGHT IT WAS ME\n"
              "You passed this level on to the next level!\n")
        l1 = 1
    elif Level_1 == "DOOR2 " or Level_1 == "2":
        print("DO YOU UNDERSTAND ENGLISH (╬▔皿▔)╯, YOU WANT ME TO SPEAK IN SPANISH\n"
              "FUEGO FURIOSO\n")
        dead()
        quit()

    elif Level_1 == "DOOR3" or Level_1 == "3":
        print("WHAT PART OF PSYCHO YOU DON'T UNDERSTAND ￣へ￣\n")
        dead()
        quit()

    else:
        wrong()

l2 = 2
while l2 == 2:
    Level_2 = input("Level 2\n"
                    "Choose a door to survive\n"
                    "*Behind Door 1 there is a laughing lion*\n"
                    "*Behind Door 2 there is sky high mountain which is impossible to climb*\n"
                    "*Behind Door 3 there is a group of whale sharks*\n"
                    "TRUST ME YOU ARE DONE {}, PICK A DOOR.\n".format(name))

    if Level_2 == "DOOR3" or Level_2 == "3":
        print("**YOU SURVIVED AGAIN HOW! WELL YOU SEE THAT\n"
              "WHALE SHARKS ARE NOT A THREAT TO PEOPLE.\n"
              "AT LEAST YOU SAW SOME WHALE SHARKS ;-;**\n"
              "You passes this level on to the next level!\n")
        l2 = 1

    elif Level_2 == "DOOR2 " or Level_2 == "2":
        print("I'M DISAPPOINTED ಥ_ಥ. I EVEN SAID IMPOSSIBLE TO CLIMB Σ(っ °Д °;)っ.\n"
              "LET ME TALK TO YOUR ENGLISH TEACHER (* ￣︿￣)\n")
        dead()
        quit()

    elif Level_2 == "DOOR1 " or Level_2 == "1":
        print("LIONS ARE LIONS. OH MY GOD (╯▔皿▔)╯\n")
        dead()
        quit()

    else:
        wrong()

print("WELL", name, "I THINK YOU HAD A NICE SWIM.\n"
                    "THIS IS NOT THE END", name, "THERE IS MORE, HAHAHAHA (EVIL LAUGH) DID IT WORK,ARE YOU SCARED NOW\n"
                                                 "HAHA, OK FINE I WILL STOP\n"
                                                 "NOW WE ARE MOVING INTO PUZZLE'S")

print()
l1 = 2
while l1 == 2:
    P_1 = input("Level 3\n"
                "When I was 8 years old my brother was half of my age.\n"
                "Now I am 24..So how old is my brother now?\n")

    if P_1 == "TWENTY" or P_1 == "20":
        print("***THE CODE IS 96***\n"
              "You passed this level on to the next level!\n")
        l1 = 1

    else:
        print("BRUH DO YOUR MATH RIGHT. LET ME TALK TO YOUR MATH TEACHER\n")
        wrong()

l1 = 2
while l1 == 2:
    P_2 = input("Level 4\n"
                "Peter was born in March but his birthday was on April\n"
                "So which city was peter born in\n")

    if P_2 == "MARCH".lower():
        print("***THE CODE IS 78***\n"
              "I THINK THERE IS CITY CALLED MARCH NOW\n"
              "TOTALLY I DIDN'T MADE THAT UP\n"
              "You passed this level on to the next level!\n")
        l1 = 1

    else:
        print("*SIGH*, READ THE QUESTION AGAIN\n"
              "*HINT ITS A WORD STARTS WITH M*\n"
              "**{} ANSWER THE QUESTION.**\n".format(name))

os.system("cls")

l4 = 2
while l4 == 2:
    Level_4 = input("Level 5\n"
                    "Choose a door to survive, I think this is the last door\n"
                    "*Behind Door 1 there is a gigantic fire breathing lizard that could burn you live*\n"
                    "*Behind Door 2 there is a dense jungle filled with deadly creatures*<---CHOOSE THIS\n"
                    "*Behind Door 3 there is lake of ice water that freezes everything in several seconds*\n")

    if Level_4 == "DOOR1" or Level_4 == "1":
        print("*DUH THERE IS NO THING CALLED FIRE BREATHING lizard*\n"
              "YOU ARE SMART, YOU ARE DIFFERENT FROM OTHERS, WHO TIRED THIS MAZE\n"
              "THEY HAD NO CHANCE OF SURVIVING THIS MAZE\n"
              "YOU MIGHT SAW SOME DEAD BODY'S ON THE WAY HERE, DON'T WORRY ABOUT THEM.TRUST ME\n"
              "You passed this level on to the next level!\n")
        l4 = 1

    elif Level_4 == "DOOR2" or Level_4 == "2":
        print("YOU REALLY FELL FOR IT.DAMN YOU ARE DUMB (╬▔皿▔)╯")
        dead()
        quit()

    elif Level_4 == "DOOR3" or Level_4 == "3":
        print("MATE I SAID IN SECONDS, NOT IN HOURS (╬▔皿▔)╯")
        dead()
        quit()

    else:
        wrong()

print("HEY {} THIS IS THE LAST LEVEL, YOU MADE IT.\n"
      "BUT WAIT THERE IS A GATE WHAT WAS THE CODE.\n"
      "*HINT IT WAS 4 DIGITS WHICH YOU HAVE SEEN\n"
      "WHILE ESCAPING,THE ORDER IS SEQUENCE YOU SAW THEM IN.\n".format(name))

l1 = 2
while l1 == 2:
    L_5 = input("Enter The Code Here!\n")

    if L_5 == "9678":
        print("OH MY GOD WHAT'S HAPPENING, I THINK YOU FAILED....SORRY GOODBYE!\n"
              "JUST KIDDING YOU WON, YOU SURVIVED THE JUNGLE MAZE. WELL DONE {}!"
              "YOU BEATEN THE GAME, NO WE DEFEATED IT AS A FAMILY.\n"
              "YO WHAT'S HAPPENING...., IS THAT DOM TORETTO, DID ANYONE SAY FAMILY\n"
              "⊙﹏⊙∥....AHHHH".format(name))

    l1 = 1

else:
    print("I THINK YOU ARE STUCK WITH ME. LET'S GO, YOU KNOW YOU AND ME AGAIN LIKE IN THE BEGINNING\n")
    wrong()

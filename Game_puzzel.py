print("Well *NAME* you passed the door maze,\n"
      "This level is puzzles they wont be hard or easy,\n"
      "so write the answer you know.\n"
      
      "**ONE IMPORTANT THING IF YOU GET IT WRONG YOU ARE DEAD**\n"
      "**ANSWERS MUST BE IN CAPITALS\n")
l1 = 2
while l1 == 2:
    P_1 = input("Level 3 \n"
                "What is 2+2 \n")

    if P_1 == "FOUR" or P_1 == "4":
        print("You passed this level on to the next level!\n"
              "THE CODE IS 68")
        l1 = 1

    else:
        print("Please answer the question {}!\n"
              "\n**ANSWER HAVE TO BE IN CAPITALS\nOR JUST THE NUMBER**")

l1 = 2
while l1 == 2:
    P_2 = input("Level 4 \n"
                "What is 1+1 \n")

    if P_2 == "TWO" or P_2 == "2":
        print("You passed this level on to the next level!\n"
              "THE CODE IS 78")
        l1 = 1

    else:
        print("Please answer the question {}!\n"
              "\n**ANSWER HAVE TO BE IN CAPITALS\nOR JUST THE NUMBER**")

show_instruction = ""
while show_instruction.lower() != "xxx":
    # ask the user if they have played before
      show_instruction = input("Have you played this game before?").lower()



     if show_instruction == "yes" or show_instruction == "y":
       show_instruction = "yes"
       print("program continues")

     elif show_instruction == "no" or show_instruction == "n":
         show_instruction ="no"
         print("display instructions")

     else:
         print("Please answer yes / no")




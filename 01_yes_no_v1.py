show_instructions = input("Have you played this game before? ").strip().lower()
if show_instructions == "yes":
    print("program continues")
elif show_instructions == "no":
    print("display instructions")
elif show_instructions == "n":
    print("display instructions")
else:
    print("please answer yes or no ")

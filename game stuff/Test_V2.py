import random
import os
import time

os.system("color")
# colour escape code
green = "\033[5;32;40m"
red = "\033[1;31;40m"
yellow = "\033[1;33;40m"


# functions


def question_check(question, answer_list, error_message):
    valid = False
    while not valid:

        response = input(question).lower().strip()

        for item in answer_list:
            if response == item[0] or response == item:
                answer = item
                return answer

        # output error if item not in list
        print(error_message)
        print()


def number_checker(question, mini, maxi, error_message):
    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low/ too high give
            if mini <= response <= maxi:
                return response

            else:
                print(error_message)
        except ValueError:
            print(error_message)


def instruction():
    decorations(" INTRODUCTION ", "#", yellow)
    print("at the start you can choose the number of decks you want to play with\n"
          " you can put up to $10 in the bank. the amount of money you put in the ban is the amount you will play with for the entire game\n"
          "\n"
          "at the start of every game you must make a bet from $1 to the amount in your bank\n"
          "you are given 2 cards at the start\n"
          "the goal of the game is to get a total higher than the dealer without going higher than 21\n"
          "\n")
    decorations("card value", "#", green)

    print("'K', 'Q', 'J'= 10\n"
          "number cards are equal to their number\n"
          "'A' = 11 or 1\n"
          "\n"
          "\n")
    decorations(" moves ", "#", yellow)
    print("hit - pick up one card\n"
          "stay - end turn\n"
          "double up - bet will double but pick up one card\n"
          "")


def deal(pick_amount, who_deck, who_num_deck, who):
    for i in range(pick_amount):
        card = deck.pop()
        who_deck.append(card)
        s = counter(who_num_deck)
        if card == "J" or card == "Q" or card == "K":
            who_num_deck.append(10)
        elif card == "A":
            if s + 11 <= 21:
                who_num_deck.append(11)
            else:
                who_num_deck.append(1)
        else:
            who_num_deck.append(card)
    print(who + " total is {}".format(counter(who_num_deck)))


def counter(add):
    count = sum(add)
    return count


def decorations(word, decor, colour):
    side = decor * 5
    statement = ("{} {} {}".format(side, word, side))
    decor_tb = decor * len(statement)

    print(colour + decor_tb)
    print(colour + statement)
    print(colour + decor_tb)
    print("\033[0;37;40m \n")
... (172 lines left

from colorama import init, Fore, Back, Style
import random

# putting the words from fiveletterwords.txt into a words list
with open('C:/Users/ethan/PycharmProjects/wordle/fiveletterwords.txt') as f:
    words = f.read().splitlines()

init()

loop = True

# the main game loop
while loop:
    # asks if the users want to start a new game

    command = input(Back.WHITE + Fore.BLACK + "Start a new game? (y/quit)" + Style.RESET_ALL)

    if command == "quit":
        loop = False

    # if yes, then enter a loop
    elif command == "y":
        inner_loop = 0

        # word is randomly chosen from the list of words
        word = random.choice(words)

        # add option to reveal word for testing purposes
        print("reveal word? should be used for testing purposes only :) (y/n)")
        test = True
        while test:
            # loop conditions
            ans = input()
            if ans.upper() == "Y":
                test = False
                print(word)
            elif ans.upper() == "N":
                test = False
                print("GOOD LUCK SOLDIER O7")
            else:
                print("please enter an actual answer, its really not that hard just y/n")

        # inner game loop
        while inner_loop < 6:
            attempt = input("enter a word")

            while attempt not in words:
                attempt = input("please enter an actual word")

            # Game logic
            output = ""
            for i in range(len(word)):

                # if the letter is in the right place
                if attempt[i] == word[i]:
                    output = output + Back.RED + attempt[i] + Back.RESET

                # if the letter is in the wrong place but in the word
                elif attempt[i] in word:
                    output = output + Back.YELLOW + attempt[i] + Back.RESET

                # if the letter is not in the word at all
                else:
                    output = output + attempt[i] + Back.RESET

            print(output)

            # if u got the entire word right
            if word == attempt:
                print("Congrats")

                # Reset game
                inner_loop = inner_loop + 6

            # decrease the number of tries that you got
            inner_loop = inner_loop + 1


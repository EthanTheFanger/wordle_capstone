import random
import re
from collections import Counter
from unittest import result

# this program is designed to be played alongside you during wordle, not for you
# THIS PROGRAM IS NOT FINISHED
# this was also built by following a guide:
# https://betterprogramming.pub/building-a-wordle-bot-in-under-100-lines-of-python-9b980539defb

# import a list of five-letter words
with open('C:/Users/ethan/PycharmProjects/wordle/fiveletterwords.txt') as f:
    words = f.read().splitlines()


# takes a list of words and then makes a guess based off of it
def guess(valid_words):
    guess = None

    lowest_worst_score = len(valid_words) + 1
    lowest_total_score = len(valid_words) ** 2

    for possible_guess in valid_words:
        # First, figure out the worst possible and total/average remaining words for this guess
        worst_score = 0
        total_score = 0

        for possible_answer in valid_words:
            # reuse our old get_result method from before, nice
            result = get_res(possible_guess, possible_answer)
            num_new_valid_words = len(update_words(valid_words, possible_guess, result))
            worst_score = max(num_new_valid_words, worst_score)
            total_score += num_new_valid_words

        # If this possble guess has a lower total/average number of words remaining, use it instead
        if worst_score < lowest_worst_score:
            guess = possible_guess
            lowest_worst_score = worst_score
            lowest_total_score = total_score

        # If it's a tie in average words remaining, choose the one that doesn't have the worst case
        elif worst_score == lowest_worst_score and total_score < lowest_total_score:
            guess = possible_guess
            lowest_worst_score = worst_score
            lowest_total_score = total_score
    return guess


# collects the results of the guess from the user, as they are playing
def collect_res():
    ask = input("what is the result? ( _ / ? / ! )").strip()
    a = ["_", "?", "!"]

    # check if the user puts in an actual input, check for length and for if the only characters are contained in the
    # list a
    if len(ask) != 5:
        print("that is not a correct response, try again")
        collect_res()

    for i in ask:
        if i not in a:
            print("that is not a correct response, try again")
            collect_res()

    return ask

    # a shorter, regex matching alternative

    # match = re.match(r'^[!?_]{5}$', result)
    # if not match:
    #     print("that is not a correct response, try again")
    #     return collect_res()


# returns the result for a guess if we knew the answer
def get_res(guess, answer):
    result = ""

    for pos, ch_guess, ch_answer in zip(range(5), guess, answer):
        # if the character is in the correct place
        if ch_guess == ch_answer:
            result += "!"
        # if the character is in the wrong place but in the word
        elif ch_guess in answer:
            result += "?"
        # if it is not in the answer at all
        else:
            result += "_"

    return result


# updates the list of words based on the guesses and the result
def update_words(words, guess, result):
    return [word for word in words if get_res(guess, word) == result]


# puts together the functions
def solve():
    valid_words = words

    while True:
        res = guess(valid_words)
        print("Guess: " + res.upper())
        if collect_res() == "!!!!!":
            print("I won!")
            break
        valid_words = update_words(valid_words, res, result)


solve()

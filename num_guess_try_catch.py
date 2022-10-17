#!/usr/bin/env python3
# Created by: Frankie fox
# Created on: Oct 17, 2022
# This program checks if the number is the answer
import random


def main():
    # The random number generator
    rand_num = random.randint(0, 9)

    # Get numbers that you can guess
    user_guess_as_string = input("Enter a number between 0 and 9: ")
    print()

    try:
        ran_num_as_int = int(user_guess_as_string)
        if user_guess_as_string == rand_num:
            print("You guessed correct")
        if user_guess_as_string != rand_num:
            print("You guessed wrong < The correct answer is {}>".format(rand_num))
    except Exception:
        print("This is not an integer ")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()

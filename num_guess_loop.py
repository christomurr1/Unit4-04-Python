#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 11 27, 2025
# This program uses a while loop to let the user guess a number until they get it right

import random


def main():
    # Pick a random number between 0 and 9
    correct_number = random.randint(0, 9)

    print("Guess the number between 0 and 9!")
    # loop runs until break
    while True:
        # try to convert input to a number
        try:

            guess = int(input("Enter your guess: "))
        except ValueError:

            print("Invalid input! Please enter a number between 0 and 9.")
            # go back to the start of the loop
            continue

        if guess == correct_number:
            print(" Correct! You guessed the number.")
            # exit the loop once correct
            break
        else:
            print("Wrong guess, try again!")


if __name__ == "__main__":
    main()

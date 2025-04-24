#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: Apr 23, 2025
# This program that allows users to guess numbers until they got it correct

import random


def main():
    # this function uses a break statement

    # Greeting message
    print("Hello. welcome to the number guess program")
    # Generate a random integer between 0 and 9 (inclusive)
    random_num = random.randint(0, 9)

    # Start an infinite loop, which will continue until the user guesses the number correctly
    while True:
        user_guess_str = input("Please guess a number between 0 to 9: ")
        try:
            # Try converting the input string to an integer
            user_guess = int(user_guess_str)

            # Check if the guess is outside the valid range
            if user_guess < 0 or user_guess > 9:
                print("Please enter a number between 0 to 9")
            else:
                # Check if the user's guess matches the right number
                if random_num == user_guess:
                    print("You guess it right!")
                    # Exit the loop since the guess is correct
                    break
                else:
                    print("Try one more time")

        except Exception:
            # Any error that occurs if input cannot be converted to int
            print("Please enter a positive integer")
            
    # After loop ends, thank the user for playing
    print("Thank you for using!")


if __name__ == "__main__":
    main()

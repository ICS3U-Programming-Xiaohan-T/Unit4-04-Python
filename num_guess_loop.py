#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: Apr 23, 2025
# This program that allows users to guess numbers until they got it correct

import random


def main():
    # this function uses a break statement

    #
    print("Hello. welcome to the number guess program")
    random_num = random.randint(0, 9)

    while True:
        user_guess_str = input("Please guess a number between 0 to 9: ")
        try:
            user_guess = int(user_guess_str)
            if user_guess < 0 or user_guess > 9:
                print("Please enter a number between 0 to 9")
            else:
                if random_num == user_guess:
                    print("You guess it right!")
                    break
                else:
                    print("Try one more time")

        except Exception:
            print("Please enter a positive integer")

    print("Thank you for using!")


if __name__ == "__main__":
    main()

#!/usr/bin/python3

import random


def display_instructions(difficulty):
    print("\tWelcome to the Number Guessing Game!%")
    print("You will be competing with the computer.")
    print("Difficulty Level: {}".format(difficulty))


def get_user_choice(number_range):
    while True:
        try:
            user_choice = int(input("Choose a number: "))
            if 1 <= user_choice <= number_range:
                return user_choice
            else:
                print("Invalid input. Please enter a number between 1 and {}.".format(number_range))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def compare_choices(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Congratulations! You win!")
        return True
    elif user_choice < computer_choice:
        print("Oops! Your guess is lower. Try again.")
    else:
        print("Oops! Your guess is higher. Try again.")
    return False


def play_game(difficulty):
    levels = {1: (4, 5), 2: (6, 10), 3: (5, 20)}
    if difficulty not in levels:
        print("Invalid difficulty level.")
        return
    guess_limit, number_range = levels[difficulty]
    score = 100
    display_instructions(difficulty)

    while guess_limit > 0:
        print("You have {} more guesses. Choose between 1 and {}.".format(guess_limit, number_range))
        user_choice = get_user_choice(number_range)
        computer_choice = random.randint(1, number_range)
        print("Your choice is: {}, "
              "Computer's choice is: {}".format(user_choice, computer_choice))
        if compare_choices(user_choice, computer_choice):
            print("Your score is: {} out of 100".format(score))
            break

        guess_limit -= 1
        score -= 10

    play_again = input("Do you want to play again (if yes, choose a higher level)? (yes/no): ")
    if play_again.lower() == "yes":
        new_difficulty = int(input("Choose the difficulty level (1, 2, or 3): "))
        play_game(new_difficulty)
    else:
        print("Thanks for playing the game!")


difficulty = int(input("Choose the difficulty level (1, 2, or 3): "))
play_game(difficulty)

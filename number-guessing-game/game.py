#!/usr/bin/python3
import random


def play_game():
    # Get the number of guesses allowed from the user
    guess_limit = int(input("Enter the number of guesses you want: "))
    score = 100

    # Print the game instructions
    print("Welcome to the Number Guessing Game!")
    print("You will be competing with the computer.")

    while True:
        # Display the number of remaining guesses
        print("You have {} more guesses.".format(guess_limit))
        try:
            user_choice = int(input("Choose a number between 1 and 10: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        computer_choice = random.randint(1, 10)
        print("Your choice is: {}, "
              "Computer's choice is: {}".format(user_choice, computer_choice))
        if user_choice == computer_choice:
            print("Congratulations! You win!")
            print("Your score is: {} out of 100".format(score))
            break
        elif user_choice < computer_choice:
            print("Oops! Your guess is lower. Try again.")
        else:
            print("Oops! Your guess is higher. Try again.")

        # Decrement guess limit and score
        guess_limit -= 1
        score -= 10
        if guess_limit == 0:
            print("You've exhausted your guess limit.")
            print("Game over!")
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thanks for playing the game!")


play_game()

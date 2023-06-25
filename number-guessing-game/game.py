#!/usr/bin/python3
import random

guess = 10
print("Welcome to Numnber Guessing Game")
print("You will be competing with Computer")
while True:
    print("You have {} more guesses".format(guess))
    user_choice = int(input("Choose a number between 1-10: "))
    computer_choice = random.randint(1, 10)
    print("Your Choice is: ", user_choice,
          "Computer's Choice is: ", computer_choice)
    if user_choice == computer_choice:
        print("You win, congratulations")
    elif user_choice < computer_choice:
        print("Ops no, yours lower, try again")
    else:
        print("Ops no, yours higher, try again")
    guess -= 1
    choice = input("You wanna try again? (yes/no): ")
    if choice.lower() != "yes":
        print("Thanks for playing this game")
        break

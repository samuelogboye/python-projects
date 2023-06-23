#!/usr/bin/python3
import math


def main():
    while True:
        try:
            print("Hi Sweet, welcome to this calculator")
            first_number = float(input("Enter the first number: "))
            print("Select the operation you wish to perform:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (x)")
            print("4. Division (/)")
            print("5. Exponentiation(**)")
            print("6. Advanced Functionalities")
            print("7. Exit")

            operand = int(input("Enter the number relating to your choice: "))
            if operand in [1, 2, 3, 4, 5]:
                second_number = float(input("Enter the second number: "))
                if operand == 1:
                    result = first_number + second_number
                elif operand == 2:
                    result = first_number - second_number
                elif operand == 3:
                    result = first_number * second_number
                elif operand == 4:
                    result = first_number / second_number
                elif operand == 5:
                    result = first_number ** second_number
                elif operand == 6:
                    print("Select the operation you wish to perform:")
                    print("1. Square root(√)")
                    print("2. Logarithm Operations(log)")
                    print("3. Trigonometry(sin)")
                    print("4. Trigonometry(cos)")
                    print("5. Trigonometry(tan)")
                    advanced_operand = int(
                        input("Enter the number relating to your choice: "))
                    if advanced_operand == 1:
                        result = math.sqrt(first_number)
                    elif advanced_operand == 2:
                        result = math.log(first_number)
                    elif advanced_operand == 3:
                        result = math.sin(first_number)
                    elif advanced_operand == 4:
                        result = math.cos(first_number)
                    elif advanced_operand == 5:
                        result = math.tan(first_number)
                    else:
                        print("Invalid Operand, please try again")
                elif operand == 7:
                    print("Thanks for using this calculator")
                    exit()
                else:
                    print("Invalid Operand, please try again")
                print("Printing the result...........")
                print(result)
                choice = input("You wanna perform more operations? (yes/no): ")
                if choice.lower() != "yes":
                    print("Thanks for using this calculator")
                    break
        except ValueError:
            print("Hi Sweet, You got value error")
            exit()
        except ZeroDivisionError:
            print("Hi Sweet, You can't divide by Zero")
            exit()


if __name__ == "__main__":
    main()

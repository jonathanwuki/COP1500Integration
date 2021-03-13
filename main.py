# A basic command line virtual assistant which assists in math equations as well as miscellaneous commands.
# Author: Jonathan Wukitsch
__author__ = "Jonathan Wukitsch"

import os
import platform
import random


#region Helper functions

# Validate user input for the calculator function (make sure it's a valid number)
def validate_input(num):
    try:
        float(num)
    except ValueError:  # This will be thrown if the input isn't a number
        return False
    return True


# This isn't really necessary in PyCharm/VSCode since it uses a virtual environment
# (cls or clear both work) but we might as well handle it anyway
def clear_console():
    user_system = platform.system()

    if user_system == "Windows":
        os.system("cls")  # Windows uses "cls" to clear the console
    elif user_system == "Darwin" or user_system == "Linux":  # macOS/Linux
        os.system("clear")  # UNIX systems use "clear" to clear the console
    else:
        print("You are using an unsupported operating system (%s). This program will now exit." % user_system)
        quit()

#endregion


#region Calculator functions

def add(num1, num2):
    if validate_input(num1) and validate_input(num2):
        return float(num1) + float(num2)  # Perform addition according to project specifications
    else:
        # I really shouldn't be returning a string here since in normal operation, this function should output a number.
        # The way this program was written allows for this (it never *explicitly* expects a number),
        # but this is definitely not best practice.
        return "Error. Invalid input numbers."


def subtract(num1, num2):
    if validate_input(num1) and validate_input(num2):
        return float(num1) - float(num2)  # Perform subtraction according to project specifications
    else:
        return "Error. Invalid input numbers."


def multiply(num1, num2):
    if validate_input(num1) and validate_input(num2):
        return float(num1) * float(num2)  # Perform multiplication according to project specifications
    else:
        return "Error. Invalid input numbers."


def divide(num1, num2):
    if validate_input(num1) and validate_input(num2):
        try:
            return float(num1) / float(num2)  # Perform division according to project specifications
        except ZeroDivisionError:
            return "Error. You cannot divide by zero."
    else:
        return "Error. Invalid input numbers."


def modulus(num1, num2):
    if validate_input(num1) and validate_input(num2):
        try:
            return float(num1) % float(num2)  # Perform modulus according to project specifications
        except ZeroDivisionError:
            return "Error. You cannot divide by zero."
    else:
        return "Error. Invalid input numbers."


def exponent(num1, num2):
    if validate_input(num1) and validate_input(num2):
        return float(num1) ** float(num2)  # Perform exponential operations according to project specifications
    else:
        return "Error. Invalid input numbers."


def floor_division(num1, num2):
    if validate_input(num1) and validate_input(num2):
        try:
            return float(num1) // float(num2)  # Perform floor division according to project specifications
        except ZeroDivisionError:
            return "Error. You cannot divide by zero."
    else:
        return "Error. Invalid input numbers."

#endregion


#region Main program function

def main():
    user_full_name = input("Hello! Please enter your name to begin: ")  # Input according to project specifications

    # Check for empty/whitespace name
    while user_full_name == "" or user_full_name.isspace():  # While loop according to project specifications
        user_full_name = input("You need to enter a name. What is your name? ")

    clear_console()  # Purely cosmetic to dismiss the prompt above

    print("Hello %s!" % user_full_name)  # Greet the user according to project specifications

    calculator_commands = ["add",
                           "subtract",
                           "multiply",
                           "divide",
                           "modulus",
                           "remainder",  # Duplicate of modulus command
                           "exponent",
                           "floor division"]

    all_available_commands = calculator_commands + \
                             ["joke",
                              "echo",
                              "guess num",
                              "invert triangle",
                              "quit"]

    # Each joke in the following bank was retrieved from https://www.rd.com/jokes/computer/.
    joke_bank = ["Have you heard the band \"1023 Megabytes\"? They're pretty good, but they don't have a gig just yet.",
                 "Don't use \"beef stew\" as a computer password. It's not stroganoff.",
                 "Why did the computer show up at work late? It had a hard drive.",
                 "What do you call an iPhone that isn't kidding around? Dead Siri-ous!",
                 "Did you hear about the monkeys who shared an Amazon account? They were Prime mates."]

    print("==========\nAvailable commands:\n")
    print(*all_available_commands, sep=", ", end="\n==========\n")  # Print statement with separator argument according to proj. specs
    user_input = input("Enter a command: ").lower()

    # This while loop is necessary so I can
    # re-prompt the user for input and continue the loop below if they enter something invalid.
    terminate_program = False
    while not terminate_program:
        while user_input in all_available_commands:  # "in" statement according to project specifications

            print("Okay.")  # We're trying to emulate a virtual assistant here, you know?

            if user_input in calculator_commands:  # "if" statement according to project specifications
                input_num1 = input("Enter the first number: ")
                input_num2 = input("Enter the second number: ")

                # This is only here to silence a PyCharm warning complaining that result could be non-existent,
                # but this would never be the case due to the way the program was written.
                result = None

                if validate_input(input_num1) and validate_input(input_num2):  # "and" operator according to proj. specs
                    if user_input == "add":  # == relational operator according to project specifications
                        result = add(input_num1, input_num2)

                        # String concatenation according to project specifications
                        print("\n" + input_num1 + " + " + input_num2 + "\n=")
                    elif user_input == "subtract":  # "elif" statement according to project specifications
                        result = subtract(input_num1, input_num2)
                        print("\n" + input_num1 + " - " + input_num2 + "\n=")
                    elif user_input == "multiply":
                        result = multiply(input_num1, input_num2)
                        print("\n" + input_num1 + " * " + input_num2 + "\n=")
                    elif user_input == "divide":
                        result = divide(input_num1, input_num2)
                        print("\n" + input_num1 + " / " + input_num2 + "\n=")
                    elif user_input == "modulus" or user_input == "remainder":  # "or" operator according to proj. specs
                        result = modulus(input_num1, input_num2)
                        print("\nThe answer is:")
                    elif user_input == "exponent":
                        result = exponent(input_num1, input_num2)
                        print("\n" + input_num1 + " ^ " + input_num2 + "\n=")
                    elif user_input == "floor division":
                        result = floor_division(input_num1, input_num2)
                        print("\nThe answer is:")
                    else:  # "else" statement according to project specifications
                        print("\nThat isn't a command.\n")
                        result = "invalid"

                # I want to validate these separate from the above if statement,
                # because if the user enters two non-numbers, the program will otherwise
                # only tell them that they inputted the first number incorrectly.
                if not validate_input(input_num1):  # "not" boolean operator according to project specifications
                    print("\nNumber 1 isn't valid.")
                    result = "invalid"

                if not validate_input(input_num2):
                    print("Number 2 isn't valid.")
                    result = "invalid"

                if result is not None:  # The result *should* never be a None type, but we'll check just to make sure
                    # The result could be "invalid" depending on user input but this is handled elsewhere,
                    # so let's not worry about it here
                    if result != "invalid":
                        # Converting result to a string here and replacing .0 with nothing for enhanced readability
                        print(("%s" % result).replace(".0", ""))  # The result has yet to be printed, so let's do that
            else:  # User did not enter a calculator command
                if user_input == "joke":  # Tell a random joke
                    print("\n" + random.choice(joke_bank))
                elif user_input == "echo":  # Put the user in an echo chamber.
                    print("\nWelcome to the echo chamber!", end=" ")  # Use end argument according to proj. specs
                    echo_statement = input("Make your voice heard! Enter something: ")

                    while echo_statement == "" or echo_statement.isspace():
                        print("\nYou need to enter something!")
                        echo_statement = input("Make your voice heard! Enter something: ")

                    print(("\n" + echo_statement) * 15)  # Use * string operator according to proj. specifications

                elif user_input == "guess num":  # Generate a random number and have the user guess what it is.
                    random_num = random.randint(1, 10)  # Random number between 1 and 10

                    user_guess = input("Guess any number between 1 and 10! But beware, if you choose incorrectly, the number will change! ")

                    if validate_input(user_guess):
                        while int(user_guess) != random_num:  # != relational operator according to proj. specs
                            if int(user_guess) < random_num:  # < relational operator according to proj. specs
                                print("You guessed too low! Try again.")
                                if random_num < 10:  # Only increment if we are less than 10
                                    random_num += 1  # Shortcut operator according to proj. specs
                            elif int(user_guess) > random_num:  # > relational operator according to proj. specs
                                print("You guessed too high! Try again.")
                                if random_num > 1:  # Only decrement if we are greater than 1
                                    random_num -= 1  # Shortcut operator according to proj. specs
                            else:
                                print("Oh my. It looks like an error has occurred. Please try again.")

                            user_guess = input("Guess any number between 1 and 10! But beware, if you choose incorrectly, the number will change! ")

                        print("You guessed correctly! The number was %s." % random_num)
                    else:
                        print("That isn't a number! Try again next time.")
                elif user_input == "invert triangle":  # Display inverted triangle (rows determined by user)
                    row_count = input("Enter number of rows to display: ")

                    if validate_input(row_count):
                        for i in range(0, int(row_count)):  # For loop according to proj. specs
                            for x in range(1, int(row_count) - i + 1):  # range() function according to proj. specs
                                print(x, end=" ")
                            print()
                elif user_input == "quit":  # User wants to quit the program
                    quit_input = input("Are you sure you want to quit? Enter Y to confirm. ").lower()
                    if quit_input == "y":
                        terminate_program = True
                        break
                    else:
                        print("Exit aborted.")
                        user_input = input("Enter a command: ").lower()

            continue_input = input("\nPress any key to continue.\n")
            user_input = input("Enter a command: ").lower()
        else:  # User entered invalid command
            print("\nThat isn't a command. Try again.\n")
            user_input = input("Enter a command: ").lower()
    else:  # Handle exiting of program
        print("\nExiting program. Thank you, %s!" % user_full_name)
        quit()

#endregion


# Call to main
main()
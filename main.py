"""A basic command line virtual assistant (of sorts) which assists in
math equations as well as miscellaneous commands."""
__author__ = "Jonathan Wukitsch"

import os
import platform
import random


# region Helper functions

def validate_input(num):
    """
    Validates user input for the calculator function
    (makes sure it's a valid number).
    :param num: A number passed in to be validated.
    :return: True or False depending on validation outcome.
    """
    try:
        float(num)
    except ValueError:  # This will be thrown if the input isn't a number
        return False
    return True


def clear_console():
    """Clears the console for a cleaner appearance."""
    user_system = platform.system()

    if user_system == "Windows":
        os.system("cls")  # Windows uses "cls" to clear the console
    elif user_system == "Darwin" or user_system == "Linux":  # macOS/Linux
        os.system("clear")  # UNIX systems use "clear" to clear the console
    else:
        print("Unsupported operating system (%s). Exiting." % user_system)
        quit()


# endregion


# region Calculator functions

def add(num1, num2):
    """
    Adds two numbers together (after checking that they're both valid ints)
    and returns the result.
    :param num1: The initial number to be added to.
    :param num2: The number to add to the first number.
    :return: The result of the addition of each number.
    """
    if validate_input(num1) and validate_input(num2):
        # Perform addition according to project specifications
        return float(num1) + float(num2)
    else:
        return "Error. Invalid input numbers."


def subtract(num1, num2):
    """
    Subtracts two numbers from each other
    (after checking that they're both valid ints)
    and returns the result.
    :param num1: The initial number to be subtracted from.
    :param num2: The number to subtract from the first number.
    :return: The result of the subtraction of each number.
    """
    if validate_input(num1) and validate_input(num2):
        # Perform subtraction according to project specifications
        return float(num1) - float(num2)
    else:
        return "Error. Invalid input numbers."


def multiply(num1, num2):
    """
    Multiplies two numbers together
    (after checking that they're both valid ints) and returns the result.
    :param num1: The initial number to be multiplied.
    :param num2: The number to multiply the first number by.
    :return: The result of the multiplication of each number.
    """
    if validate_input(num1) and validate_input(num2):
        # Perform multiplication according to project specifications
        return float(num1) * float(num2)
    else:
        return "Error. Invalid input numbers."


def divide(num1, num2):
    """
    Divides two numbers (after checking that they're both valid ints)
    and returns the result
    :param num1: The first number (the number to be divided).
    :param num2: The number to divide the first number by.
    :return: The result of the division of the two numbers.
    """
    if validate_input(num1) and validate_input(num2):
        try:
            # Perform division according to project specifications
            return float(num1) / float(num2)
        except ZeroDivisionError:
            return "Error. You cannot divide by zero."
    else:
        return "Error. Invalid input numbers."


def perform_modulus(num1, num2):
    """
    Finds the remainder of two numbers
    (after checking that they're both valid ints) and returns the result.
    :param num1: The first number (to be divided).
    :param num2: The number to divide the first number by.
    :return: The remainder of the division of the two numbers.
    """
    if validate_input(num1) and validate_input(num2):
        try:
            # Perform modulus according to project specifications
            return float(num1) % float(num2)
        except ZeroDivisionError:
            return "Error. You cannot divide by zero."
    else:
        return "Error. Invalid input numbers."


def raise_to_power(num1, num2):
    """
    Sets one number's exponent to another
    (after checking that they're both valid ints) and returns the result.
    :param num1: The number of which to raise to a power.
    :param num2: The power to raise the first number to.
    :return: The result of the exponential operation of the two numbers.
    """
    if validate_input(num1) and validate_input(num2):
        # Perform exponential operations according to project specifications
        return float(num1) ** float(num2)
    else:
        return "Error. Invalid input numbers."


def divide_floor(num1, num2):
    """
    Divides two numbers and rounds down
    (after checking that they're both valid ints) and returns the result.
    :param num1: The number to be divided.
    :param num2: The number to divide the first number by.
    :return: The result of the (floor) division of the two numbers.
    """
    if validate_input(num1) and validate_input(num2):
        try:
            # Perform floor division according to project specifications
            return float(num1) // float(num2)
        except ZeroDivisionError:
            return "Error. You cannot divide by zero."
    else:
        return "Error. Invalid input numbers."


# endregion


# region Program sub-functions

def show_all_commands(commands_list):
    """Displays all of this program's available commands to the user."""
    print("==========\nAvailable commands:\n")

    # I know it would be ideal to return something here rather than just
    # printing it -- but I don't want to have to repeat the sep and end
    # arguments wherever I'm calling this function.

    # Print statement with separator argument according to proj. specs
    print(*commands_list, sep=", ",
          end="\n==========\n")


def run_echo_chamber():
    """Repeats user input 15 times to act as an 'echo' of sorts."""
    # Use end argument according to proj. specs
    print("\nWelcome to the echo chamber!", end=" ")
    echo_statement = input("Make your voice heard! "
                           "Enter something: ")

    while echo_statement == "" or echo_statement.isspace():
        print("\nYou need to enter something!")
        echo_statement = input("Make your voice heard! "
                               "Enter something: ")

    # Use * string operator according to proj. specs
    print(("\n" + echo_statement) * 15)


def run_guess_num():
    """Generates a random number and has the user guess it."""
    # Random number between 1 and 10
    random_num = random.randint(1, 10)

    user_guess = input("Guess any number between 1 and 10! "
                       "But beware, if you choose incorrectly,"
                       " the number will change! ")

    while validate_input(user_guess):
        if int(user_guess) != random_num:
            if int(user_guess) < random_num:
                print("\nYou guessed too low! Try again.\n")
                if random_num < 10:
                    # Only increment if we are less than 10

                    # Shortcut op. according to proj. specs
                    random_num += 1
            elif int(user_guess) > random_num:
                # > relational op. according to proj. specs
                print("\nYou guessed too high! Try again.\n")
                if random_num > 1:
                    # Only decrement if we are greater than 1

                    # Shortcut op. according to proj. specs
                    random_num -= 1
            else:
                print("Oh my. It looks like an error "
                      "has occurred. Please try again.")
        else:
            print("\nYou guessed correctly! "
                  "The number was %s." % random_num)
            break

        user_guess = input("Guess any number between "
                           "1 and 10! But beware, if you "
                           "choose incorrectly, the number"
                           " will change! ")
    else:
        print("\nThat isn't a number! Let's try this again...")
        run_guess_num()


def run_invert_triangle():
    """Displays an inverted triangle (rows determined by user)."""
    row_count = input("Enter number of rows to display: ")

    if validate_input(row_count):
        print()  # Empty line for cleaner look
        # For loop according to proj. specs
        for i in range(0, int(row_count)):
            # range() function according to proj. specs
            for x in range(1, int(row_count) - i + 1):
                print(x, end=" ")
            print()
    else:
        print("\nThat isn't a number! Try again.")
        run_invert_triangle()


# endregion


# region Main program function

def main():
    """The main function of the program, which handles almost all logic
    and core functionality."""
    # Input according to project specifications
    user_full_name = input("Hello! Please enter your name to begin: ")

    # Check for empty/whitespace name
    # While loop according to project specifications
    while user_full_name == "" or user_full_name.isspace():
        user_full_name = input("You need to enter a name. What is your name? ")

    clear_console()  # Purely cosmetic to dismiss the prompt above

    # Greet the user according to project specifications
    print("Hello %s!" % user_full_name)

    calculator_commands = ["add",
                           "subtract",
                           "multiply",
                           "divide",
                           "modulus",
                           "remainder",  # Duplicate of modulus command
                           "exponent",
                           "floor division"]

    all_available_commands = calculator_commands + ["joke",
                                                    "echo",
                                                    "guess num",
                                                    "invert triangle",
                                                    "commands",
                                                    "help",
                                                    "quit"]

    # Each joke in the following bank was retrieved from
    # https://www.rd.com/jokes/computer/.
    joke_bank = ["Have you heard the band \"1023 Megabytes\"? They're pretty"
                 " good, but they don't have a gig just yet.",
                 "Don't use \"beef stew\" as a computer password."
                 " It's not stroganoff.",
                 "Why did the computer show up at work late?"
                 " It had a hard drive.",
                 "What do you call an iPhone that isn't kidding around?"
                 " Dead Siri-ous!",
                 "Did you hear about the monkeys who shared an Amazon account?"
                 " They were Prime mates."]

    show_all_commands(all_available_commands)

    user_input = input("Enter a command: ").lower()

    # This while loop is necessary so I can
    # re-prompt the user for input and continue the loop below
    # if they enter something invalid.
    terminate_program = False
    while not terminate_program:
        # "in" statement according to project specifications
        while user_input in all_available_commands:

            # We're trying to emulate a virtual assistant here, you know?
            print("Okay.")

            # "if" statement according to project specifications
            if user_input in calculator_commands:
                input_num1 = input("Enter the first number: ")
                input_num2 = input("Enter the second number: ")

                # This is only here to silence a PyCharm warning complaining
                # that result could be non-existent,
                # but this would never be the case due to the way
                # the program was written.
                result = None

                # "and" operator according to proj. specs
                if validate_input(input_num1) and validate_input(input_num2):
                    # == relational operator according to project specs
                    if user_input == "add":
                        result = add(input_num1, input_num2)

                        # String concatenation according to project specs
                        print("\n" + input_num1 + " + " + input_num2 + "\n=")
                    elif user_input == "subtract":  # "elif" statement (proj.)
                        result = subtract(input_num1, input_num2)
                        print("\n" + input_num1 + " - " + input_num2 + "\n=")
                    elif user_input == "multiply":
                        result = multiply(input_num1, input_num2)
                        print("\n" + input_num1 + " * " + input_num2 + "\n=")
                    elif user_input == "divide":
                        result = divide(input_num1, input_num2)
                        print("\n" + input_num1 + " / " + input_num2 + "\n=")
                    elif user_input == "modulus" or user_input == "remainder":
                        # "or" operator according to proj. specs
                        result = perform_modulus(input_num1, input_num2)
                        print("\nThe answer is:")
                    elif user_input == "exponent":
                        result = raise_to_power(input_num1, input_num2)
                        print("\n" + input_num1 + " ^ " + input_num2 + "\n=")
                    elif user_input == "floor division":
                        result = divide_floor(input_num1, input_num2)
                        print("\nThe answer is:")
                    else:  # "else" statement according to project specs
                        print("\nThat isn't a command.\n")
                        result = "invalid"

                # I want to validate these separate from the above
                # if statement, because if the user enters two non-numbers,
                # the program will otherwise only tell them that they inputted
                # the first number incorrectly.

                # "not" boolean operator according to project specifications
                if not validate_input(input_num1) and not validate_input(
                        input_num2):
                    # Display a different error message
                    # if both numbers are invalid
                    print("\nUh oh! Neither of those are numbers. Please try "
                          "again.")
                    result = "invalid"
                else:  # Either the numbers are valid, or just one is invalid
                    if not validate_input(input_num1):
                        print(
                            "\nIt looks like your first input isn't a number."
                            " Please try again.")
                        result = "invalid"

                    if not validate_input(input_num2):
                        print(
                            "\nIt looks like your second input isn't a number."
                            " Please try again.")
                        result = "invalid"

                # The result *should* never be a None type,
                # but we'll check just to make sure
                if result is not None:
                    # The result could be "invalid" depending on user input,
                    # but this is handled elsewhere,
                    # so let's not worry about it here
                    if result != "invalid":
                        # Converting result to a string here and replacing .0
                        # with nothing for enhanced readability

                        # The result has yet to be printed, so let's do that
                        print(("%s" % result).replace(".0", ""))
            else:  # User did not enter a calculator command
                if user_input == "joke":  # Tell a random joke
                    print("\n" + random.choice(joke_bank))
                elif user_input == "echo":  # Put the user in an echo chamber
                    run_echo_chamber()
                elif user_input == "guess num":  # Have the user guess a number
                    run_guess_num()
                elif user_input == "invert triangle":
                    # Show an inverted triangle (rows determined by user)
                    run_invert_triangle()
                elif user_input == "commands" or user_input == "help":
                    # Show all available commands
                    show_all_commands(all_available_commands)
                elif user_input == "quit":  # User wants to quit the program
                    quit_input = input("Are you sure you want to quit? "
                                       "Enter Y to confirm. ").lower()
                    if quit_input == "y":
                        terminate_program = True
                        break
                    else:
                        print("Exit aborted.")

            input("\nPress enter to continue.\n")
            user_input = input("Enter a command: ").lower()
        else:  # User entered invalid command
            print("\nThat isn't a command. Try again.\n")
            user_input = input("Enter a command: ").lower()
    else:  # Handle exiting of program
        print("\nExiting program. Thank you, %s!" % user_full_name)


# endregion


if __name__ == '__main__':
    main()  # Call to main

"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
# Import the random module.
import random

# Create the start_game function.


def start_game():

    #   1. Display an intro/welcome message to the player.
    print("Hello and welcome (or welcome back) to the number guessing game.\U0001F916 Let's start and have some fun!")
    while True:
        try:
            number_guess = int(
                input("Please chose a number between 1 and 10:  "))
        # if value cant be turned into an integer throw error.
        except:
            print("Thats not an integer, please try again.")
            continue
        # if value is not in the allowed range throw error and keep looping, otherwise continue the program.
        else:
            if number_guess <= 0:
                print("Values smaller than 1 are not allowed, please try again.")
                continue
            elif number_guess > 10:
                print("Values larger than 10 are not allowed, please try again.")
                continue
            else:
                break

    #   2. Store a random number as the answer/solution.
    correct_number = random.randint(1, 10)

    #   3. Continuously prompt the player for a guess.
    # initializing the number of guesses the player needs
    number_of_guesses = 1

    # as long as the guess is not correct:

    while number_guess != correct_number:
        # increment number of guesses
        number_of_guesses += 1
        # display specific messages depending on whether the number is too low or too high
    #     a. If the guess is greater than the solution, display to the player "It's lower".
        if number_guess > correct_number:
            while True:
                try:
                    number_guess = int(
                        input("Nope thats not it.The correct number is lower.Please guess again:  "))
                    break
                except ValueError:
                    print("That was not a valid number. Please try again.")

    #     b. If the guess is less than the solution, display to the player "It's higher".
        elif number_guess < correct_number:
            while True:
                try:
                    number_guess = int(
                        input("Nope thats not it.The correct number is higher.Please guess again:  "))
                    break
                except ValueError:
                    print("That was not a valid number. Please try again.")

    # distingusih whether it hat been one or more guesses to get language right.
    if number_of_guesses == 1:
        print(f"Yeahy, you got it!\U0001F973\nIt took you 1 attempt to guess the right number.")
    else:
        print(
            f"Yeahy, you got it!\U0001F973\nIt took you {number_of_guesses} attempts to guess the right number.")
    # ending the game
    print("The game is over.")
    # return the amount of guesses needed to use it in case the player wants to play again.
    return number_of_guesses


# starting the game
number_of_guesses = start_game()
# storing old number of guesses as current high score
current_high_score = number_of_guesses

# ask the user whether he wants to play again after the first round, if so start again, if not, end game.
while True:
    play_again = input(
        "Would you like to play again? If so, please type 'y'.\nIf you dont want to play again, type 'n':   ").lower()
    if play_again == "y":
        # determine & display the current high score to the user
        print(
            f"The current high score is {current_high_score}. Let's see if you can beat it! Good luck.")
        number_of_guesses = start_game()
        if number_of_guesses < current_high_score:
            current_high_score = number_of_guesses
        else:
            current_high_score = current_high_score
    # message if user doesn't want to play again
    elif play_again == "n":
        print("Goodbye.\nHope to see you soon!\U0001F63A")
        break
    # message if input is neither n nor y
    else:
        print("Thats not a valid input.")

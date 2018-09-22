""" Random number guessing game"""

import random


def main():

    """Print out the goal of the game."""
    print(" Hey there! I am thinking of an integer between 0 and 50.")

    #create the secret number
    secret = random.randrange(1,51)

    #create attempt counter
    attempt_count = 1

    #create initial guess to something outside of the range for intialization purposes
    user_guess = -1

    #create while loop until user guests secret number or number of attempts is exceeded
    while user_guess != secret and attempt_count < 6:

        #show attempt number and get guess
        print("--- attempt", attempt_count)
        user_guess = int(input("What is your guess: "))

        # show high or low or win
        if user_guess > secret:
            print("Too High!")
        elif user_guess < secret:
            print("Too Low!")
        else:
            print("You guessed correctly!")

        #advance the attempt
        attempt_count += 1

    if user_guess != secret:
        print("You ran out of attempts.  The secret number was " + str(secret) + ".")





if __name__ == "__main__":
    main()
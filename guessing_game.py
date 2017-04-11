import random
import os


def clear():
    os.system('clear')


def play_again():
    play_again = input("Game over, restart? Y/n \n")
    if play_again.lower() != "n":
        game()
    else:
        print("See you next time!")


def game():
    secret_num = random.randrange(100)
    guesses = []
    turns = 0
    while len(guesses) < 5:
        if len(guesses) == 0:
            clear()
            print("Welcome to the number game!")
        try:
            guess = input("Turns: [{}]\nGuess a number "
                          "between 1 and 100: ".format(turns))
            guess = int(guess)
            if guess in guesses:
                print("You already tried {}! Come on, brain!\n".format(guess))
                continue
            elif guess == '':
                break
            guesses.append(guess)
            turns += 1
        except ValueError:
            input("{} isn't a number!\n".format(guess))
        else:
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                print("You took {} turns!".format(turns))
                break
            elif guess < secret_num:
                print("My number is higher than {}\n".format(guess))
            else:
                print("My number is lower than {}\n".format(guess))
    else:
        clear()
        print("You didn't get it! My number was {}\n".format(secret_num))
    play_again()


game()

import random

# define terminal colours
def prGreen(skk):
    print("\033[92m{}\033[00m".format(skk))
def prRed(skk):
    print("\033[91m{}\033[00m".format(skk))

def prPurple(skk):
    print("\033[95m{}\033[00m".format(skk))

# Print necessary information
prPurple("Welcome to rock paper scissors! For rock, type r, for paper, type p, and for scissors, type s. Best of 3, and goodluck!")

# Setup variables + computer's response
computer_score = 0
user_score = 0
options = ["r", "p", "s"]
response = random.choice(options)

# bulk of code
def game():

    # scoring system
    def scores():
        global computer_score
        global user_score

        if user_score == 3:
            prGreen("You win!")
            exit()

        elif computer_score == 3:
            prRed("The computer wins!")
            exit()

    # input validation

    def checker():
        global computer_score
        global user_score
        global response
        if response == user_input:
            prPurple("Reroll!")
            game()

        elif response == "r" and user_input == "p":
            prGreen("You get a point!")
            user_score = user_score + 1
            scores()
            game()

        elif response == "r" and user_input == "s":
            prRed("The computer gets a point!")
            computer_score = computer_score + 1
            scores()
            game()

        elif response == "s" and user_input == "r":
            prGreen("You get a point!")
            user_score = user_score + 1
            scores()
            game()

        elif response == "s" and user_input == "p":
            prRed("The computer gets a point!")
            computer_score = computer_score + 1
            scores()
            game()

        elif response == "p" and user_input == "r":
            prRed("The computer gets a point!")
            computer_score = computer_score + 1
            scores()
            game()

        elif response == "p" and user_input == "s":
            prGreen("You get a point!")
            user_score = user_score + 1
            scores()
            game()

        else:
            prRed("Your response is not valid. Please try again.")
            game()

    # take in user input
    user_input = input("What is your input? ")
    user_input = user_input.lower()
    checker()

# starting the game!
game()




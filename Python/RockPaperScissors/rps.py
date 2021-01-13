import random

#defines computer roll
r = int()

#defines user choice
user_c = int()

#prints Rock
def rock():
    return("Rock")

#prints Paper
def paper():
    return("Paper")

#prints Scissors
def scissors():
    return("Scissors")

#python dictionary to be used as a switch statement for our choices
comp = {1: rock,
        2: paper,
        3: scissors,}

#computer rolls 1-3 to see which it will choose
def roll():
    #Makes sure global variable is beign changed, and rolls random number 1-3
    global r
    r = random.randrange(1, 4)
    #uses python dictionary in exchange for a switch statement to find what the rolls corresponds to
    cr = comp[r]()
    print("The computer has chosen: " + cr)

#Asks user for thier choice between 1-3 for rock paper or scissors in said order
def user():
    #Makes sure global variable is beign changed, and takes input and converts input to int
    global user_c
    user_c = int(input("Hello, please enter your input for Rock(1) Paper(2) Scissors(3): "))
    #uses switch statement to check as roll
    u_roll = comp[user_c]()
    print("You have chosen: " + u_roll)

#Checks who won the game by running though various else if statements, there should be a better way tbh.
def winner():
    if user_c == r:
        print("It's a tie!")
    elif user_c == 1 and r == 3:
        print("User Wins!")
    elif user_c == 3 and r == 1:
        print("Computer Wins!")
    elif user_c > r: 
        print("User Wins!")
    elif user_c < r:
        print("Computer Wins!")

    #these were cut out due to the results being the same in accordance to the conditions
    # elif user_c == 2 and r == 1:
    #     print("User Wins!")
    # elif user_c == 3 and r == 2:
    #     print("User Wins!")
    # elif user_c == 1 and r == 2:
    #     print("Computer Wins!")
    # elif user_c == 2 and r == 3:
    #     print("Computer Wins!")
user()
roll()
winner()
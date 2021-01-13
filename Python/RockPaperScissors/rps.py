import random

#defines computer choice
comp_c = int()

#defines user choice
user_c = int()

#defines game counter
game_c = 0

#defines game status
game_active = True

#defines computer score
c_score = 0

#defines user score
u_score = 0

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
choice = {1: rock,
        2: paper,
        3: scissors,}

#computer rolls 1-3 to see which it will choose
def comp():
    #Makes sure global variable is beign changed, and rolls random number 1-3
    global comp_c
    comp_c = random.randrange(1, 4)
    #uses python dictionary in exchange for a switch statement to find what the rolls corresponds to
    cr = choice[comp_c]()
    print("The computer has chosen: " + cr)

#Asks user for thier choice between 1-3 for rock paper or scissors in said order
def user():
    #Makes sure global variable is beign changed, and takes input and converts input to int
    global user_c
    user_c = int(input("Hello, please enter your input for Rock(1) Paper(2) Scissors(3): "))
    #uses switch statement to check as roll
    u_roll = choice[user_c]()
    print("You have chosen: " + u_roll)

#Checks who won the game by running though various else if statements, there should be a better way tbh.
def game_logic():
    #calls globals c_score and u_score to update them to see who wins best out of 5
    global c_score
    global u_score
    
    if user_c == comp_c:
        print("It's a tie!\nResult: No one gets a point!")
    elif user_c == 1 and comp_c == 3:
        print("User Wins!\nResult: +1 point for User!")
        u_score += 1
    elif user_c == 3 and comp_c == 1:
        print("Computer Wins!\nResult: +1 point for the Computer!")
        c_score += 1
    elif user_c > comp_c: 
        print("User Wins!\nResult: +1 point for User!")
        u_score += 1
    elif user_c < comp_c:
        print("Computer Wins!\nResult: +1 point for the Computer!")
        c_score += 1

def winner():
    global c_score
    global u_score
    global game_active
    
    

    #these were cut out due to the results being the same in accordance to the conditions
    # elif user_c == 2 and comp_c== 1:
    #     print("User Wins!")
    # elif user_c == 3 and comp_c == 2:
    #     print("User Wins!")
    # elif user_c == 1 and comp_c == 2:
    #     print("Computer Wins!")
    # elif user_c == 2 and comp_c == 3:
    #     print("Computer Wins!")
# user()
# roll()
# winner()

#starts the game and goes until either the user or the computer have won 5 games
def game():
    #calls global variable to check if game is still active
    global game_active
    global game_c
    
    while game is True:
        game_c += 1
        user()
        comp()
        game_logic()
        winner()
    
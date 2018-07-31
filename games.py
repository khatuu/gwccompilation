#TODO: import the random module since you  will need it in your game functions
import random

#TODO: define function guess_the_num

def guess_the_num() :
    numb = random.randint(1,100)
    guess = input("(Guess a number between 1 to 100!)")
    tries = 0
    for tries in range (0,6):
        if int(guess) < numb:
            guess = int(input('guess higher:'))
        elif int(guess) > numb:
            guess = int(input('guess lower:'))
        else:
            continue
    print('the number is {}!'.format(numb))


#TODO: define function rock_paper_scissors
import random

def rps() :
# TODO: Create a list of possible moves in rock paper scissors
    gestures = ["rock", "paper", "scissors"]
    # Allow the computer to make a random selection on the move
    computer = random.choice(gestures)

    # TODO: Take in user input for rock, paper, or scissors
    move = input("(Choose rock, paper, scissors!)")
    # BE SURE TO PROCESS INPUT (valid inputs allowed ONLY)
    # TODO

    # Show the human player what the computer decided on
    print("I chose {}!".format(computer.upper()))

    # Determine who wins
    # TODO: when would there be a tie?
    if move == computer :
        print("It's a tie!")
    elif move == "rock" and computer == "scissors" :
        print ("You won!")
    elif move == "scissors" and computer == "paper" :
        print ("You won!")
    elif move == "paper" and computer == "rock" :
        print ("You won!")
    elif move == "rock" and computer == "paper" :
        print ("Sorry, you lost!")
    elif move == "paper" and computer == "scissors" :
        print ("Sorry, you lost!")
    elif move == "scissors" and computer == "rock" :
        print ("Sorry, you lost!")
    else :
        print ("Your invalid input made me die :(, please try again!)")

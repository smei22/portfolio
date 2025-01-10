# In this programming assignment,
# you will create a simple Python program
# that allows the player to play the classic
# game of "Rock-Paper-Scissors" against the computer.
# The game involves selecting either rock, paper, or scissors
# and comparing the choices to determine the winner.
# The program should also keep track of the score
# and give the player the option to play again.

# Sharon Mei
# ROCK PAPER SCISSORS GAME
import random


def game():

    print("Welcome to Rock, Paper, Scissors!")
    print("""
Rules:
- Rock Beats Scissors
- Scissors Beats Paper
- Paper Beats Rock""")
    playerscore = 0
    computerscore = 0


    while True:
        choice = random.randint(1,3)
        player = int(input("Choose: Rock(1), Paper(2), Scissors(3), or Quit(4) "))

        if player == 1:
            player = "rock"
        elif player == 2:
            player = "paper"
        elif player == 3:
            player = "scissor"
        elif player == 4:
            break


        if choice == 1:
            choice = "rock"
        elif choice == 2:
            choice = "paper"
        elif choice == 3:
            choice = "scissor"


        print("""
    """ + "The Computer chose " + choice)
        print("""
    """ + "The Player chose " + player)



        if player == choice:
            print("""
    It's A Tie!
    --------------------""")
            print("""
""" + str(playerscore) + ":" + str(computerscore))


        elif player == "rock" and choice == "scissor":
            print("""
    Player Wins
    --------------------""")
            playerscore = playerscore + 1
            print("""
""" + str(playerscore) + ":" + str(computerscore))


        elif player == "paper" and choice == "rock":
            print("""
    Player Wins
    --------------------""")
            playerscore = playerscore + 1
            print("""
""" + str(playerscore) + ":" + str(computerscore))


        elif player == "scissor" and choice == "paper":
            print("""
    Player Wins
    --------------------""")
            playerscore = playerscore + 1
            print("""
""" + str(playerscore) + ":" + str(computerscore))

        else:
            print("""
    Player Loses
    --------------------""")
            computerscore = computerscore + 1
            print("""
""" + str(playerscore) + ":" + str(computerscore))





game()




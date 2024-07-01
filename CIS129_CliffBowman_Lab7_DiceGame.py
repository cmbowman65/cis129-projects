"""

Module 7 Lab - Dice Game
Cliff Bowman
27 Jun 2024

This program determines the winner between two players as the one who rolls a higher
number on a 6-sided die. If the players roll the same number, a tie is declared.

The players may continue playing or the program will end.

"""
# import needed library
import random

# Main Function
def main():
    
    # initialize variables
    endProgram = 'no'     #sets while loop condition
    playerOne = ""        #sets player one's name to null
    playerTwo = ""        #sets player two's name to null
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    while endProgram == 'no':
        
        # initialize variables for while loop
        p1number = 0      #sets player one die roll to zero
        p2number = 0      #sets player two die roll to zero
        winnerName = ""   #sets winner's name to null
        
        winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName)
        
        displayinfo(winnerName)
        endProgram = input("Do you want to end program?(Enter yes or no):")

# Function Call for the name of the two players
def inputNames(playerOne, playertwo):
    playerOne= input('Enter player 1 name: ')
    playerTwo= input('Enter player 2 name: ')
    return playerOne, playerTwo

# Function Call to roll the dice and determine a winner or a tie
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)

    if p1number == p2number:
        winnerName = "TIE"

    elif p1number>p2number:
        winnerName=playerOne

    else:
        winnerName=playerTwo

    return winnerName

#Function Call to display the winner's name
def displayinfo(winnerName):
    print("The winner is", winnerName)


main()

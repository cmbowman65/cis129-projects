"""

Module 6 Lab
Cliff Bowman
22 Jun 2024

This program calculates the number of packages of hot dogs and the number of
packages of hot dog buns needed for a cookout with the minimum number of
leftovers for dogs and buns.

"""

# Initialize variables
totalHotDogs = 0

# Main function
def main():
    totalHotDogs = getTotalHotDogs()
    showResults(totalHotDogs)

# Determines the total number of hot dogs needed
def getTotalHotDogs():
    
    #Initialize variables
    attendees = 0
    hotDogs = 0
    
    # Gets input from user
    attendees = int(input('What is the maximum number of people attending the cookout? '))
    hotDogs = int(input('How many hot dogs per person? '))
    totnum_hotDogs = attendees * hotDogs   # total number of hot dogs cooked and given out
    
    return totnum_hotDogs    

# Determines the results
def showResults(total):
    
    # Initialize variables
    DOGS = 10     # number of hot dogs in each package
    BUNS = 8      # number of buns in each package
    dogsLeft = 0
    bunsLeft = 0
    minDogs = 0
    minBuns = 0

    #  Determines leftovers and number of packages of dogs and buns neeeded
    dogsLeft = (DOGS - total % DOGS) % DOGS
    minDogs = (total // DOGS) + (0 ** (0 ** dogsLeft))
    bunsLeft = (BUNS - total % BUNS) % BUNS 
    minBuns = (total // BUNS) + (0 ** (0 ** bunsLeft))

    # Displays results
    print('\nMinimum packages of hot dogs needed:', minDogs)
    print('Minimum packages of hot dog buns needed:', minBuns)
    print('Hot dogs remaining:', dogsLeft)
    print('Hot dog buns remaining:', bunsLeft)

main()

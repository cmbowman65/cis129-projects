# Module 5 Lab
# Cliff Bowman
# 19 Jun 2024
# This program determines weekly bottles collected and payout
# Practice Repition Structures

# Initialize variables
totalBottles = 0
totalPayout = 0
keepGoing = "y"

# Sets condition to enter weekly totals
while keepGoing == "y":
    totalBottles = 0  
    totalPayout = 0   
    print('')
 
    # processes a week of bottle collection      
    for counter in range(7):
        print('Enter number of bottles for day',counter + 1,': ', end='')
        todayBottles = int(input())
        totalBottles = todayBottles + totalBottles
    
    totalPayout = totalBottles * 0.1
    
    # detail totals for the week
    print('The total number of bottles collected is', totalBottles)
    print(f'the total paid out is ${totalPayout:.2f}')
    
    # Question to process another week or end program    
    keepGoing = input("Do you want to enter another week’s worth of data? (y or n)")
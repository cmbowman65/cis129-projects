"""

Module 11 Lab - Exercise 9.3 - Store names and grades in a csv file
Cliff Bowman
CIS-129
19 Jul 2024

This program has a user input an unlimited number of students and grades  
and stores them in a csv file named grades.csv.

"""

import csv


def main():
    
    # creates and opens csv file
    with open('grades.csv', 'w', newline='') as grades:
        writer = csv.writer(grades)
       
        # loop to collect data until sentinel entered
        while True:
            firstname = input("Student's first name or 'end' if complete: ")
            
            # check for letters only in firstname
            while firstname.isalpha() == False:
                firstname = input("Only letters please.  Student's first name or 'end' if complete: ")
            
            # check for sentinel to end the program
            if firstname.lower() == 'end':
                break
            
            # store first name with first letter in caps
            firstname = firstname.capitalize()
            
            lastname = input("Student's last name: ")
            
            # check for only letters in lastname
            while lastname.isalpha() == False:
                lastname = input("Only letters please.  Student's last name: ")
            
            # store last name with first letter in caps
            lastname = lastname.capitalize()
          
            # enter exam grades and call functions to check for valid integers
            exam1grade = goodGrade("First exam grade: ")
            exam2grade = goodGrade("Second exam grade: ")
            exam3grade = goodGrade("Third exam grade: ")

            # write data to the csv file
            writer.writerow([firstname, lastname, exam1grade, exam2grade, exam3grade])
            
            print()

# Ensures valid user input for exam grades of a positive integer or zero
def goodGrade(user_input):
    good_input = validNumber(user_input)
    while good_input < 0 or good_input > 100:
        print('Enter a integer between zero and 100 for a grade. Try again.')
        good_input = validNumber(user_input)
    return good_input

# Validates exam input as not a float or not a string that can be further validated in goodGrade function
def validNumber(user_input):
    while True:
        try:
            num = int(input(user_input))
            return num
        except ValueError:
            print('Enter a number greater than or equal to 0. No letters or decimals allowed. Please try again.')  

main()


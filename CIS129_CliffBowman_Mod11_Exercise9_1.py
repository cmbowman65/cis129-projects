"""

Module 11 Lab - Exercise 9.1 - Store grades in a text file
Cliff Bowman
CIS-129
18 Jul 2024

This program has a user input an unlimited number of grades until the sentinel is 
entered and stores them in a text file named grades.txt.

"""
def main():
    # main function to write grades to txt file
    with open('grades.txt', mode='w') as grades:
        # input first grade
        grade = goodGrade('Enter a grade, -1 to end: ')  
        
        # write to txt file and enter more grades 
        while grade != -1:
            grades.write(str(grade) + '\n')
            grade = int(input('Enter a grade, -1 to end: '))    
        
# Ensures valid user input of a positive integer or 0
def goodGrade(user_input):
    good_input = validNumber(user_input)
    while good_input < 0 and good_input != -1:
        print('\nEnter a positive integer or zero for a grade. Try again.\n')
        good_input = validNumber(user_input)
    return good_input

# Validates user input as not a float or not a string that can be further validated in goodGrade function
def validNumber(user_input):
    while True:
        try:
            num = int(input(user_input))
            return num
        except ValueError:
            print('Enter a number greater than or equal to 0. No letters or decimals allowed. Please try again.\n')  

# calls main function            
main()            
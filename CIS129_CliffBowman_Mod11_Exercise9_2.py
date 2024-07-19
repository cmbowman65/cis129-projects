"""

Module 11 Lab - Exercise 9.2
Cliff Bowman
CIS-129
18 Jul 2024

This program reads the grades.txt file and displays the sum of the grades,
the number of grades, and the average.

"""

with open('grades.txt', mode='r') as grades:
    # initialize variables
    sumTotal = 0
    num = 0
    
    for grade in grades:
        sumTotal += int(grade)
        num += 1
    
    # display sum, number of grades, and average    
    print(f'Sum of all the grades: {sumTotal}')
    print(f'Number of grades: {num}')
    print(f'Average grade: {sumTotal / num:.1f}')
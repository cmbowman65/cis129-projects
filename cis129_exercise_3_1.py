# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 12:26:19 2024

@author: CMB-Acer
"""
# fig03_03.py
"""Using nested control statements to analyze examination results."""

# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures

# process 10 students
for student in range(5):
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
    
    while (result != 1 and result != 2):
        result = int(input('Enter a correct result (1=pass, 2=fail):  '))

    if result == 1:
        passes = passes + 1
    else: 
        failures = failures + 1


# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')

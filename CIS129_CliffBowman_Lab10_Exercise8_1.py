"""

Module 10 Lab - Exercise 8.1 - Check printing with check-protected format
Cliff Bowman
CIS-129
11 Jul 2024

This program prints a check in check-protected format.

"""

# Main Function
def main():
    
    checkAmount = amount('Enter a check amount less than 1000000.00: ') 

    print('\nThe check-protected dollar amount is:')
    print(f'\n{checkAmount:*>10,.2f}')

# Ensures valid user input between zero and 1000000
def amount(user_input):
    good_input = validNumber(user_input)
    while good_input <= 0 or good_input >= 1000000:
        print('\nDollar amount must be greater than zero and less than 1000000.  Try again.\n')
        good_input = validNumber(user_input)
    return good_input

# Validates user input as a float that can be further validated in checkAmount function
def validNumber(user_input):
    while True:
        try:
            num = float(input(user_input))
            return num
        except ValueError:
            print('\nPlease try again using numbers.')

# Call Main
main()


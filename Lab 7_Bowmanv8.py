"""
Lab 7

Cliff Bowman
CIS188 - 21623
26 Mar 25

Lab 7 - Strong Password Detection

This program takes a password and determines if it meets minimum requirements. 
  
"""

import re

print("""You are to provide a password that meets ALL of the following requirements:
- At least 10 characters long
- Must contain at least one uppercase and one lowercase letter
- Must contain at least one number
- Must contain at least one of these special characters: @$_
- Cannot contain the user's name (case insensitive)
- Cannot contain the following words: dog, cat, rat (case insensitive)
""")

user_name = input("Hello.  Please enter your name:\n")

# Strong Password Regexes

length_regex = re.compile(r'.{10,}')           # >= 10 characters
upper_regex = re.compile(r'[A-Z]')             # Contains an upper case letter
lower_regex = re.compile(r'[a-z]')             # Contains a lower case letter
number_regex = re.compile(r'[0-9]')            # Contains a number
special_regex = re.compile(r'[@]|[$]|[_]')     # contains @, $, or _
name_regex = re.compile(rf"{user_name}", re.I) # contains user name in the password
common_regex = re.compile(r'dog|cat|rat', re.I)

def main():

    while True:
        
        user_password = input("Input a password:\n")
        print("")

        # Run it through the function and print relevant messages to the user
        if password_check(user_password) == True:
            print("Good job - strong password!  All requirements met.")
            break
        else:
            print("\nYour password doesn't meet the minimum requirements.\n")

            # Ask user if they desire to process another quote/lyric
            once_more = input("Would you like to try another password? (yes/no)\n")
            if once_more.lower() != "yes":
                break

def password_check(password):
    # Check if password meets all the requirements
    counter = 0
    if length_regex.search(password) == None:
        print("Your password has less than 10 characters")
        counter = 1
    if upper_regex.search(password) == None:
        print("Your password doesn't have an uppercase letter")
        counter = 1
    if lower_regex.search(password) == None:
        print("Your password doesn't have an lowercase letter")
        counter = 1
    if number_regex.search(password) == None:
        print("Your password doesn't have a number")
        counter = 1
    if special_regex.search(password) == None:
        print("Your password doesn't have one of the required special characters")
        counter = 1
    if name_regex.search(password) != None:
        print("Your password should NOT contain your name")
        counter = 1
    if common_regex.search(password) != None:
        print("Your password contains a common word")
        counter = 1    
        
    if counter == 1:
        return False
    else:
        return True

main()



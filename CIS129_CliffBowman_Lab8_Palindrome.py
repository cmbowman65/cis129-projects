"""

Module 8 Lab - Palindrome Tester
Cliff Bowman
30 Jun 2024

This program tests whether a string is a palindrome not testing for case, spaces, 
or punctuation.

"""

def is_palindrome(string):
    pal_stack = []
    
    # builds the stack
    for character in string:
        pal_stack.append(character)
        
    # loop to check string characters with their popped counterparts
    # e.g. first string character with the first popped character, then second string
    # character with second popped character, etc
    
    for character in string:
        popped_character = pal_stack.pop()
        
        # compares stack and pop characters in lower case and if the characters do not match 
        # ends loop and returns false
        if character.lower() != popped_character.lower():
            return False   # is NOT a palindrome
    
    return True  # is a palindrome

# Ask the user to input a word or phrase to check for palindrome.
user_input = input('Enter a phrase to determine if it is a palindrome: ')

# Call the is_palindrome function and display the result.
if is_palindrome(user_input):
 print('Yes, it is a palindrome.')
else:
 print('No, it is not a palindrome.')

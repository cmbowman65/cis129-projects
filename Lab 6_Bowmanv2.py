"""
Lab 6

Cliff Bowman
CIS188 - 21623
19 Mar 25

Lab 6 - String Processing Program

This program has a user input their favorite quote or lyrics.  The program then passes
the string to a group of functions that executes and outputs the following:
    
- Determine and return the number of characters in the given string, not including spaces.
- Determine and return what character is in the 6th position of the given string
- Return the given string in all uppercase.
- Determine and return the last word in the given string, repeated a random number of times.
- Create and return a dictionary that contains key pair values where each word in the given 
  string is the key and the count of how often that word appears is the value.
- Generate and return a 20-character slice of the given string using a random number to 
  determine what index the slice starts at. 
  
"""

import random

def main():
    print("Welcome to the String Processing Program!")

    while True:
        user_input = input("\nPlease enter your favorite quote or lyrics:\n")

        # Ensure user makes an input
        if not user_input.strip():
            print("You did not enter a quote or lyric. Please try again.")
            continue

        # Variables assigned the calls of the required functions/tasks
        total_char = num_characters(user_input)
        sixth = sixth_position(user_input)
        yelling = all_caps(user_input)
        repeat = last_word_random_repeat(user_input)
        word_dictionary = quote_words_total(user_input)
        poetry_slice = twenty_char_slice(user_input)

        # Outputs of the results of the functions executed on the user inputed string 
        print(f"\nBased on our processing, your favorite quote contains {total_char} characters, not including spaces!")
        
        if sixth:
            print(f"\nThe character in the 6th position is: {sixth}")
        else:
            print("\nThe string is too short to have a 6th character.")
        
        print("\nHere is the quote read by someone yelling:\n")
        print(f"{yelling}\n")
        
        print(f"{repeat}\n")
        
        print("Here are all the words in your quote and how often they appear:\n")
        print("WORD COUNT".center(26, "-"))
        for k, v in word_dictionary.items():
            kspace = k + " "
            print(kspace.ljust(23, ".") + str(v).rjust(3))
            
        if poetry_slice:
            print("\nHere is a slice of your quote, randomly selected for poetic effect:\n")
            print(f"{poetry_slice}\n")
        else:
            print("\nYour quote is too short to make poetry!\n")

        # Ask user if they desire to process another quote/lyric
        once_more = input("That's all the processing we have for you today! Do you want to do that again? (yes/no)\n")
        if once_more.lower() != 'yes':
            break

    print("Thanks for sharing your favorite quote!")

def num_characters(string):
    # Returns the number of characters, not including spaces, in the quote/lyric
    return len(string.replace(" ", ""))

def sixth_position(string):
    # Returns the character in the sixth position of the quote/lyric
    if len(string) > 5: 
        return string[5] 
    else:
        None

def all_caps(string):
    # Returns the quote/lyric in all caps
    return string.upper()

def last_word_random_repeat(string):
    # Returns the last word in the quote/lyric repeated a random number of times (up to 16)
    words = string.split()
    if not words:
        return ""
    last_word = words[-1]
    num = random.randint(1, 16)
    return "  ".join([last_word for _ in range(num)])

def quote_words_total(string):
    # Returns a dictionary with the words in the quote/lyric and how often they appear
    words = string.split()
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

def twenty_char_slice(string):
    # Returns a random 20-character slice of the quote/lyric (if input >= 20 characters)
    if len(string) >= 20:
        count = len(string) - 20
        num = random.randint(0, count)
        return string[num:(num + 20)] 
    else:
        None

# Run the main function
main()

"""
CIS188, Lab 8 - Sandwich Maker

This program asks users to choose various items for their sandwich (such as bread, 
protein, cheese, and condiments), how many sandwiches they would like, and gives 
them a reciept with their order and total price for the sandwiches.

Author:  Cliff Bowman

Date:  4 Apr 2025

"""

import pyinputplus as pyip

# Nested dictionaary of prices for all the sandwich options
prices = {
    'bread': {'Wheat': 1.50, 'White': 1.50, 'Sourdough': 1.85},
    'protein': {'Chicken': 3.00, 'Turkey': 3.00, 'Ham': 2.85, 'Tofu': 3.25},
    'cheese': {'Cheddar': 0.35, 'Swiss': 0.50, 'Mozzarella': 0.60},
    'condiments': {'mayo': 0.25, 'mustard': 0.25, 'lettuce': 0.30, 'tomato': 0.50}
}


def make_sandwich():    
    """ 
    Gets user input for sandwich makings
    
    Action: user input using PyInputPlus functions
    
    Input:  none
    
    Output: PyInputPlus message and reprompt if invalid input

    Return: values for bread, protein, cheese, number of sandwiches; list for condiments
    """
    
    # Choosing bread and protein types using inputMenu()
    bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], prompt='Choose your bread type:\n')
    protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], prompt='Choose your protein type:\n')

    # Ask if user wants cheese using inputYesNo() then choosing type
    cheese = pyip.inputYesNo('Would you like cheese? (yes or no)\n')
    if cheese == 'yes':
        cheese = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], prompt='Choose your cheese type:\n')
    else:
        cheese = None

    # Ask if user wants condiments using inputYesNo() for each and creating a condiments list
    condiments = []
    for condiment in ['mayo', 'mustard', 'lettuce', 'tomato']:
        if pyip.inputYesNo(f'Do you want {condiment}? (yes or no)\n') == 'yes':
            condiments.append(condiment)

    # User input for number of sandwiches using inputInt(), minimum of 1
    num_sandwiches = pyip.inputInt('How many sandwiches would you like to order?\n', min=1)

    return bread, protein, cheese, condiments, num_sandwiches


def bill_total(bread, protein, cheese, condiments, num_sandwiches):    
    """ 
    Calculates the total cost of the order

    Action: computes the total cost of the sandwich and order total

    Input:  bread, protein, cheese, condiments, number of sandwiches

    Output: none

    Return: total cost of the bill
    """
        
    # bread and protein cost
    sandwich_cost = prices['bread'][bread] + prices['protein'][protein]

    # add cheese cost
    if cheese:
        sandwich_cost += prices['cheese'][cheese]

    # add condiment cost
    for condiment in condiments:
        sandwich_cost += prices['condiments'][condiment]

    # total bill
    return sandwich_cost * num_sandwiches


def main():
    """ 
    Main function
    
    Action: Welcomes the user, calls the program's other functions, outputs info
    
    Input:  none
    
    Output: Welcome.  Order and Receipt - bread, protein, cheese, condiments, number of 
            sandwiches, and the total cost of the bill. Output the sandwich order in a 
            restaurant style receipt - general items left justified, choices right 
            justified, dots between, total cost at bottom. 
    
    Return: none
    """   
    
    print("Welcome to the Sandwich Maker program.  Let's make some sandwiches!\n")
    
    # call first function
    bread, protein, cheese, condiments, num_sandwiches = make_sandwich()
    
    # call second function
    total_cost = bill_total(bread, protein, cheese, condiments, num_sandwiches)
    
    # output receipt
    print(('\n' * 2) + 'YOUR ORDER '.center(44, '*'))
    print('Bread '.ljust(43 - len(bread), '.') + f' {bread}'.rjust(len(bread)))
    print('Protein '.ljust(43 - len(protein), '.') + f' {protein}'.rjust(len(protein)))
    
    if cheese:
        print('Cheese '.ljust(43 - len(cheese), '.') + f' {cheese}'.rjust(len(cheese)))
    else:
        print('Cheese '.ljust(39, '.') + ' none'.rjust(5))
    
    if condiments:
        all_condiments = ', '.join(condiments)        
        # rjust + 1 to add space between items and dots
        print('Condiments '.ljust(43 - len(all_condiments), '.') + all_condiments.rjust(len(all_condiments) + 1))
    else:
        print('Condiments '.ljust(39, '.') + ' none'.rjust(5))
    
    print('Number of sandwiches '.ljust(43 - len(str(num_sandwiches)), '.') + f' {num_sandwiches}'.rjust(len(str(num_sandwiches))))
    print('=' * 44)
    print("")
    
    # consistent output of total cost to the hundreths place (i.e. include zero in hundreths)
    total_cost = "{:.2f}".format(total_cost)
    
    # Ljust of 42 to account for the dollar sign
    print('Total cost '.ljust(42 - len(str(total_cost)), '.') + f' ${total_cost}'.rjust(len(str(total_cost))))

    print('\n' + 'Thank you for your business!'.center (44))
    
# call main
main()

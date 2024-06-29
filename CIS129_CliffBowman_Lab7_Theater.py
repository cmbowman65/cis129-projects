"""

Module 7 Lab - Theater Revenue
Cliff Bowman
27 Jun 2024

This program requests the number of tickets sold in each of the theater's
three sections then determines the revenue of each section and total sales.

"""

# Constant variables for the cost of tickets and number of seats in each section
A_COST = 20
B_COST = 15
C_COST = 10

SEATS_IN_A = 300
SEATS_IN_B = 500
SEATS_IN_C = 200

# Initialize variable
total_rev = 0

# Main Function
def main():
    print('Welcome to the Theater Revenue Program')
    print(f'\nSection A: {SEATS_IN_A} seats at ${A_COST}')
    print(f'Section B: {SEATS_IN_B} seats at ${B_COST}')
    print(f'Section B: {SEATS_IN_C} seats at ${C_COST}')
    print()
    
    # Call to get valid number of tickets sold per section
    a_tickets = num_tickets('Number of tickets sold in section A: ', 0, SEATS_IN_A)
    b_tickets = num_tickets('Number of tickets sold in section B: ', 0, SEATS_IN_B)
    c_tickets = num_tickets('Number of ticket solds in section C: ', 0, SEATS_IN_C)
    print()
    
    # Call to get total revenue per section
    revenue_a = secRevenue(A_COST, a_tickets)
    revenue_b = secRevenue(B_COST, b_tickets)
    revenue_c = secRevenue(C_COST, c_tickets)
      
    # Call to display total revenue and tickets sold per section
    sectionTotal('A', revenue_a, a_tickets)
    sectionTotal('B', revenue_b, b_tickets)
    sectionTotal('C', revenue_c, c_tickets)
    
    # Total overall revenue
    total_rev = revenue_a + revenue_b + revenue_c
    
    # Display the overall total
    print(f'\nTotal revenue is ${total_rev}')   

             
# Ensures valid user input between zero and max seats in section (single function validation)
def num_tickets(user_input, low, full):
    good_input = validNumber(user_input)
    while good_input < low or good_input > full:
        print('Number of tickets must be between zero and max seats in section. Please try again.\n')
        good_input = validNumber(user_input)
    return good_input

# Validates user input as an integer that can be further validated in num_tickets function
def validNumber(user_input):
    while True:
        try:
            num = int(input(user_input))
            return num
        except ValueError:
            print('Enter a number greater than or equal to 0. No letters or decimals allowed. Please try again.\n')

# Calculates the total revenue for each section
def secRevenue(price, tickets):
    secTotal = price * tickets
    return secTotal

# Displays total revenue and tickets sold for each section
def sectionTotal(sectionLetter, revPerSection, tickets):
    print(f'Section {sectionLetter} revenue - ${revPerSection}: Tickets sold - {tickets}')
    
# Call Main
main()
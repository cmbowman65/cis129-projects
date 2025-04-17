"""
CIS188, Lab 10 - CSV Files and Password Generation

This program takes a provided CSV file, employee.csv, with a list of all employees in the 
company.  The list contains first name, last name, phone number and email for each person.  
The program creates a new CSV file which contains the first name, last name, email and a 
new randomly generated password.

Author:  Cliff Bowman

Date:  18 Apr 2025

"""
import csv, sys, random, string
from pathlib import Path


def gen_pass(length):
    """
    Generates a password
    
    Action: Generate a randomized password of size 'length' using all ascii letters, 
            numbers 0-9, and a subset of special characters
            
    Input: length of password
    
    Output:  None
    
    Returns: password
    """
    all_characters = string.ascii_letters + string.digits + '!@$%^&*-_+=~<>/\\(){}[]?|'
    password = "".join(random.sample(all_characters, length))
    return password


def main():    
    """ 
    Main function
    
    Action: Calls other functions, pauses program to allow user to confirm 'employee.csv' 
            exists in the working directory, quits program if it cannot find 'employees.csv',
            reads employees.csv, and writes first name, last name, email, and password
            to employees_password.csv
    
    Input:  none
    
    Output: Confirm 'employees.csv' found or 'quit' if 'employees.csv' cannot be found;
            Directory for 'employees_password.csv'
    
    Return: none
    """            
    print("Ensure 'employees.csv' has been downloaded/copied to the same directory as this program.")
    input("\nPress Enter to continue.")   
       
    # intializing
    current_dir = Path.cwd()
    employee_file = (current_dir / 'employees.csv')
    password_file = (current_dir / 'employees_password.csv')
    pass_length = 16
    
    # inform user file found or quitting program for lack of 'emplyees.csv'
    try:
        with open(employee_file, 'r') as input_file:
            print("File 'employees.csv' found.")
    except FileNotFoundError:
        print("\nThe file does not exist.")
        print("The program will quit for you to download 'employees.csv' to the program working folder.")
        sys.exit()

    # context manager to open/read or write/close employees.csv and employees_password.csv
    with open(employee_file, 'r', newline='') as input_file, open(password_file, 'w', newline='') as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)

        next(csv_reader)  # skips over the header row in employees.csv        

        # Write header row for the new 'employee_password.csv' file
        csv_writer.writerow(['first_name', 'last_name', 'email', 'password'])
     
        # Process each row after the header in the input file, employees.csv, and write to employees_password.csv
        for row in csv_reader:
            first_name = row[0]
            last_name = row[1]
            email = row[3]
            password = gen_pass(pass_length)
            csv_writer.writerow([first_name, last_name, email, password])

        print(f"\nSuccess! File {password_file} created.")
        
# Call main
main()
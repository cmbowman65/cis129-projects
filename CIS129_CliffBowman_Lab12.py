"""

Module 12 Lab
Cliff Bowman
CIS-129
25 Jul 2024

This program creates a class named "Pet"; creates an object of the class;
prompts a user to enter name, type, and age of a pet; and displays the data.

"""

def main():
    
    # Request input from user to get a pet's name, type, and age
    inputName = input("Enter your pet's name: ")
    inputType = input("Enter your pet's type: ")
    inputAge = goodNum("Enter your pet's age: ")
    
    # Make a new pet object from the Pet class
    petAnimal = Pet()
    
    # Set the details of the pet from user input
    petAnimal.set_name(inputName)
    petAnimal.set_type(inputType)
    petAnimal.set_age(inputAge)
    
    # Display the details about the pet
    print(f"\nThe pet name is: {petAnimal.get_name()}")
    print(f"The pet type is: {petAnimal.get_type()}")
    print(f"The pet age is: {petAnimal.get_age()}")

# Create a class named Pet
class Pet:
    
    # Initialize properties of a pet
    def __init__(self, name = '', type = '', age = 0):
        self.name = name # Name of the pet
        self.type = type # What type of animal 
        self.age = age # Age of the pet
        
    # Method for setting a pet's name
    def set_name(self, name):
        self.name = name
        
    # Method for setting the type of pet
    def set_type(self, type):
        self.type = type
        
    # Method for setting the age of a pet
    def set_age(self, age):
        self.age = age
        
    # Method to get a pet's name
    def get_name(self):
        return self.name
    
    # Method to get a pet's type
    def get_type(self):
        return self.type
    
    # Method to get the pet's age
    def get_age(self):
        return self.age


# Ensure valid user input for pet age as a positive integer or zero
def goodNum(user_input):
    good_input = validNumber(user_input)
    while good_input < 0:
        print('Enter an integer greater than or equal to zero.')
        good_input = validNumber(user_input)
    return good_input

# Validate pet's age as not a float or not a string that can be further validated in goodNum function
def validNumber(user_input):
    while True:
        try:
            num = int(input(user_input))
            return num
        except ValueError:
            print('Enter a number geather than or equal to zero. No letters or decimals allowed.')
            
# Call main function
main()
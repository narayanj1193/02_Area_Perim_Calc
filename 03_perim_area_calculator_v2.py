# functions always go at the start

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:
        error = "Please enter a number above zero"
        
        try:    
            
            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response  

            # outputs error if input is invalid
            else:
                print(error)
                print()
        
        except ValueError:
            print(error)

# Main routine goes here

# Introduction
print("**** Area and Perimeter Calculator! ****")

# Looping for the calculator.
keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculations for area and perimeter
    area = width * height
    perimeter = 2 * (width + height) 

    # Output the area and perimeter to 2 decimal places. 
    # Use the code ":.xf" where "x" is the number of decimal points you require
    print()
    print("The area of your shape is {:.2f} square units". format(area))
    print("The perimeter of your shape is {:.2f}". format(perimeter))
    print()

    keep_going = input("Press <enter> to keep going or press any other key to quit.")

# Concluding output. 
print()
print("Thanks for using the area / perimeter calculator")
print()
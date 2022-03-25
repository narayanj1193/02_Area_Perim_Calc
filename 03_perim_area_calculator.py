# functions always go at the start

# checks input is a number more than zero


from turtle import width


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

# main routine goes here
width = num_check("Width: ")
height = num_check("Height: ")

# calculations for area and perimeter
area = width * height
perimeter = 2 * (width + height) 

print()
print("The area of your shape is {} square units". format(area))
print("The perimeter of your shape is {}". format(perimeter))
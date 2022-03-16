# checks that users enter a number above zero
valid = False
while not valid:

    try:    
        error = "Please enter a number above zero"
        # ask user to enter a number
        response = float(input("Enter a number: "))

        # checks number is more than zero
        if response > 0:
            valid = True    

        # outputs error if input is invalid
        else:
            print(error)
            print()
    
    except ValueError:
        print(error)
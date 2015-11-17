##!/usr/bin/python
# Filename: p1.py

##### ADD YOUR NAME, Student ID, and Section number #######
# NAME:
# STUDENT ID:
# SECTION: 
###########################################################

###########  ADD YOUR CODE HERE ###############################
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def convert_miles_to_kilometers():
    miles = raw_input("Enter the miles to be converted: ")
    if is_float(miles):
        #convert miles string to numeric miles
        miles = float(miles)
        # now apply conversion km = miles * 0.62137
        km =  miles * 0.62137
        print "{the_miles} are equivalent to {the_km} kilometers".format(the_miles = miles, the_km=km)
    else:
        print "Illegal unit of conversion. Input miles are not a number."

################################################################

def print_program_menu():
    print "\n"
    print "Welcome to unit conversion program. Please, choose an option:"
    print "1. Miles to kilometers"
    print "2. Kilometers to miles"
    print "3. Pounds to kilograms "
    print "4. Kilograms to pounds"
    print "5. Celsius to Fahrenheit"
    print "6. Fahrenheit to Celsius"
    print "7. Miles/hour to kilometers/hour"
    print "8. Kilometers/hour to Miles/hour"
    print "9. Exit"

def identify_option(option):
    if option.isdigit() :  # Verify if this is a number
        numeric_option = int(option)
        # check if in range
        if numeric_option >= 1 and numeric_option <= 9:
            return (0, numeric_option)
        else:
            return (-1, 0) # invalid option
    else:
        return (-1, 0) # invalid option

def process_conversion(numeric_option):
    if (numeric_option == 1):
        convert_miles_to_kilometers()

def main():
    done = False
    while not done:
        print_program_menu()
        user_option = raw_input("Enter option: ")
        option_info_tuple = identify_option(user_option)
        if option_info_tuple[0] == 0:
            #option was valid
            if option_info_tuple[1] == 9:
                done = True
                print "Thanks for using the unit conversion program"
            else:
                process_conversion(option_info_tuple[1])
        else:
            #option invalid
            print "Invalid Option\n"

# This line makes python start the program from the main function
if __name__ == "__main__":
    main()


__author__ = 'manuel'



def print_program_menu():
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



def main_program():
    done = False
    while not done:
        print_program_menu()
        user_option = raw_input("Enter option: ")
        option_info_tuple = identify_option(user_option)
        if option_info_tuple[0] == 0:
            #option was valid
            if option_info_tuple[1] == 9:
                done = True
            else:
                process_conversion(option_info_tuple[1])
        else:
            #option invalid
            print "Invalid Option"




'''
Validate user input
Name
Email
Contact number
'''
completed = False
details = ["All", "Name", "Email", "Contact Number"]

while not completed:
    correct = False
    # Checks if name is valid with alphabetical letters only,
    # whtespace or hyphen
    while True:
        name = input("Please enter your full name: ").title()
        if name.isalpha() or "-" in name or " " in name:
            print("Name stored")
            break
        else:
            print("Invalid character entered.")

    # Checks if an '@' and '.' are included in the email
    while True:
        email = input("\nPlease enter you email address: ").lower()
        if "@" in email and "." in email:
            print("Email stored")
            break
        else:
            print("Please enter a valid email")

    # Checks if input can be converted to an integer, if not, custom
    # message is displayed letting the user know what happened
    while True:
        try:
            contact_number = input('''\nPlease enter your primary \
contact number: ''')
            contact_number = int(contact_number)
            print("Contact number stored")
            contact_number = str(contact_number)
            break
        except ValueError:
            print("Incorrect contact number entered")
    while not correct:
        print("\nPlease check the details entered are correct")
        print(f"{name}\n{email}\n{contact_number}")
        print("-"*60)
        details_correct = input('''Please enter 'y' for yes or 'n' for \
no: ''').lower()
        if details_correct == "y":
            print("\nThank you, your details have been stored.")
            completed = True
            break
        elif details_correct == "n":
            print("\n")
            for i, option in enumerate(details):
                print(i, option)
            option_change = False
            while not option_change:
                while True:
                    try:
                        change_details = input('''Please enter the \
number of the option you would like to change: ''')
                        change_details = int(change_details)
                        break
                    except ValueError:
                        print("Please enter a number only")
                if change_details == 0:
                    option_change = True
                    correct = True
                    break
                elif change_details == 1:
                    while True:
                        name = input("Please enter your name: ").title()
                        if name.isalpha() or "-" in name or " " in name:
                            print("Name stored")
                            option_change = True
                            break
                        else:
                            print("Invalid character entered.")                     
                elif change_details == 2:
                    while True:
                        email = input("Please enter you email address: ").lower()
                        if "@" in email and "." in email:
                            print("Email stored")
                            option_change = True
                            break
                        else:
                            print("Please enter a valid email")
                elif change_details == 3:
                    while True:
                        try:
                            contact_number = input("Please enter your primary contact number: ")
                            contact_number = int(contact_number)
                            print("Contact number stored")
                            contact_number = str(contact_number)
                            option_change = True
                            break
                        except ValueError:
                            print("Incorrect contact number entered")
        else:
            print("\nPlease enter a valid option")
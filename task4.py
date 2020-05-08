import os
import datetime
import string
import random

# When the app is executed
# Set a running state for it
running_state = True

while running_state:

    invalid_input = True
    while invalid_input:
        try:
            user_command = int(input("""
    Type in 1 or 2 to perform any of the below
(1) Staff Login
(2) Close App
            """))
        except ValueError:
            print("Type in only 1 or 2")
            invalid_input = True

            # open the file for staff's credentials
        staff_credentials = open("staff.txt", "r").readlines()
        first_user = staff_credentials[0].split(",")[0]
        first_user_password = staff_credentials[0].split(",")[1]
        second_user = staff_credentials[1].split(",")[0]
        second_user_password = staff_credentials[1].split(",")[1]

        if user_command == 1:  # Staff Login
            username = input("Type in your username: ")
            password = input("Type in your password: ")

            # keep prompting for the username and password, until user enters a correct credential
            # check in side staff.txt for the staff login credential
            while (username != first_user and password != first_user_password) \
                    and (username != second_user and password != second_user_password):
                print("Username or password is incorrect, try again")
                username = input("Type in your username: ")
                password = input("Type in your password: ")

            # once correct username and password are inserted or typed in.
            # create user's session file
            logged_in_time = datetime.datetime.now()
            user_session = open("user_session_log.txt", "a")
            user_session.write(username + "\nLogged in at " + str(logged_in_time) + "\n\n\n")
            user_session.close()

            # Set user's logged in status
            logged_in_status = True
            while logged_in_status:
                # Ask user for which operation, he or she wishes to perform
                try:
                    user_operation_code = int(input("""
        What do you want to do?
        Type in:\n
    (1) to Create a New Bank Account
    (2) to Check Account Details
    (3) to Logout
                    """))
                except ValueError:
                    print("Only number 1 or 2 or 3 is allowed.")
                    logged_in_status = True

                # check for the inserted code
                if user_operation_code == 1:  # Create a bank account
                    account_name = input("Account Name: ")
                    opening_bal = input("Opening Balance: ")
                    account_type = input("Account Type: ")
                    account_email = input("Account Email: ")
                    account_number = ""
                    for allnum in random.choices(string.digits, k=10):
                        account_number += "".join(allnum)

                    # take all the above 5 data and save them inside
                    # the customer.txt file or user data house
                    with open("customer.txt", "a") as customer_data:
                        save_customer_data = customer_data.write("Account Number: " + account_number + "\n" + \
                                                                 "Account Name: " + account_name + "\n" + \
                                                                 "Account Balance: NGN " + opening_bal + "\n" + \
                                                                 "Account Type: " + account_type + "\n" + \
                                                                 "Account Owner Email: " + account_email + "\n\n\n")

                    # display the generated account number to the user
                    print(
                        "\n\nAccount created successfully.\nAccount Number for the just created user is: " + account_number)

                    logged_in_time = datetime.datetime.now()
                    user_session = open("user_session_log.txt", "a")
                    user_session.write(username + "\nCreated new account: (" + account_number + ") at " + str(
                        logged_in_time) + "\n\n\n")
                    user_session.close()

                    logged_in_status = True

                elif user_operation_code == 2:  # Search for a bank account
                    # collect and store the account number to be searched for
                    account_number = input("Please, type in the Account Number: ")

                    # connect to the customer data house to fetch data and close it.
                    customer_data_house = open("customer.txt", "r")
                    customer_data = customer_data_house.read()
                    customer_data_house.close()

                    # check if the given account number exists in the data house
                    # and if yes, fetch the user detail.
                    if account_number in customer_data:
                        with open("customer.txt", "r") as customers_data_house:
                            customers_data_house = customers_data_house.read()
                            searched_account_index_start = customers_data_house.find(
                                "Account Number: " + account_number)
                            searched_account_index_end = customers_data_house.find("\n\n", searched_account_index_start)
                            searched_account_detail = customers_data_house[
                                                      searched_account_index_start:searched_account_index_end]
                            print("\n\n" + searched_account_detail)

                        logged_in_time = datetime.datetime.now()
                        user_session = open("user_session_log.txt", "a")
                        user_session.write(
                            username + "\nSearched for user details of account  (" + account_number + ") at " + str(
                                logged_in_time) + "\n\n\n")
                        user_session.close()

                    else:
                        print("The typed in account does not exist\nPlease, enter a valid Account number")
                        logged_in_time = datetime.datetime.now()
                        user_session = open("user_session_log.txt", "a")
                        user_session.write(
                            username + "\nTyped in invalid account number - " + account_number + " at " + str(
                                logged_in_time) + "\n\n\n")
                        user_session.close()

                    logged_in_status = True

                elif user_operation_code == 3:  # Logout
                    user_session.close()
                    os.remove("user_session_log.txt")
                    logged_in_status = False
                    invalid_input = True
                else:
                    print("""
        Type in:
    (1) to Create a New Bank Account
    (2) to Check Account Details
    (3) to Logout
                    """)

                    logged_in_status = True




        # Close this App
        elif user_command == 2:
            invalid_input = False
            running_state = False
            break

        else:
            print("Only number 1 or 2 is allowed, try again please...")
            invalid_input = True

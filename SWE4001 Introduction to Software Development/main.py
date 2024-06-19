
import csv  # Importing the CSV module for the purpose of managing CSV files in a program.

# Utilizing the import statement to include functions from another file for use in the current program.
from clerks import new_orders,undelivered_orders 
from menus import manager_menu,delivery_menu,clerk_menu
from manager import total_orders_per_customer,total_daily_orders,total_delivered_orders,total_income_per_customer,\
total_daily_income, extracting_names, extract_order_each_cleck, extract_all_orders
from main_fuctions import login,is_valid
from delivery import CompleteDelivery



print("Greetings, I hope you are doing well. How has your day been thus far?") # Extending a cordial welcome as you enter the main section.


# We have set a limit on the maximum number of attempts for logging in.
login_attempts=0
max_attempts=3


# Requesting user input and verifying the number of attempts made.
while login_attempts < max_attempts:
    username=str.lower(input("Enter username: "))
    password=str.lower(input("Enter password: "))
    login_attempts += 1
    if login_attempts == 3:
        # Presenting the appropriate message to the user in a formal manner
        print("I apologize, but it seems that you have reached the maximum attempts allowed.\nPlease try again later. Thank you for your understanding.") 


    

    if is_valid(username,password): # Checking if username/password exists
        role=login(username, password) # Executing the login
        if role:
            choice='0' 
            while True:
                if role == 'manager': # Manager's role
                    choice=manager_menu()
                    print()
                    if choice == '1': # Choice 1 - Total Orders/Customer
                        total_orders_per_customer()
                        print() 
                    if choice == '2': # Choice 2 Total Daily Orders
                        total_daily_orders()
                        print()
                    if choice == '3': # Choice 3 Total Finished Orders
                        total_delivered_orders()
                        print()
                    if choice == '4': # Choice 4 Total Income/Customer
                        total_income_per_customer()
                        print()
                    if choice == '5': # Choice 5 Total Daily Income
                        total_daily_income()
                        print()
                    if choice == '6': # Choice 6 Extracting names in a list (.txt file)
                        extracting_names()
                        print()
                    if choice == '7': # Choice 7 Extracting orders of each Clerk by their name
                        extract_order_each_cleck()
                        print()
                    if choice == '8': # Choice 8
                        extract_all_orders()
                        print()
                    if choice == '0': # Choice 0(Exiting the program)
                        print("Concluding the program respectfully.")
                        break
                if role == 'clerk': # Clerk's role
                    choice = clerk_menu()
                    if choice == '1': # Choice 1  Adding new in a queue order
                        new_orders()
                    if choice == '2': # Choice 2  Displaying Incomplete Orders
                        undelivered_orders()
                    if choice == '0':
                        print("Concluding the program respectfully.") # Displaying proper message
                        break
                if role == 'delivery': # Delivery's role
                    choice = delivery_menu()
                    if choice == '1': # Choice 1 Update status of a specific order
                        CompleteDelivery()
                    elif choice == '2': # Choice 2 See undelivered orders
                        undelivered_orders()
                        
                        
                        
                    elif choice == '0':
                        print("Concluding the program respectfully.") # Exiting Program
                        break

        
        break
    else:
        print("The provided username or password is incorrect or invalid.") # Displaying right message
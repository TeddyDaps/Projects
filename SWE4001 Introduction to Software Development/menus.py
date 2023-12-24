
def manager_menu(): # Displaying manager's menu.
    print("Welcome, Esteemed Manager, to the Application.")
    print()
    print("---MANAGER MENU---")
    print("1. Display Total Orders per Customer")
    print("2. View Daily Orders")
    print("3. Show Total Delivered Orders")
    print("4. Calculate Total Income per Customer")
    print("5. Display Total Daily Income")
    print("6. Export List Of Customers")
    print("7. Export Orders Of Each Clerk")
    print("8. Export All Orders")
    print("0. Exit the application")
    print("--------------------------------")
    choice=input("Option: ")
    return choice # Returns as result the variable -choice-.

def clerk_menu(): # Displaying clerk's menu.
    print("We extend a warm welcome as you access our application.")
    print()
    print("---CLERK MENU---")
    print("1. Initiate Addition of a New Order")
    print("2. Outstanding or Pending Orders yet to be Delivered")
    print("0. Exit the application")
    print("--------------------------")
    choice=input("Option: ")
    return choice # Returns as result the variable choice.


def delivery_menu() : #Displaying derilvery's menu.
    print("Welcome, Delivery Personnel.")
    print()
    print("---DELIVERY MENU---")
    print("1. Finalize Order")
    print("2. View Undelivered Orders")
    print("0. Exit the application")
    print("--------------------")
    choice=input("Option: ")
    return choice # Returns as result the variable choice.
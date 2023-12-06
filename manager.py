
import csv # Importing the csv module for handling CSV files
 

def total_orders_per_customer(): 

    
    name=str(input("Enter customer's name: ")) # Asking for customer's name input:

    
    file=open("orders.csv", "r") # Open the proper .csv file (in read mode BY DEFAULT)
    reader=csv.DictReader(file)
    counter = 0
    orders=[] # Creating a new list so we can add the orders inside 
    for row in reader:
        if row['name'] == name:
            counter +=1
            orders.append(row)  # Adding the orders per customer in a new list
    
    if name in reader:
        print(f"{name} has ordered {counter} times") # Displaying proper message to the user
        answer=str.lower(input("Would you like to check them? Y/N: ")) # Waiting for user's input (asnwer)
    

    if name not in reader:
        answer = 'n'

    """
    Displaying the individual orders belonging to a customer sequentially.
    """
    if answer == 'y': #Checking asnwer input by user
        for order in orders:
            print("Order Details:")
            for order in orders:
                print(f"Order ID: {order['id']}")
                print(f"Address: {order['address']}")
                print(f"Cost: {order['cost']}")
                print(f"Date: {order['date']}")
                print(f"Delivered: {'Yes' if order['delivered'] == '1' else 'No'}")
                print(f"Description: {order['descr']}")
                print()   
    elif answer == 'n':
        print("Unfortunately, name not found")  
        print("Concluding program execution...")
        file.close()

            
        


    




def total_daily_orders():

    file=open("orders.csv")
    reader=csv.DictReader(file) # Opening and reading the correct .csv file
    orders=sum(1 for row in reader)

    print(f"The orders for the current day were {orders}") # Showing the results of the daily orders that had been staged
    print()
    
    answer=str.lower(input("Are you interested in examining today's records? Please indicate by choosing Y for yes or N for no.\n")) # Waiting for user's input
    file.close()

    if answer == 'y': # Checking user's input
        with open("orders.csv") as file:
            reader=csv.DictReader(file)
            orders_data=list(reader)



        """
        Presenting exclusively the daily orders that have been staged, allowing for ease of inspection.
        """
        for order in orders_data:
            print(f"Order ID: {order['id']}")
            print(f"Customer Name: {order['name']}")
            print(f"Address: {order['address']}")
            print(f"Cost: {order['cost']}")
            print(f"Date: {order['date']}")
            print(f"Delivered: {'Yes' if order['delivered'] == '1' else 'No'}") # Checking all the orders and displaying  executed and not carried out orders
            print(f"Description: {order['descr']}")
            print()
        file.close() # Closing the already open .csv file(Orders.csv)         
       
       





        

def total_delivered_orders():
    print("---DELIVERED ORDERS---")
        
    file=open("orders.csv") # Open the .csv file 
    reader=csv.DictReader(file)
    counter=0
    for row in reader:
        if row['delivered'] == '1': # Checking inside the .csv file if orders has been accomplished
            counter +=1
    file.close()

    print(f"The aggregate count of fulfilled orders {counter}\n") # Showing to the user the right message
    answer=str.lower(input("May I inquire if you would prefer to review the delivered orders for today? Please respond with Y for yes or N for no. ")) # Asking for user's answer input

     
    if answer == 'y': # Checking for user's input
        delivered_orders=[] # Creating a new list
    if answer == 'y':
        with open("orders.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['delivered'] == '1':
                    delivered_orders.append(row) # Adding in the list(delivered_orders) the orders that had already been settled
    elif answer == 'n':
        print("Concluding program execution...")
    file.close()

        
    """
    Presenting exclusively the daily orders that have been staged, allowing for ease of inspection

    """

    for order in delivered_orders: 
        print("Order ID:", order['id'])
        print("Customer:", order['name'])
        print("Address:", order['address'])
        print("Items:", order['descr'])
        print("Cost:", order['cost'])
        print(f"Delivered: {'Yes' if order['delivered'] == '1' else None}")
        print("---------------------------")

        

def total_income_per_customer():
    name=input("Give customer's name: ") # Asking for customer's name(user's input)
    total_income=0
    
    with open("orders.csv") as file: # Open .csv file
        reader=csv.DictReader(file)
        for row in reader:
            if row['name'] == name:
                total_income += float(row['cost']) # Adding the the cost from customer per order
        
        if name not in reader:
            print("Invalid Input:Name Not Found") # Displaying  decent message to the user
    
    print(f"The cumulative revenue generated from {name} amounts to {total_income}") 




def total_daily_income():
    daily_income =0
    with open("orders.csv") as f: # Open .csv file
        reader=csv.DictReader(f)
        for row in reader:
            daily_income += float(row['cost']) # Adding to daily_income all the costs from the .CSV file 
    
    print(f"The revenue generated for the day stands at {daily_income}") # Displaying decent message to the user




def extracting_names():
 pass

    

         

   
  
    
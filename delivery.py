import csv


def CompleteDelivery():

    rows = []
    with open('orders.csv', mode='r') as file:
        reader = csv.DictReader(file) # Read the CSV file and store the data in a list of dictionaries
        rows = list(reader)

        id=input("Give ID: ") # Ask for input 

        
        for row in rows:
            if row['id'] == id and row['delivered'] == '0': #Updating [row'delivered'] status to 1 for delivered
                row['delivered'] = '1'
                print("Successfully Uptaded")
    
    with open('orders.csv', 'w', newline='') as file: 
        fieldnames = ['id', 'name', 'address', 'descr', 'date', 'cost', 'delivered', 'clerk']  # Write the updated data back to the same CSV file
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)



